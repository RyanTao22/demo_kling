import streamlit as st
import datetime
import pytz
#from helpers import add_row_to_responses_df, initialize_responses_df


st.title("Demographics Survey")

age = st.selectbox("Age Range", [ "18-24", "25-44",  "45-64","65+"])
gender = st.radio("Gender", ["Male", "Female", "Non-binary / third gender"])
income = st.selectbox("Household Income Range Before Taxes During the Past 12 Months", ["<25,000", "25,000-150000", "150,000+", "Prefer not to say"])
ethnicity = st.selectbox("Ethnicity", ["American Indian or Alaska Native", "Asian", "Black or African American", "Native Hawaiian or Other Pacific Islander",
                                        "White",  "Multiracial/Mixed ethnicity"])


st.write('Finalizing the questions for AI literacy...')

if st.button("Save"):
    LA_time = datetime.datetime.now(pytz.timezone('America/Los_Angeles')).strftime('%Y-%m-%d %H:%M:%S')
    row_data = [LA_time, None, age, gender,  income, ethnicity, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    #add_row_to_responses_df(row_data)
    #st.session_state.demographics_complete = True
    st.switch_page("pages/3_Prompt_Script_Page.py")  # 跳转到产品选择页面

# if __name__ == "__main__":
#     if 'responses_df' not in st.session_state:
#         initialize_responses_df()
#         st.switch_page("pages/1_exp_des.py")
#     survey_page()
