import streamlit as st
import pickle
import pandas as pd
import math
from datetime import datetime


pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

st.title('Car Price Prediction App')

name = st.text_input("Enter the car name", value="Ford EcoSport Titanium")
company = st.text_input("Enter the car company",value="Ford")
year = st.number_input("Enter the car year", min_value=1900, step=1)
kms_driven = st.number_input("Enter the km driven", min_value=0, step=1)
fuel_type = st.text_input("Enter the fuel type",value="Diesel")
fuel_type = fuel_type.strip().title()

if st.button('Predict'):
    try:
        if year <= datetime.now().year:
            input_df = pd.DataFrame(
                [[name, company, int(year), int(kms_driven), fuel_type]],
                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
            )
            prediction = pipe.predict(input_df)
            st.success('The car price is: {}'.format(math.ceil(prediction[0] * 1.6)))
        else:
            st.error("⚠️ Year cannot be in the future.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

