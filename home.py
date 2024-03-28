import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/b1a54132-656b-4938-b386-4b485b797dd4/fL1DLtzzN1.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/chart.py", label="การทำนายข้อมูลการตลาดธนาคาร", icon="1️⃣")
st.page_link("pages/statistic.py", label="การทำนายข้อมูลการตลาดธนาคารด้วยเทคนิค", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")