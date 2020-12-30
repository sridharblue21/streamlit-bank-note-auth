import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time


pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def predict_value(variance,skewness,curtosis,entropy):
    predicted_value = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(predicted_value)
    return predicted_value

def main():
    st.title('Bank Authenticator')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input('Variance', 'Enter the Value')
    skewness = st.text_input('Skewness', 'Enter the Value')
    curtosis = st.text_input('Curtosis', 'Enter the Value')
    entropy  = st.text_input('Entropy',  'Enter the Value')
    result = st.empty()
    if st.button('Predict'):
        result = predict_value(variance,skewness,curtosis,entropy)
        if result == 0:
            st.success(f'The Prediction is {result}')
            st.balloons()
            st.text('*0 is Real bank note')
            st.text('*1 is Fake note')
            st.stop()
        else:
            st.error(f'The Prediction is {result}')
            st.text('*0 is Real bank note')
            st.text('*1 is Fake note')
            st.stop()


if __name__ == "__main__":
    main()