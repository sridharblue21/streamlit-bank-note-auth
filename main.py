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
    variance = st.number_input('Variance',min_value=-7,max_value=7,value=1,step=1)
    skewness = st.number_input('Skewness',min_value=-7,max_value=7,value=1,step=1)
    curtosis = st.number_input('Curtosis',min_value=-7,max_value=7,value=1,step=1)
    entropy  = st.number_input('Entropy',min_value=-7,max_value=7,value=1,step=1)
    result = st.empty()
    if st.button('Predict'):
        result = predict_value(variance,skewness,curtosis,entropy)
        if result == 0:
            st.success(f'The Prediction is {result}')
            st.balloons()
            st.markdown('*_0 is Real bank note_*')
            st.markdown('*_1 is Fake note_*')
            st.stop()
        else:
            st.error(f'The Prediction is {result}')
            st.markdown('*_0 is Real bank note_*')
            st.markdown('*_1 is Fake note_*')
            st.stop()


if __name__ == "__main__":
    main()
