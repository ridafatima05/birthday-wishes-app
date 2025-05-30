import streamlit as st
from datetime import datetime, date, timedelta

# 🎉 Confetti on load
st.set_page_config(page_title="Birthday Wishes App", layout="centered", page_icon="🎂")
st.title("🎂 Birthday Wishes App")

# 🧑 User inputs
name = st.text_input("Enter your name:")
birthdate = st.date_input("Select your birthdate:", min_value=date(2000, 1, 1))  # Limit to year 2000+

if name and birthdate:
    today = date.today()
    this_year_birthday = birthdate.replace(year=today.year)

    # 🎯 Adjust if birthday has passed this year
    if this_year_birthday < today:
        next_birthday = this_year_birthday.replace(year=today.year + 1)
    else:
        next_birthday = this_year_birthday

    days_left = (next_birthday - today).days

    # 🎈 Birthday today
    if days_left == 0:
        st.balloons()
        st.success(f"Happiest Birthday, {name}! 🎂")
        st.markdown("Wishing you a day filled with love, laughter, and everything that makes you smile. 🎉")
    else:
        st.info(f"✨ Countdown begins, {name}! Just **{days_left} days** to go until your birthday on **{next_birthday.strftime('%B %d')}** — get ready for some serious celebration! 🎂🎉")

    # 🎵 Optional: birthday song (local file)
    if st.checkbox("🎵 Play birthday song"):
        try:
            with open("birthday_song.mp3", "rb") as audio_file:  # Make sure this file exists in your folder
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
        except FileNotFoundError:
            st.error("🎵 The audio file 'birthday_song.mp3' was not found. Please make sure it's in the same directory.")

    # 💌 Optional: birthday message
    if st.checkbox("🎁 Show a birthday message"):
        if days_left == 0:
            # 🎉 Actual Birthday
            st.markdown(f"""
            <div style='background-color: #fff0f5; padding: 20px; border-radius: 10px; text-align: center;'>
                <h2>Dear {name},</h2>
                <p>May your birthday be the beginning of a year filled with happiness, health, and success!</p>
                <p>Hope your birthday is as special as you are to me. 🎁</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # 🎈 Advance Birthday
            st.markdown(f"""
            <div style='background-color: #f0fff4; padding: 20px; border-radius: 10px; text-align: center;'>
                <h2>Dear {name},</h2>
                <p>Your birthday is just around the corner! 🎈</p>
                <p>Wishing you an early Happy Birthday filled with excitement and happiness. 🎁</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<hr><p style='text-align: center;'>Made with ❤️ by Rida Fatima</p>", unsafe_allow_html=True)
