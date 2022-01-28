
import streamlit as st
from model import predict_yield
import numpy as np

st.set_page_config(page_title="Wild Blueberry Yield Prediction App", page_icon= "", layout="wide")
col1, col2= st.columns([3,5])

with col1:
    with st.form("Prediction Form"):
        st.header("Enter the required features")
        clonesize= st.text_input("clonesize value")
        osmia= st.text_input("osmia value")
        AverageOfUpperTRange= st.text_input("average Of Upper TRange")
        AverageOfLowerTRange= st.text_input("average Of Lower TRange")
        AverageRainingDays= st.text_input("average number of raining days")
        fruitset= st.text_input("fruitset value")
        fruitmass= st.text_input("fruitmass value")
        seeds= st.text_input("seeds value")

        submit_val=st.form_submit_button("Predict Yield")

if submit_val:
    print(clonesize)
    attribute=np.array([float(clonesize), float(osmia), float(AverageOfLowerTRange), float(AverageOfUpperTRange), float(AverageRainingDays),
    float(fruitmass), float(fruitset), float(seeds)]).reshape(1,-1)

    if attribute.shape==(1,8):
        print("Attributes are valid")
        value= predict_yield(attributes= attribute)

        with col2:
            st.header("Here are the results: ")
            st.success(f"The yield value is {value}")

