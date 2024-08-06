import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_extras.switch_page_button import switch_page # type: ignore


def intro_page():
    # Header
    st.title("⚖️ AI 홍변")
    st.subheader("법령 관련 챗봇 서비스")

    # Introduction
    st.write("""
    AI 홍변은 최신 인공지능 기술을 활용하여 법령 관련 질문에 신속하고 정확하게 답변을 제공하는 챗봇 서비스입니다. 
    저희 서비스를 통해 복잡한 법률 용어와 절차를 쉽게 이해하고, 필요한 정보를 빠르게 찾아볼 수 있습니다.
    """)

    # Features
    st.write("## 주요 기능")
    st.write("""
    - **빠르고 정확한 답변:** 최신 AI 기술을 통해 법령 관련 질문에 신속하고 정확하게 답변을 제공합니다.
    - **24/7 서비스:** 언제 어디서나 접속하여 서비스를 이용할 수 있습니다.
    - **사용자 친화적 인터페이스:** 누구나 쉽게 이용할 수 있도록 직관적이고 간편한 사용자 인터페이스를 제공합니다.
    """)

    # Footer
    st.write("""
    ---
    AI 홍변은 여러분의 법적 문제 해결을 도와드리기 위해 항상 최선을 다하겠습니다. 문의 사항이 있으시면 언제든지 연락주세요.
    """)
