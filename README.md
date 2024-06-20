# Vehicle CO2 Emission Prediction App

## Overview

The Vehicle CO2 Emission Prediction App is a web application designed to predict the CO2 emissions of vehicles based on user-provided inputs such as transmission type, fuel type, powertrain, engine power, fuel consumption, and engine capacity. The app uses a trained machine learning model to make these predictions and classifies the vehicle's emission rating based on the predicted CO2 emissions.

## Features

- User-friendly interface to input vehicle specifications.
- Predict CO2 emissions based on user inputs.
- Classify the vehicle into an emission category.
- Display the prediction results and emission category.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Joblib
- Scikit-learn
- Seaborn
- Matplotlib
- NumPy


## Input Parameters
Transmission: Select the transmission type from a dropdown list.
Fuel Type: Select the fuel type from a dropdown list.
Powertrain: Select the powertrain type from a dropdown list.
Engine Power (PS): Enter the engine power in PS.
Fuel Consumption Comb (L/100 km): Enter the fuel consumption combined in L/100 km.
Engine Capacity (L): Enter the engine capacity in liters.

### Output
After entering the input parameters and clicking on the "Check Results" button, the app will:

### Predict the CO2 emissions.
Classify the vehicle into an emission category.
Display the predicted CO2 emissions and the emission category.

#### Model Training
### Dataset
The dataset used for training the model consists of vehicle specifications and their corresponding CO2 emissions. The dataset includes the following columns:

Manufacturer
Model
Transmission
Fuel Type
Powertrain
Engine Power (PS)
Fuel Consumption Comb (L/100 km)
CO2 Emissions (G/Km)
Engine Capacity (L)

## Data Preprocessing
Removed spaces and special characters from column names.
Dropped duplicate records.
Handled outliers by removing extreme values.
Encoded categorical features using OneHotEncoder.
Standardized numerical features using StandardScaler.

## Model Training
Several regression models were trained and evaluated, including:

### Random Forest Regressor
Linear Regression
Decision Tree Regressor
Gradient Boosting Regressor
Lasso Regression
Ridge Regression
The Random Forest Regressor was chosen as the final model due to its performance.

### Model Evaluation
The models were evaluated using the following metrics:

Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)

### Files
app.py: The main Streamlit application script.
final_model.joblib: The trained machine learning model.
df.csv: The dataset used for training the model (if applicable).
df_without_outliers.csv: The preprocessed dataset with outliers removed.
effect.jpeg: An image displayed in the app.
