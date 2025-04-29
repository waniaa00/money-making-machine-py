import streamlit as st  #  for UI purpose
import random           #  for generating random numbers etc
import time             #  for accessing all time related functions and methods
import requests         #  for calling API to get data from internet

st.title("💰Money Making Machine")


def generate_money():
    return random.randint(1, 1000)


st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)                         #sleep method is used to delay/ postpone /pause functionality for given seconds
    amount = generate_money()
    st.success(f"You made ${amount}")


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustlers?apiKey=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")
    except:
        return("Something went wrong!")
    

st.subheader("Side Hustles Ideas")
if st.button("Generate Hustles"):
    idea = fetch_side_hustle()
    st.success(idea)


def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_making_quotes?apiKey=1234567890")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_making_quote"]
        else:
            return ("Save money. Make money.")
    except:
        return("Something went wrong!")
    
st.subheader("Money Making Quotes")
if st.button("Generate Quotes"):
    motivation = fetch_money_quotes()
    st.info(motivation)


st.write("-----------------------------")

st.write("🔹  Developed by [Wania Akram](https://github.com/waniaa00)  &nbsp;|&nbsp;  Secure & Smart  🔹")

    
