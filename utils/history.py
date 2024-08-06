import streamlit as st  # type: ignore
from streamlit import session_state as state # type: ignore
import datetime
from database.database import db_instance  # Import the Database instance
from chatbot.llm_summary import get_ai_summary


def get_history(session_id):
    history = db_instance.get_history_by_session_id(session_id)
    return history


def save_to_history(user_id, session_id, target_chatbot, subject):
    db_instance.insert_history({
        "user_id": user_id,
        "session_id": session_id,
        "target_chatbot": target_chatbot,
        "subject": subject,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    })


def save_to_history_qa(session_id, question, answer):
    db_instance.insert_history_qa({
        "session_id": session_id,
        "question": question,
        "answer": answer
    })


def add_to_history(session_id, question, answer):
    history = get_history(session_id)
    if history:
        pass
    else:
        user_id = state.logged_user['email']
        target_chatbot = state.current_chatbot
        if user_id and target_chatbot:
            subject = get_ai_summary(question, answer)
            save_to_history(user_id, session_id, target_chatbot, subject)
    save_to_history_qa(session_id, question, answer)
