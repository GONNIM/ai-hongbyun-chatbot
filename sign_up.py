import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_extras.switch_page_button import switch_page # type: ignore
from utils.util import is_valid_email, hash_password
from database.database import db_instance  # Import the Database instance
import random
import smtplib
import datetime
from email.mime.text import MIMEText


if "signup_username" not in state:
    state.signup_username = ""
if "signup_email" not in state:
    state.signup_email = ""
if "signup_password" not in state:
    state.signup_password = ""
if "signup_password_confirm" not in state:
    state.signup_password_confirm = ""

# Email setup
EMAIL_HOST = st.secrets["EMAIL_HOST"]
EMAIL_PORT = int(st.secrets["EMAIL_PORT"])
EMAIL_HOST_USER = st.secrets["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = st.secrets["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = st.secrets["EMAIL_USE_TLS"] == "True"


def send_verification_email(email, code):
    text = f"""
안녕하세요,
아래의 인증 코드를 사용하여 AI 홍변 챗봇 서비스 가입 절차를 완료해 주시기 바랍니다:
인증 코드: **{code}**
이메일 인증을 통해 회원가입이 완료됩니다. 감사합니다.
"""
    # msg = MIMEText(f"Your verification code is {code}")
    msg = MIMEText(text)
    msg["Subject"] = "Email Verification"
    msg["From"] = EMAIL_HOST_USER
    msg["To"] = email

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.set_debuglevel(1)  # Enable debug output
            if EMAIL_USE_TLS:
                server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, email, msg.as_string())
            message = "인증코드가 귀하의 이메일로 발송되었습니다! 받은메일함을 확인해주세요."
            return True, message
    except Exception as e:
        return False, str(e)
    

def signup():
    st.write("## 회원가입")
    
    username = st.text_input("이름(닉네임)", max_chars=20, key="signup_username")
    email = st.text_input("이메일", key="signup_email")
    password = st.text_input("비밀번호", type="password", key="signup_password")
    password_confirm = st.text_input("비밀번호 확인", type="password", key="signup_password_confirm")

    sign_up_button = st.button(label='가입하기')
    if sign_up_button:
        if username == '':
            st.error("이름(닉네임)을 입력해 주세요.")
            return
        if email == '':
            st.error("이메일을 입력해 주세요.")
            return
        if password == '':
            st.error("비밀번호를 입력해 주세요.")
            return
        if password_confirm == '':
            st.error("비밀번호 확인을 입력해 주세요.")
            return
        if password != password_confirm:
            st.error("동일한 비밀번호을 입력해 주세요.")
            return

        if is_valid_email(email):
            if db_instance.get_user_by_name(username):
                st.error("이미 존재하는 이름(닉네임)입니다.")
            else:
                if db_instance.get_user_by_email(email):
                    st.error("이미 존재하는 이메일입니다.")
                else:
                    code = random.randint(100000, 999999)
                    hashed_password = hash_password(password)
                    db_instance.insert_user({
                        "email": email,
                        "password_hash": hashed_password,
                        "name": username,
                        "created_at": datetime.datetime.now(),
                        "updated_at": datetime.datetime.now(),
                        "verified": False,
                        "verification_code": code,
                        "verification_code_expires": datetime.datetime.now() + datetime.timedelta(hours=1),
                        "last_login": None,
                        "failed_login_attempts": 0,
                        "account_locked": False
                    })
                    is_success, message = send_verification_email(email, code)
                    if is_success:
                        st.success(message)
                    else:
                        st.error(message)
        else:
            st.error("유효한 이메일 주소를 입력하세요.")
