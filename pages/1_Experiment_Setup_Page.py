import streamlit as st

import streamlit as st
import pandas as pd
#import plotly.express as px


st.header("Experiment Setup")

# Objectives
st.subheader("Experimental Objects")
st.write("""
1. Compare **AI-generated video ads** vs **human-created ads**.
2. Evaluate **personalized AI ads** vs **non-personalized AI ads**.
3. Explore the relationship between **AI literacy** and **AI video ads receptivity** (inspired by [EXPRESS: Lower Artificial Intelligence Literacy Predicts Greater AI Receptivity](https://journals.sagepub.com/doi/10.1177/00222429251314491)).
""")

# Experimental Conditions
st.subheader("Experimental Conditions")
st.write("""
There are **7 conditions** for each product:
1. **Non-personalized Human Ad** (1 ad).
2. **Non-personalized AI Ad** (1 ad).
3. **Personalized AI Ads**:
   - Gender-based (3 ads).
   - Age-based (4 ads).
   - Income-based (3 ads).
   - Race-based (6 ads).
   - Fully personalized (all 216 combinations).
""")
#st.write(f"**Total Demographic Combinations:** 216 per product.")


# # Demographic Input
# st.subheader("Survey")
# st.write("""
# Demographic combinations:
# - **Gender:** Female, Male, Non-binary/Third gender.
# - **Ethnicity:** American Indian/Alaska Native, Asian, Black/African American, Native Hawaiian/Pacific Islander, White, Multiracial.
# - **Age Range:** 18-24, 25-44, 45-64, 65+.
# - **Household Income**(dollar): <25,000, 25,000-150,000, 150,000+.
# """)

# Total Combinations


# # Video Generation Process
# st.subheader("Video Generation Process")
# st.write("""
# 1. **Script Generation:** GPT-4o for ad scripts.
# 2. **Voice Generation:** ElevenLabs for voiceovers.
# 3. **Video Generation:** Kling for video production.
# """)

# # Outcome Measures
# st.subheader("Outcome Measures")
# st.write("""
# Participants rate the ads on a scale of 1-10 for the following metrics:
# - Satisfaction
# - Accuracy
# - Persuasiveness
# - Credibility
# - Engagement
# - Relevance
# - Creativity
# - Memorability
# - Effectiveness
# """)



if st.button("Next Page"):
    st.switch_page("pages/2_Survey_Page.py") 


