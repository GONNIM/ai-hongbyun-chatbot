import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_extras.switch_page_button import switch_page # type: ignore
from utils.util import is_valid_email
from database.database import db_instance  # Import the Database instance
import datetime


if "verify_email" not in state:
    state.verify_email = ""
if "verify_code" not in state:
    state.verify_code = ""


def verify_email():
    st.write("## 이메일 인증")
    
    email = st.text_input("이메일", key="verify_email")
    code = st.text_input("인증코드", key="verify_code")

    verify_email_button = st.button(label='인증하기')
    if verify_email_button:
        if email == '':
            st.error("이메일을 입력해 주세요.")
            return
        if code == '':
            st.error("인증코드를 입력해 주세요.")
            return

        if is_valid_email(email):
            user = db_instance.get_user_by_email(email)
            if user and user["verification_code"] == int(code):
                if user["verification_code_expires"] > datetime.datetime.now():
                    db_instance.update_user(email, {"verified": True})
                    st.success("이메일 인증이 완료되었습니다! 이제 로그인 할 수 있습니다.")
                else:
                    st.error("인증코드가 만료되었습니다.")
            else:
                st.error("유효하지 않은 이메일 또는 인증코드입니다.")
        else:
            st.error("유효한 이메일 주소를 입력하세요.")
