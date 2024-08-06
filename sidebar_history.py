import streamlit as st # type: ignore
from streamlit import session_state as state # type: ignore
from streamlit_option_menu import option_menu # type: ignore
import pandas as pd
from database.database import db_instance
from datetime import datetime, timedelta
from utils.logger import print_and_log


def get_history(email):
    cursor_history = db_instance.get_history_by_email(email)
    list_history = list(cursor_history)
    return list_history
    

def sidebar_history():
    with st.sidebar:
        user_email = state.logged_user['email']
        history_items = get_history(user_email)

        if not history_items:
            st.error("이용하신 내역이 없습니다.")
            return None

        # 현재 시각
        now = datetime.now()

        # 각 카테고리에 대한 기준 시간 계산
        today_start = datetime(now.year, now.month, now.day)
        yesterday_start = today_start - timedelta(days=1)
        last_7_days_start = today_start - timedelta(days=7)
        last_month_start = today_start - timedelta(days=30)
        last_year_start = today_start - timedelta(days=365)

        # 각 카테고리별로 항목 분류
        categories = {
            '오늘': [],
            '어제': [],
            '지난 7일': [],
            '지난 30일': [],
            '지난 1년': [],
            '그 외': [],
            '전체': [],
            'Target': []
        }

        # 항목 분류
        for item in history_items:
            updated_at = item['updated_at']
            formatted_item = f"{item['subject']}"
            target_item = f"{item['target_chatbot']}"
            
            if updated_at >= today_start:
                categories['오늘'].append(formatted_item)
            elif updated_at >= yesterday_start:
                categories['어제'].append(formatted_item)
            elif updated_at >= last_7_days_start:
                categories['지난 7일'].append(formatted_item)
            elif updated_at >= last_month_start:
                categories['지난 30일'].append(formatted_item)
            elif updated_at >= last_year_start:
                categories['지난 1년'].append(formatted_item)
            else:
                categories['그 외'].append(formatted_item)
            
            if updated_at >= last_year_start:
                categories['전체'].append(formatted_item)
                categories['Target'].append(target_item)
        
        if categories['전체']:
            st.write('전체')
            selected_option = option_menu(
                "",
                categories['전체'],
                icons=["clock-history"] * len(categories['전체']),
                menu_icon="",
                default_index=0
            )
            selected_index = categories['전체'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            selected_target_chatbot = history_items[selected_index]['target_chatbot']
            return selected_session_id, selected_target_chatbot
                
        if categories['오늘']:
            st.write('오늘')
            selected_option = option_menu(
                "",
                categories['오늘'],
                icons=["clock-history"] * len(categories['오늘']),
                menu_icon="",
                default_index=-1
            )
            selected_index = categories['오늘'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            return selected_session_id

        if categories['어제']:
            st.write('어제')
            selected_option = option_menu(
                "",
                categories['어제'],
                icons=["clock-history"] * len(categories['어제']),
                menu_icon="",
                default_index=-1
            )    
            selected_index = categories['어제'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            return selected_session_id

        if categories['지난 7일']:
            st.write('지난 7일')
            selected_option = option_menu(
                "",
                categories['지난 7일'],
                icons=["clock-history"] * len(categories['지난 7일']),
                menu_icon="",
                default_index=-1
            )    
            selected_index = categories['지난 7일'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            return selected_session_id

        if categories['지난 30일']:
            st.write('지난 30일')
            selected_option = option_menu(
                "",
                categories['지난 30일'],
                icons=["clock-history"] * len(categories['지난 30일']),
                menu_icon="",
                default_index=-1
            )    
            selected_index = categories['지난 30일'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            return selected_session_id

        if categories['지난 1년']:
            st.write('지난 1년')
            selected_option = option_menu(
                "",
                categories['지난 1년'],
                icons=["clock-history"] * len(categories['지난 1년']),
                menu_icon="",
                default_index=-1
            )    
            selected_index = categories['지난 1년'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            return selected_session_id

        if categories['그 외']:
            st.write('그 외')
            selected_option = option_menu(
                "",
                categories['그 외'],
                icons=["clock-history"] * len(categories['그 외']),
                menu_icon="",
                default_index=-1
            )   
            selected_index = categories['그 외'].index(selected_option)
            selected_session_id = history_items[selected_index]['session_id']
            return selected_session_id

    print_and_log(f"sidebar_history, End")