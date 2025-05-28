import streamlit as st
import openai

st.title("Find Your Career Sweet Spot 🚀")
openai.api_key = st.secrets["OPENAI_API_KEY"]

with st.form("career_form"):
    passion = st.text_area("What energizes you at work?")
    strengths = st.text_area("What are your key strengths?")
    experience = st.text_area("What have you done professionally?")
    preference = st.text_area("What kind of environment do you thrive in?")
    vision = st.text_area("What is your ideal lifestyle or career goal?")
    submitted = st.form_submit_button("Get My Career Suggestions")

if submitted:
    prompt = f"""
    Based on the following:
    - Passion: {passion}
    - Strengths: {strengths}
    - Experience: {experience}
    - Workstyle: {preference}
    - Vision: {vision}

    Suggest 2–3 career directions that align with the user's 'career sweet spot'.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a friendly and insightful career coach."},
                  {"role": "user", "content": prompt}]
    )
    st.subheader("🔍 Your Career Sweet Spot")
    st.write(response['choices'][0]['message']['content'])
