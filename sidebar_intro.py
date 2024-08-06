import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_option_menu import option_menu # type: ignore


def sidebar_intro():
    with st.sidebar:
        page = option_menu(
            "AI 홍변",
            ["Intro", "Sign in", "Sign up", "Verify email"],
            icons=["bi-app-indicator", "bi-door-open-fill", "bi-signpost-fill", "bi-person-check-fill"],
            menu_icon="",
            default_index=0
        )
    return page
