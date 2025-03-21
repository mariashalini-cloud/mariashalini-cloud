import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("flight_price_model.joblib")

# Title of the app
st.title("Flight Price Prediction")

# Dropdowns for categorical features
airlines = ["IndiGo", "Air India", "SpiceJet", "Vistara"]
sources = ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai"]
destinations = ["Mumbai", "Kolkata", "Delhi", "Chennai", "Bangalore"]

airline = st.selectbox("Select Airline", airlines)
source = st.selectbox("Select Source", sources)
destination = st.selectbox("Select Destination", destinations)

# Numeric inputs
departure_time = st.text_input("Enter Departure Time (HH:MM)", "10:00")
arrival_time = st.text_input("Enter Arrival Time (HH:MM)", "12:30")
duration = st.number_input("Duration (in hours)", min_value=1.0, max_value=24.0, value=2.5)
stops = st.slider("Number of Stops", 0, 3)

# Predict button
if st.button("Predict Price"):
    # Encode user inputs
    airline_encoded = airlines.index(airline)
    source_encoded = sources.index(source)
    destination_encoded = destinations.index(destination)
    departure_hour, departure_minute = map(int, departure_time.split(":"))
    arrival_hour, arrival_minute = map(int, arrival_time.split(":"))

    # Prepare input for prediction
    input_data = np.array([[
        airline_encoded, source_encoded, destination_encoded, 
        departure_hour, departure_minute, arrival_hour, arrival_minute, 
        duration, stops
    ]])

    # Predict the price
    price = model.predict(input_data)

    # Display the result
    st.success(f"Estimated Flight Price: ₹{price[0]:,.2f}")
