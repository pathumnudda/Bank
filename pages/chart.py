import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/ea1c2191-9b4a-4059-b355-402bad609bac/GWFsZVVoPV.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

html_1 = """
<div style="background-color:#EFB9AE;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>กราฟแสดงข้อมูลการตลาดธนาคาร</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

dt=pd.read_csv('./data/bank1.csv')
st.subheader("ข้อมูลการตลาดธนาคาร")
st.write('ผลรวม')

cl1,cl2,cl3,cl4,cl5=st.columns(5)
cl1.write(dt['balance'].sum())
cl2.write(dt['housing'].sum())
cl3.write(dt['loan'].sum())
cl4.write(dt['contact'].sum())
cl5.write(dt['day'].sum())