import streamlit as st # type: ignore


def footer_page():
    # Footer with copyright notice
    footer_content = """
    <div style="text-align: center; padding: 10px 0;">
        <p>&copy; 2024 AI 홍변. All rights reserved.</p>
    </div>
    """
    st.sidebar.markdown(footer_content, unsafe_allow_html=True)
