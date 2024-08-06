import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_extras.switch_page_button import switch_page # type: ignore
import utils.util as util


def logout_page():
    st.title("감사합니다!")
    st.write("저희 [AI 홍변]을 이용해 주셔서 감사합니다. 여러분의 방문이 저희에게 큰 의미가 있습니다.")
    st.write("다시 찾아주실 날을 기다리겠습니다. 다음에 뵙기를 기대하며, 좋은 하루 되세요!")
    st.write("")

    if st.button(label="로그아웃하기"):
        st.write("로그인 페이지로 이동합니다.")
        state.logged_in = False
        state.logged_user = None
        util.init_session_id()
        util.init_message_list()
        switch_page('app')
