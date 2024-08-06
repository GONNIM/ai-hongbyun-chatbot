import streamlit as st  # type: ignore
from streamlit import session_state as state # type: ignore
import uuid
from utils.logger import print_and_log


if 'session_id' not in state:
    state.session_id = None


def start_session():
    session_id = str(uuid.uuid4())
    state.session_id = session_id
    state.message_list = []
    state.history = []
    return session_id


def end_session():
    if 'session_id' in state:
        print_and_log(f"Session {state.session_id} ended.")
        del state.session_id
        del state.message_list
