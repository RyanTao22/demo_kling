import streamlit as st
import pandas as pd


result_csv_name = 'review_results_klings_df_250203_part1.xlsx'

@st.cache_data
def load_data():
    full_df = pd.read_excel(result_csv_name )
    
    full_df.reset_index(drop=True, inplace=True)
    
    #exclude_indices = list(range(22, 88)) + list(range(97, 135))
    #full_df = full_df[~full_df.index.isin(exclude_indices)]
    #full_df = full_df[full_df['sid'] != 0]
    
    full_df = full_df.sort_values(by=['sid', 'order'])
    full_df.reset_index(drop=True, inplace=True)


    # kling = pd.read_csv(result_csv_kling, encoding='utf-8')
    # #kling = kling.iloc[15:]
    # kling.reset_index(drop=True, inplace=True)

    # return full_df, kling
    return full_df

# df_org,kling_df = load_data()
df_org = load_data()

st.dataframe(df_org.loc[[0], ['product', 'Gender', 'Age_Range', 'Household_Income', 'Ethnicity']])

row = df_org.iloc[0]

st.header("Prompt:")
prompt = row['prompt']
st.markdown(prompt.replace('$','\$').split('Requirements:')[0])

st.header("Script:")

script = row['refine_script']

st.write(script)

if st.button("Next Page"):
    st.switch_page("pages/4_Video_Review_Page.py") 
