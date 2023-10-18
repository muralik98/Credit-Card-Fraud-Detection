import streamlit as st
import pandas as pd
import numpy as np
import pickle


file1 = open('best_model_final.pkl', 'rb')
model = pickle.load(file1)
file1.close()

data = pd.read_csv("X_train_smote.csv")

st.title("Fraud Prediction")

Merchant_Category= st.selectbox('Transaction Category', data['Shopping_Category'].unique())

Transaction_Amount= st.number_input('Amount', min_value=0, max_value=200000, value="min", step=1)

User_Gender= st.selectbox('Gender', data['gender'].unique())

User_Latitude= st.number_input('Latitude', min_value=-90.0, max_value=90.0, value="min", step=0.1)

User_Longitude= st.number_input('User Longitude', min_value=-90.0, max_value=90.0, value="min", step=0.1)

#City_Population= st.number_input('User Population', min_value=0, max_value=200000, value="min", step=1)

Merchant_Latitude= st.number_input('Merchant Latitude', min_value=-90.0, max_value=90.0, value="min", step=0.1)

Merchant_Longitude= st.number_input('Merchant Longitude', min_value=-90.0, max_value=90.0, value="min", step=0.1)

User_age = st.number_input('User Age', min_value=0, max_value=100, value="min", step=1)

trans_time_hour = st.number_input('Transaction Time in Hour(24hr Format)', min_value=0, max_value=24, value="min", step=1)






if st.button('Fraud Status'):

    query = pd.DataFrame([[Merchant_Category, Transaction_Amount, User_Gender, User_Latitude, User_Longitude,  Merchant_Latitude, Merchant_Longitude, User_age, trans_time_hour ]],
                         columns=data.columns)


    prediction = int((model.predict(query)))

    if prediction==1:
        st.title("Fraud Detected!! Block Your Card Immediately")

    if prediction==0:
        st.title("No Suspicious Transaction!!")