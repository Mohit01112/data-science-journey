import streamlit as st


st.title("streamlit text input")

name=st.text_input("enter your name ")


age=st.slider("select your age :",0,100,25)
st.write(f"your age is {age}.")
options=["python","java","c","c#","R"]
choice=st.selectbox("choose your favorite languagae:",options)
st.write(f"you select {choice}")




if name:
    st.write(f"hello ,{name}")

import streamlit as st
import pandas as pd
import numpy as np


df=pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[10,20,30,40]
})

## display the data frame
st.write("here is the data frame")
st.write(df)

## chart line chart

chart_data=pd.DataFrame(np.random.randn(20,4),columns=['a','b','c','d'])
st.line_chart(chart_data)


uploaded_file=st.file_uploader("choose a csv file ",type="csv")

if uploaded_file is not None:
    df.pd.read_csv(uploaded_file)
    st.write(df)