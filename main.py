import streamlit as st
import pandas as pd
import random

# Motivational quotes
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you."
]

# Function to load or create CSV file
def load_data():
    try:
        return pd.read_csv("progress.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Challenge", "Lesson Learned"])

# Function to save data
def save_data(date, challenge, lesson):
    df = load_data()
    new_data = pd.DataFrame([[date, challenge, lesson]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("progress.csv", index=False)

# Streamlit UI
st.title("🌱 Growth Mindset Tracker")
st.write("Track your daily challenges and lessons learned.")

# User input fields
date = st.date_input("Select Date")
challenge = st.text_area("What challenge did you face today?")
lesson = st.text_area("What did you learn from it?")

if st.button("Save Entry"):
    if challenge and lesson:
        save_data(date, challenge, lesson)
        st.success("Entry saved successfully!")
    else:
        st.warning("Please enter both challenge and lesson learned.")

# Show previous entries
st.subheader("📅 Your Growth Journey")
df = load_data()
st.dataframe(df)

# Show motivational quote
st.subheader("💡 Motivation for Today")
st.write(random.choice(quotes))
   