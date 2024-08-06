import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from dotenv import load_dotenv
from utils.logger import print_and_log
from utils.session import start_session, end_session
from chatbot.llm_05 import get_ai_response
import utils.history as history


# 메인 함수
def show_chatbot_labor():
    st.title("⚖️ 근로기준법 챗봇")
    caption = "무엇이든 물어보세요! 근로기준법상의 다양한 규정과 그에 따른 처벌, 노동자의 권리와 의무, 근로 조건 위반 시 대처 방법 등에 대해 자세히 알려드립니다."
    st.caption(caption)

    load_dotenv()

    if 'labor_session_id' not in state or state.labor_session_id == None:
        state.labor_session_id = start_session()

    if 'labor_message_list' not in state:
        state.labor_session_id = start_session()
    
    for message in state.labor_message_list:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    placeholder = "근로기준법에 관련된 궁금한 내용들을 말씀해 주세요!"
    if user_question := st.chat_input(placeholder=placeholder):
        with st.chat_message("user"):
            st.write(user_question)
        state.labor_message_list.append({"role": "user", "content": user_question})

        with st.spinner("답변을 생성하는 중입니다"):
            ai_response = get_ai_response(user_question)
            with st.chat_message("ai"):
                ai_message = st.write_stream(ai_response)
            state.labor_message_list.append({"role": "ai", "content": ai_message})
            if state.labor_session_id != None:
                history.add_to_history(state.labor_session_id, user_question, ai_message)
