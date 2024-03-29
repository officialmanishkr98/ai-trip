import streamlit as st
from utils import main

st.set_page_config(page_title="TRAVEL ITINERARY GUIDE APP")
st.title("AI Travel Itinerary Guide System 🤖 📑")
st.subheader("Planing your vacations 📝")

place = st.text_input("Enter the place you wanted to visit")
start_date = st.date_input("Enter dates of your travel")
day_count = st.number_input("Enter number of days of your travel", min_value= 0)
submit_button = st.button("Get started")
 
if submit_button and day_count and place:
    with st.spinner("Geting best plan for your vacation..."):
        response = main(place , start_date , day_count)
        st.write(response)
        print(response)