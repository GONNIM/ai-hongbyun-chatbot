import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_option_menu import option_menu # type: ignore


def sidebar_chatbot():
    with st.sidebar:
        page = option_menu(
            "Chatbot",
            ["소득세법", "민법", "형법", "도로교통법", "근로기준법", "개인정보 보호법", "의료법"],
            icons=["bi-1-square-fill", "bi-2-square-fill", "bi-3-square-fill", "bi-4-square-fill", "bi-5-square-fill", "bi-6-square-fill", "bi-7-square-fill"],
            menu_icon="",
            default_index=0
        )
    return page
