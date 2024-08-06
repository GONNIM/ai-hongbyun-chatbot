import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from sidebar_intro import sidebar_intro
from intro import intro_page
from sign_in import signin
from sign_up import signup
from verify_email import verify_email


if 'current_intro' not in state:
    state.current_intro = "Intro"


def navigate_intro_page():
    state.current_intro = sidebar_intro()
    if state.current_intro == "Intro":
        intro_page()
    elif state.current_intro == "Sign in":
        signin()
    elif state.current_intro == "Sign up":
        signup()
    elif state.current_intro == "Verify email":
        verify_email()
