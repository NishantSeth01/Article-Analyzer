# main.py
import streamlit as st
from login import Login
from signup import Signup
from home import Homepage

def main():
    st.title("Article Analyzer")

    # Page navigation
    page = st.radio("Select Page", ["Login", "Signup", "Homepage"])

    if page == "Login":
        login = Login()
        login.login_form()
        st.markdown('[Create an account](signup)')
    elif page == "Signup":
        signup = Signup()
        signup.signup_form()
        st.markdown('[Already have an account? Login here](login)')
    elif page == "Homepage":
        homepage = Homepage()
        homepage.show_homepage()

if __name__ == "__main__":
    main()
