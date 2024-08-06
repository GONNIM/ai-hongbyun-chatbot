import streamlit as st # type: ignore


def user_guide():
    # User Guide
    st.write("## 사용안내")
    st.write("""
    AI 홍변은 다음과 같은 기능을 제공합니다:
    1. **법령 검색:** 특정 법령의 내용을 검색하고 필요한 정보를 확인할 수 있습니다.
    2. **질의 응답:** 법령 관련 질문을 입력하면 AI가 신속하게 답변을 제공합니다.
    3. **상담 기록:** 이전 상담 내용을 조회하고 관리할 수 있습니다.
    """)


def main_feature():
    # Main Features
    st.write("## 주요기능")
    st.write("""
    ##### **법령 검색** 
    - 원하는 법령을 검색하고 상세 내용을 확인할 수 있습니다.
    - 최신 법령 업데이트와 개정 사항을 제공합니다.
    ##### **질의 응답** 
    - 법률 용어, 절차, 사례 등에 대해 질문하면 AI가 상세히 설명합니다.
    - 질문 히스토리를 저장하여 필요할 때 다시 확인할 수 있습니다.
    ##### **사용자 맞춤형 서비스** 
    - 사용자의 검색 및 질의 패턴을 분석하여 맞춤형 법령 정보를 제공합니다.
    - 개인 맞춤형 알림 설정이 가능합니다.
    """)
    st.write("")


def legal_updates():
    # Legal Updates
    st.write("## 최신 법령 업데이트")
    st.write("""
    최신 법령과 개정 사항을 실시간으로 확인하세요. 중요한 법령 변경 사항을 놓치지 않고 챙길 수 있습니다.
    """)


def user_interface():
    # User Interface
    st.write("## 사용자 인터페이스")
    st.write("""
    - **검색 창:** 원하는 법령 또는 질문을 입력하여 검색하세요.
    - **질의 응답 창:** 실시간 채팅으로 법령 관련 질문에 답변을 받을 수 있습니다.
    - **알림 센터:** 법령 업데이트와 관련된 알림을 확인할 수 있습니다.
    """)


def call_to_action():
    st.write("## 시작하기")
    st.write("""
    지금 바로 질문을 입력하여 AI 홍변의 법령 관련 챗봇 서비스를 이용해 보세요. 신속하고 정확한 답변을 통해 법적 문제를 해결하는데 도움을 드립니다.
    """)
    st.write("AI 홍변을 통해 보다 편리하게 법령 정보를 이용하세요. 감사합니다~!")


def main_page():
    # Welcome Message
    st.write("""
    환영합니다, AI 홍변에 오신 것을 환영합니다! 
    이곳에서 법령 관련 궁금증을 빠르고 정확하게 해결할 수 있습니다.
    """)

    st.write("")

    # Tabs for Sign In and Sign Up
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["사용안내", "주요기능", "최신 법령 업데이트", "사용자 인터페이스", "시작하기"])

    with tab1:
        user_guide()
    
    with tab2:
        main_feature()

    with tab3:
        legal_updates()
    
    with tab4:
        user_interface()
    
    with tab5:
        call_to_action()

    st.write("")
