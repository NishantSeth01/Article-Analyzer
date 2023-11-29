import streamlit as st
from database import Database

class Signup:
    def __init__(self):
        self.db = Database()

    def signup_form(self):
        st.title("Signup")
        new_username_signup = st.text_input("Choose a username:")
        new_password_signup = st.text_input("Choose a password:", type="password")

        if st.button("Signup"):
            self.validate_signup(new_username_signup, new_password_signup)

    def validate_signup(self, username, password):
        existing_user = self.db.validate_signup(username)
        if existing_user:
            st.error("Username already exists. Please choose a different one.")
        else:
            self.db.insert_user(username, password)
            st.success("Signup successful! You can now login.")
