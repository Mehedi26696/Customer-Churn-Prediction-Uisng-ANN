

import pandas as pd
import numpy as np
import pickle

import streamlit as st


# Custom CSS for a better UI
st.markdown(
    """
    <style>
    /* Center the Predict button */
    div.stButton {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;

    }

    /* Center the prediction result */
    div.prediction-result {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
        font-size: 18px;
        font-weight: bold;
    }

    /* Red text for "not likely to churn" */
    .result-not-churn {
        color: #dc3545;  
    }

    /* Green text for "likely to churn" */
    .result-churn {
        color: #28a745;
    }
    </style>
    """,
    unsafe_allow_html=True

)
 

st.title('Churn Prediction App')


gender = st.selectbox('Gender', ['Female','Male'])

if 'Gender' == 'Female':
    gender = 1
else:
    gender = 0



SeniorCitizen = st.selectbox('Senior Citizen', ["Yes", "No"])

if SeniorCitizen == 'Yes':
    SeniorCitizen = 1
else:
    SeniorCitizen = 0


Partner = st.selectbox('Partner', ['Yes', 'No'])

if Partner == 'Yes':
    Partner = 1
else:
    Partner = 0

Dependents = st.selectbox('Dependents', ['Yes', 'No'])

if Dependents == 'Yes':
    Dependents = 1
else:
    Dependents = 0

tenure = st.number_input('Tenure', min_value=0, max_value=100, value=0)

PhoneService = st.selectbox('Phone Service', ['Yes', 'No'])

if PhoneService == 'Yes':
    PhoneService = 1
else:
    PhoneService = 0

MultipleLines = st.selectbox('Multiple Lines', ['Yes', 'No'])

if MultipleLines == 'Yes':
    MultipleLines = 1
else:
    MultipleLines = 0

OnlineSecurity = st.selectbox('Online Security', ["Yes", "No"])

if OnlineSecurity == 'Yes':
    OnlineSecurity = 1
else:
    OnlineSecurity = 0

OnlineBackup = st.selectbox('Online Backup', ['Yes', 'No'])

if OnlineBackup == 'Yes':
    OnlineBackup = 1
else:
    OnlineBackup = 0

DeviceProtection = st.selectbox('Device Protection', ['Yes', 'No'])

if DeviceProtection == 'Yes':
    DeviceProtection = 1
else:
    DeviceProtection = 0

TechSupport = st.selectbox('Tech Support', ['Yes', 'No'])

if TechSupport == 'Yes':
    TechSupport = 1
else:
    TechSupport = 0

StreamingTV = st.selectbox('Streaming TV', ['Yes', 'No'])

if StreamingTV == 'Yes':
    StreamingTV = 1
else:
    StreamingTV = 0

StreamingMovies = st.selectbox('Streaming Movies', ['Yes', 'No'])

if StreamingMovies == 'Yes':
    StreamingMovies = 1
else:
    StreamingMovies = 0

PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])

if PaperlessBilling == 'Yes':
    PaperlessBilling = 1
else:
    PaperlessBilling = 0

MonthlyCharges = st.number_input('Monthly Charges', min_value=0.0, max_value=1000.0, value=0.0)

TotalCharges = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, value=0.0)

InternetService = st.selectbox('Internet Service', ['No', 'DSL', 'Fiber optic'])

InternetService_No, InternetService_DSL, InternetService_Fiber_optic = 0, 0, 0

if InternetService == 'No':
    InternetService_No = 1
    InternetService_DSL = 0
    InternetService_Fiber_optic = 0
elif InternetService == 'DSL':
    InternetService_No = 0
    InternetService_DSL = 1
    InternetService_Fiber_optic = 0
else:
    InternetService_No = 0
    InternetService_DSL = 0
    InternetService_Fiber_optic = 1

Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])

Contract_Month_to_month , Contract_One_year, Contract_Two_year = 0, 0, 0
if Contract == 'Month-to-month':
    Contract_Month_to_month = 1
    Contract_One_year = 0
    Contract_Two_year = 0
elif Contract == 'One year':
    Contract_Month_to_month = 0
    Contract_One_year = 1
    Contract_Two_year = 0
else:
    Contract_Month_to_month = 0
    Contract_One_year = 0
    Contract_Two_year = 1

PaymentMethod = st.selectbox('Payment Method', ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])

PaymentMethod_Bank_transfer_automatic, PaymentMethod_Credit_card_automatic, PaymentMethod_Electronic_check, PaymentMethod_Mailed_check = 0, 0, 0, 0

if PaymentMethod == 'Bank transfer (automatic)':
    PaymentMethod_Bank_transfer_automatic = 1
    PaymentMethod_Credit_card_automatic = 0
    PaymentMethod_Electronic_check = 0
    PaymentMethod_Mailed_check = 0

elif PaymentMethod == 'Credit card (automatic)':
    PaymentMethod_Bank_transfer_automatic = 0
    PaymentMethod_Credit_card_automatic = 1
    PaymentMethod_Electronic_check = 0
    PaymentMethod_Mailed_check = 0

elif PaymentMethod == 'Electronic check':
    PaymentMethod_Bank_transfer_automatic = 0
    PaymentMethod_Credit_card_automatic = 0
    PaymentMethod_Electronic_check = 1
    PaymentMethod_Mailed_check = 0

else:
    PaymentMethod_Bank_transfer_automatic = 0
    PaymentMethod_Credit_card_automatic = 0
    PaymentMethod_Electronic_check = 0
    PaymentMethod_Mailed_check = 1



data = {
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [Dependents],
    'tenure': [tenure],
    'PhoneService': [PhoneService],
    'MultipleLines': [MultipleLines],
    'OnlineSecurity': [OnlineSecurity],
    'OnlineBackup': [OnlineBackup],
    'DeviceProtection': [DeviceProtection],
    'TechSupport': [TechSupport],
    'StreamingTV': [StreamingTV],
    'StreamingMovies': [StreamingMovies],
    'PaperlessBilling': [PaperlessBilling],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges],
    'InternetService_No': [InternetService_No],
    'InternetService_DSL': [InternetService_DSL],
    'InternetService_Fiber_optic': [InternetService_Fiber_optic],
    'Contract_Month_to_month': [Contract_Month_to_month],
    'Contract_One_year': [Contract_One_year],
    'Contract_Two_year': [Contract_Two_year],
    'PaymentMethod_Bank_transfer_automatic': [PaymentMethod_Bank_transfer_automatic],
    'PaymentMethod_Credit_card_automatic': [PaymentMethod_Credit_card_automatic],
    'PaymentMethod_Electronic_check': [PaymentMethod_Electronic_check],
    'PaymentMethod_Mailed_check': [PaymentMethod_Mailed_check]
    }
df = pd.DataFrame(data).astype(float)
 
cols_to_scale = ['tenure', 'MonthlyCharges', 'TotalCharges']
 

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])



# model loading

model = pickle.load(open('model.pkl', 'rb'))

prediction = model.predict(df)
 


if st.button('Predict'):
    if prediction == 1:
        st.markdown(
            '<div class="prediction-result result-churn">Customer is likely to churn</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="prediction-result result-not-churn">Customer is not likely to churn</div>',
            unsafe_allow_html=True
        )
