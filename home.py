import streamlit as st
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import yake
from database import Database

class Homepage:
    def __init__(self):
        self.db = Database()

    def extract_keywords(text, num_keywords=5):
        custom_kw_extractor = yake.KeywordExtractor(n=1, top=num_keywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(text)
        return [keyword for keyword, score in keywords]

    def logout(self):
        st.session_state.logged_in = False
        st.experimental_rerun()

    def show_homepage(self):
        st.title("Homepage")

        # Check if the user is logged in
        if st.session_state.get('logged_in', False):
            st.title("Article Analyzer")

            # Logout button on the navigation bar
            if st.button("Logout", key="logout_btn"):
                self.logout()
                st.warning("You are not logged in. Please log in to access the homepage.")

            # User input
            article_link = st.text_input("Paste the article link here:")

            if article_link:
                # Web scraping
                response = requests.get(article_link)
                soup = BeautifulSoup(response.text, 'html.parser')
                article_text = soup.get_text()

                # Extract important keywords and phrases
                important_keywords = self.extract_keywords(article_text, num_keywords=5)

                # Display the most important keywords and phrases
                st.subheader("5 Most Important Keywords and Phrases")
                for i in range(len(important_keywords)):
                    st.write((i + 1), " ", important_keywords[i])

                # Sentiment analysis
                sentiment = TextBlob(article_text)

                # Display polarity and subjectivity
                st.write(f"Sentiment Analysis - Polarity: {sentiment.sentiment.polarity:.2f}, Subjectivity: {sentiment.sentiment.subjectivity:.2f}")

                # Word cloud
                wordcloud = WordCloud().generate(article_text)
                st.subheader("Word Cloud")
                st.image(wordcloud.to_array())

                # Create a bar chart for sentiment polarity
                st.subheader("Sentiment Analysis: Polarity")
                fig, ax = plt.subplots()
                ax.bar(["Negative", "Neutral", "Positive"], [sentiment.sentiment.polarity, 0, 1 - sentiment.sentiment.polarity])
                st.pyplot(fig)

                # Create a pie chart for sentiment subjectivity
                st.subheader("Sentiment Analysis: Subjectivity")
                fig, ax = plt.subplots()
                ax.pie([sentiment.sentiment.subjectivity, 1 - sentiment.sentiment.subjectivity], labels=["Subjective", "Objective"], autopct='%1.1f%%')
                st.pyplot(fig)
            
        else:
            st.warning("You are not logged in. Please log in to access the homepage.")
