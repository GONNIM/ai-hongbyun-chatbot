import os
import re
import bcrypt
from streamlit import session_state as state # type: ignore


# Initialize
if 'tax_message_list' not in state:
    state.tax_message_list = []

if 'civil_message_list' not in state:
    state.civil_message_list = []

if 'criminal_message_list' not in state:
    state.criminal_message_list = []

if 'traffic_message_list' not in state:
    state.traffic_message_list = []

if 'labor_message_list' not in state:
    state.labor_message_list = []

if 'privacy_message_list' not in state:
    state.privacy_message_list = []

if 'medical_message_list' not in state:
    state.medical_message_list = []


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


def init_session_id():
    state.tax_session_id = None
    state.civil_session_id = None
    state.criminal_session_id = None
    state.traffic_session_id = None
    state.labor_session_id = None
    state.privacy_session_id = None
    state.medical_session_id = None


def init_message_list():
    state.tax_message_list = []
    state.civil_message_list = []
    state.criminal_message_list = []
    state.traffic_message_list = []
    state.labor_message_list = []
    state.privacy_message_list = []
    state.medical_message_list = []


def get_chroma_directory():
    current_directory = os.getcwd()
    persist_directory = os.path.join(current_directory, 'ai_hongbyun_data')
    return persist_directory