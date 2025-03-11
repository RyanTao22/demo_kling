import streamlit as st

st.header("Score the Advertising Videos")
st.write("Please score the advertising videos you watched on the bottom 3 pages.")

satisfaction = st.slider("Satisfaction (1-10)", 1, 10, 6)
accuracy = st.slider("Accuracy (1-10)", 1, 10, 6)
persuasiveness = st.slider("Persuasiveness (1-10)", 1, 10, 6)
credibility = st.slider("Credibility (1-10)", 1, 10, 6)
engagement = st.slider("Engagement (1-10)", 1, 10, 6)
relevance = st.slider("Relevance (1-10)", 1, 10, 6)
creativity = st.slider("Creativity (1-10)", 1, 10, 6)
memorability = st.slider("Memorability (1-10)", 1, 10, 6)
effectiveness = st.slider("Effectiveness (1-10)", 1, 10, 6)





