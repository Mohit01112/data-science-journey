import streamlit as st
import pandas as pd
import numpy as np


## title of the application
st.title("hello streamlit")

## display the simple text
st.write("this is a simple text")

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