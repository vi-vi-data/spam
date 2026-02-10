import streamlit as st
import pickle

with open("spam_model.pkl", "rb") as f:
    vectorizer, svm = pickle.load(f)

st.title("SMS Spam Detector")

text = st.text_area("Enter SMS text:")

if st.button("Check"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        text_vec = vectorizer.transform([text])
        pred = svm.predict(text_vec)[0]

        st.error("SPAM 🚨" if pred else "NOT SPAM ✅")
