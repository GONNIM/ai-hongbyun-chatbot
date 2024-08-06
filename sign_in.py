import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from utils.util import is_valid_email, check_password
from database.database import db_instance  # Import the Database instance
import datetime
import utils.util as util


if "signin_email" not in state:
    state.signin_email = ""
if "signin_password" not in state:
    state.signin_password = ""


def login_update(user, is_success):
    if is_success:
        update_field = {
            "last_login": datetime.datetime.now()
        }
    else:
        fail_count = user.get('failed_login_attempts')
        fail_count += 1
        update_field = {
            "failed_login_attempts": fail_count
        }
    email = user.get('email')
    db_instance.update_user(email, update_field)


@st.dialog("AI 홍변")
def greeting(user):
    st.write(f"[{user['name']}]님을 환영합니다!")
    if st.button("확인"):
        util.init_session_id()
        util.init_message_list()
        st.rerun()


def signin():
    st.write("## 로그인")

    email = st.text_input("이메일", key="signin_email")
    password = st.text_input("비밀번호", type="password", key="signin_password")

    sign_in_button = st.button(label='로그인')
    if sign_in_button:
        if email == '':
            st.error("이메일을 입력해 주세요.")
            return
        if password == '':
            st.error("비밀번호를 입력해 주세요.")
            return

        if is_valid_email(email):
            try:
                user = db_instance.get_user_by_email(email)
                if user and 'password_hash' in user:
                    if check_password(password, user['password_hash']):
                        if user.get('verified', False):
                            login_update(user, True)
                            state.logged_in = True
                            state.logged_user = user
                            st.success("로그인 성공!")
                            st.balloons()
                            greeting(user)
                        else:
                            login_update(user, False)
                            st.error("이메일 인증이 완료되지 않았습니다.")
                    else:
                        login_update(user, False)
                        st.error("유효하지 않은 비밀번호입니다.")
                else:
                    st.error("유효하지 않은 이메일입니다.")
            except Exception as e:
                st.error(f"오류 발생: {str(e)}")
        else:
            st.error("유효한 이메일 주소를 입력하세요.")
