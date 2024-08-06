import streamlit as st # type: ignore
from pymongo import MongoClient # type: ignore


class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
    
    # Collection, [users]
    def get_user_by_email(self, email):
        users_collection = self.db['users']
        return users_collection.find_one({"email": email})
    
    def get_user_by_name(self, username):
        users_collection = self.db['users']
        return users_collection.find_one({"username": username})
    
    def insert_user(self, user_data):
        users_collection = self.db['users']
        users_collection.insert_one(user_data)
    
    def update_user(self, email, update_fields):
        users_collection = self.db['users']
        users_collection.update_one({"email": email}, {"$set": update_fields})
    
    # Collection, [history]
    def get_history_by_session_id(self, session_id):
        history_collection = self.db['history']
        return history_collection.find_one({"session_id": session_id})
    
    def get_history_by_email(self, email):
        history_collection = self.db['history']
        return history_collection.find({"user_id": email}).sort("updated_at", -1)
    
    def insert_history(self, history_data):
        history_collection = self.db['history']
        history_collection.insert_one(history_data)

    # Collection, [history_qa]
    def get_history_qa_by_session_id(self, session_id):
        history_qa_collection = self.db['history_qa']
        return history_qa_collection.find({"session_id": session_id})
    
    def insert_history_qa(self, history_qa_data):
        history_qa_collection = self.db['history_qa']
        history_qa_collection.insert_one(history_qa_data)


M_CLUSTER=st.secrets["M_CLUSTER"]
M_USER=st.secrets["M_USER"]
M_PW=st.secrets["M_PW"]
M_DB_NAME=st.secrets["M_DB_NAME"]

M_URI = f"mongodb+srv://{M_USER}:{M_PW}@{M_CLUSTER.lower()}.bmxugol.mongodb.net/?retryWrites=true&w=majority&appName={M_CLUSTER}"

db_instance = Database(M_URI, M_DB_NAME)
