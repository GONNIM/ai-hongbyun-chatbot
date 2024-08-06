import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from sidebar_main import sidebar_main
from sidebar_chatbot import sidebar_chatbot
from sidebar_history import sidebar_history
from header import header_page
from footer import footer_page
from logout import logout_page
from router.main import main_page
from router.chatbot_01_tax import show_chatbot_tax
from router.chatbot_02_civil import show_chatbot_civil
from router.chatbot_03_criminal import show_chatbot_criminal
from router.chatbot_04_traffic import show_chatbot_traffic
from router.chatbot_05_labor import show_chatbot_labor
from router.chatbot_06_privacy import show_chatbot_privacy
from router.chatbot_07_medical import show_chatbot_medical
from router.history import show_history


if 'current_menu' not in state:
    state.current_menu = "Main"

if 'current_chatbot' not in state:
    state.current_chatbot = "소득세법"

if 'current_history' not in state:
    state.current_history = None


def navigate_page():
    state.current_menu = sidebar_main()
    if state.current_menu == "Main":
        header_page()        
        main_page()
    elif state.current_menu == "Chatbot":
        state.current_chatbot = sidebar_chatbot()
        if state.current_chatbot == "소득세법":
            show_chatbot_tax()
        elif state.current_chatbot == "민법":
            show_chatbot_civil()
        elif state.current_chatbot == "형법":
            show_chatbot_criminal()
        elif state.current_chatbot == "도로교통법":
            show_chatbot_traffic()
        elif state.current_chatbot == "근로기준법":
            show_chatbot_labor()
        elif state.current_chatbot == "개인정보 보호법":
            show_chatbot_privacy()
        elif state.current_chatbot == "의료법":
            show_chatbot_medical()
    elif state.current_menu == "History":
        state.current_history_session_id, state.current_history_target_chatbot = sidebar_history()
        if state.current_history_session_id and state.current_history_target_chatbot:
            show_history()
    elif state.current_menu == "Logout":
        header_page()
        logout_page()

    footer_page()
