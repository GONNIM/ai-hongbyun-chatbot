import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_option_menu import option_menu # type: ignore


def sidebar_main():
    with st.sidebar:
        page = option_menu(
            state.logged_user['name'],
            ["Main", "Chatbot", "History", "Logout"],
            icons=["bi-chat-square-text-fill", "bi-chat-square-dots-fill", "bi-bookmarks-fill", "bi-box-arrow-right"],
            menu_icon="",
            default_index=0
        )
    return page
