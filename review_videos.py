import streamlit as st
from helpers import initialize_responses_df

# Sidebar navigation
st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", ["Experiment Design","Survey Page", "Prompt & Script","Video (in Review)", "Score the Video"], key='page')

if page_selection == "Experiment Design":
    st.switch_page("pages/1_Experiment_Setup_Page.py")
elif page_selection == "Survey Page":
    st.switch_page("pages/2_Survey_Page.py")
elif page_selection == "Prompt & Script":
    st.switch_page("pages/3_Prompt_Script_Page.py")
elif page_selection == "Video (in Review)":
    st.switch_page("pages/4_Video_Review_Page.py")
elif page_selection == "Score the Video":
    st.switch_page("pages/5_Score_Video_Page.py")
