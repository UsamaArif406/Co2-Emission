import streamlit as st
import pandas as pd
# Load the trained model
from joblib import load
loaded_model = load('final_model.joblib')
# Add titles and headings
st.title('Vehicle CO2 Emission Prediction')
st.sidebar.title("Input Data")

# User input form
transmission = st.sidebar.selectbox('Transmission', ['M5', 'SAT5', 'A8', 'M6', 'A6', 'SA6', 'A9', 'SAT6', 'A5', '7DCT',
       'MPS6', 'A8_AWD', 'DCT7', 'M6_AWD', 'A6_AWD', 'MPS6_AWD', 'CVT',
       '5MT', '6MT', 'DCT6', 'A9_AWD', '6_speed_auto_DCT', 'A7', '4AT',
       'A4', 'MT5', 'AMT5', 'MT6', 'DCT8', 'E_CVT', '8AT', 'M7', '6AT',
       'AT', 'Manual', '8A_AWD', 'AT6', 'Automatic', 'SA5', '8_speed',
       'SA7', 'eCVT', 'MT7', '7_Speed_DCT', 'AC', '7AT_FWD', '8AT_FWD',
       '8AT_AWD'])
fuel_type = st.sidebar.selectbox('Fuel Type', ['Petrol', 'Diesel', 'Electricity/Petrol', 'Petrol Electric',
       'Diesel Electric', 'Petrol/LPG', 'Petrol Hybrid'])

powertrain = st.sidebar.selectbox('Powertrain', ['Internal_Combustion_Engine_(ICE)',
       'Plug_in_Hybrid_Electric_Vehicle_(PHEV)',
       'Hybrid_Electric_Vehicle_(HEV)',
       'Mild_Hybrid_Electric_Vehicle_(MHEV)',
       'Micro_Hybrid'])
engine_power = st.sidebar.number_input('Engine Power (PS)', min_value=1.0, max_value=1000.0, step=1.0, value=10.3)
fuel_consumption = st.sidebar.number_input('Fuel Consumption Comb (L/100 km)', min_value=1.0, max_value=1000.0, step=0.1, value=8.0)
engine_capacity = st.sidebar.number_input('Engine Capacity (L)', min_value=0.1, max_value=1000.0, step=0.1, value=1.6)

# Ranges and types
# ranges_and_types = [
#     (1, 50, 'B'),
#     (51, 75, 'C'),
#     (76, 90, 'D'),
#     (91, 100, 'E'),
#     (101, 110, 'F'),
#     (111, 130, 'G'),
#     (131, 150, 'H'),
#     (151, 170, 'I'),
#     (171, 190, 'J'),
#     (191, 225, 'K'),
#     (226, 255, 'L'),
#     (256, float('inf'), 'M')
# ]

# Button to make predictions
if st.button('Check Results'):
    # User input to DataFrame
    user_input_df = pd.DataFrame([{
        'Transmission': transmission,
        'Fuel Type': fuel_type,
        'Powertrain': powertrain,
        'Engine Power (PS)': engine_power,
        'Fuel Consumption Comb (L/100 km)': fuel_consumption,
        'Engine Capacity (L)': engine_capacity
    }])

    # Make predictions using the pipeline
    prediction = loaded_model.predict(user_input_df)

    # Determine the emission category
    if prediction[0] > 255:
        emission_type = 'M'
    elif prediction[0]>=1 and prediction[0]<=50:
        emission_type='B'
    elif prediction[0]>50 and prediction[0]<=75:
        emission_type='C'
    elif prediction[0]>75 and prediction[0]<=90:
        emission_type='D'
    elif prediction[0]>90 and prediction[0]<=100:
        emission_type='E' 
    elif prediction[0]>100 and prediction[0]<=110:
        emission_type='F'   
    elif prediction[0]>110 and prediction[0]<=130:
        emission_type='G' 
    elif prediction[0]>130 and prediction[0]<=150:
        emission_type='H'
    elif prediction[0]>150 and prediction[0]<=170:
        emission_type='I'   
    elif prediction[0]>170 and prediction[0]<=190:
        emission_type='J'  
    elif prediction[0]>190 and prediction[0]<=225:
        emission_type='K'
    elif prediction[0]>225 and prediction[0]<=255:
        emission_type='L'                 

    # Display prediction result
    st.markdown("## Prediction Result")
    st.success(f"Emitted CO2 is: {prediction[0]:.2f}")
    st.info(f"Vehicle is rated as: {emission_type}")

st.image('effect.jpeg', width=450)
