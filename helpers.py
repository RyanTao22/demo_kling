import streamlit as st
import pandas as pd
import numpy as np



def initialize_responses_df():
    if 'responses_df' not in st.session_state:
        data = {
            'Timestamp_LA': [],
            'Test_Group': [],
            'Age_Range': [],
            'Gender': [],
            'Education_Level': [],
            'Household_Income': [],
            'Ethnicity': [],
            'Product_Choice_1': [],
            'Product_Choice_2': [],
            'Product_Choice_3': [],
            "Prompt": [],
            "Script": [],
            "Video_url": [],
            "Satisfaction": [],
            "Accuracy": [],
            "Persuasiveness": [],
            "Credibility": [],
            "Engagement": [],
            "Relevance": [],
            "Creativity": [],
            "Memorability": [],
            "Effectiveness": []
        }
        st.session_state.responses_df = pd.DataFrame(data)
    
    if 'demographics_complete' not in st.session_state:
        st.session_state.demographics_complete = False

    if 'product_choice_complete' not in st.session_state:
        st.session_state.product_choice_complete = False

    if 'group' not in st.session_state:
        st.session_state.group = ""

    if 'prompt' not in st.session_state:
        st.session_state.prompt = ""

    if 'script' not in st.session_state:
        st.session_state.script = ""

def get_last_index():
    return len(st.session_state.responses_df) - 1

def add_row_to_responses_df(row_data):
    st.session_state.responses_df.loc[len(st.session_state.responses_df)] = row_data

def update_responses_df(row_index, column_name, value):
    st.session_state.responses_df.at[row_index, column_name] = value

def display_responses_df():
    st.dataframe(st.session_state.responses_df)
