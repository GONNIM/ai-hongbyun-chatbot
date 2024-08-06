import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from dotenv import load_dotenv
from utils.logger import print_and_log
from utils.session import start_session, end_session
from chatbot.llm_02 import get_ai_response
import utils.history as history


# 메인 함수
def show_chatbot_civil():
    st.title("⚖️ 민법 챗봇")
    caption = "무엇이든 물어보세요! 계약, 소유, 상속, 채무 등 다양한 개인 권리와 의무에 관해 자세히 알려드립니다."
    st.caption(caption)

    load_dotenv()

    if 'civil_session_id' not in state or state.civil_session_id == None:
        state.civil_session_id = start_session()

    if 'civil_message_list' not in state:
        state.civil_session_id = start_session()
    
    for message in state.civil_message_list:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    placeholder = "계약, 소유, 상속, 채무에 관련된 궁금한 내용들을 말씀해 주세요!"
    if user_question := st.chat_input(placeholder=placeholder):
        with st.chat_message("user"):
            st.write(user_question)
        state.civil_message_list.append({"role": "user", "content": user_question})

        with st.spinner("답변을 생성하는 중입니다"):
            ai_response = get_ai_response(user_question)
            with st.chat_message("ai"):
                ai_message = st.write_stream(ai_response)
            state.civil_message_list.append({"role": "ai", "content": ai_message})
            if state.civil_session_id != None:
                history.add_to_history(state.civil_session_id, user_question, ai_message)
