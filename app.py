import streamlit as st

# Create a text message and a button
message = st.empty()
button = st.button("Click me!")

# When the button is clicked, update the text message
if button:
    message.markdown("Thank you for clicking the button!")
