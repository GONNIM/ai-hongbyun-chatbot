import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
import pandas as pd
from database.database import db_instance
from utils.logger import print_and_log


if 'current_history_session_id' not in state:
    state.current_history_session_id = None

if 'current_history_target_chatbot' not in state:
    state.current_history_target_chatbot = None


def get_history_qa(selected_id):
    cursor_history_qa = db_instance.get_history_qa_by_session_id(selected_id)
    list_history_qa = list(cursor_history_qa)
    return list_history_qa


def show_history():
    title = f"⚖️ {state.current_history_target_chatbot} 챗봇 히스토리"
    st.title(title)
    caption = f"{state.current_history_target_chatbot} 챗봇 히스토리를 조회하고 상세 내용을 확인하세요."
    st.caption(caption)

    if state.logged_user and state.current_history_session_id:
        message_list = []

        history_qa = get_history_qa(state.current_history_session_id)
        if history_qa:
            for item in history_qa:
                question = item['question']
                if question:
                    message_list.append({"role": "user", "content": question})
                answer = item['answer']
                if answer:
                    message_list.append({"role": "ai", "content": answer})
        
        if message_list:
            for message in message_list:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
