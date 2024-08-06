import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from dotenv import load_dotenv
from utils.logger import print_and_log
from utils.session import start_session, end_session
from chatbot.llm_03 import get_ai_response
import utils.history as history


# 메인 함수
def show_chatbot_criminal():
    st.title("⚖️ 형법 챗봇")
    caption = "무엇이든 물어보세요! 다양한 범죄와 그에 따른 처벌, 자기 방어, 개인의 권리와 보호에 관해 자세히 알려드립니다."
    st.caption(caption)

    load_dotenv()

    if 'criminal_session_id' not in state or state.criminal_session_id == None:
        state.criminal_session_id = start_session()

    if 'criminal_message_list' not in state:
        state.criminal_session_id = start_session()
    
    for message in state.criminal_message_list:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    placeholder = "다양한 범죄와 그에 따른 처벌, 자기 방어, 개인의 권리와 보호에 관련된 궁금한 내용들을 말씀해 주세요!"
    if user_question := st.chat_input(placeholder=placeholder):
        with st.chat_message("user"):
            st.write(user_question)
        state.criminal_message_list.append({"role": "user", "content": user_question})

        with st.spinner("답변을 생성하는 중입니다"):
            ai_response = get_ai_response(user_question)
            with st.chat_message("ai"):
                ai_message = st.write_stream(ai_response)
            state.criminal_message_list.append({"role": "ai", "content": ai_message})
            if state.criminal_session_id != None:
                history.add_to_history(state.criminal_session_id, user_question, ai_message)
