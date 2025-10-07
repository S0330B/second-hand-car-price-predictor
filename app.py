import streamlit as st
import pickle
import pandas as pd
import math

pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

st.title('Car Price Prediction App')

name = st.text_input("Enter the car name")
company = st.text_input("Enter the car company")
year = st.number_input("Enter the car year", min_value=1900, max_value=2100, step=1)
kms_driven = st.number_input("Enter the km driven", min_value=0, step=1)
fuel_type = st.text_input("Enter the fuel type")
fuel_type = fuel_type.strip().title()

if st.button('Predict'):
    input_df = pd.DataFrame([[name, company, int(year), int(kms_driven), fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = pipe.predict(input_df)

    st.success('The car price is: {}'.format(math.ceil(prediction[0])))
