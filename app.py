import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from navigate import navigate_page
from navigate_intro import navigate_intro_page


# Page configuration
st.set_page_config(page_title="AI 홍변", page_icon="⚖️")


# Initialize Session.
if 'logged_in' not in state:
    state.logged_in = False

if 'logged_user' not in state:
    state.logged_user = None

if state.logged_in and state.logged_user:
    navigate_page()
else:
    navigate_intro_page()
