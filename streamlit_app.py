import response
import streamlit as st
import time
import requests

# Streamlit App Title
st.title("Language Detection Tool")


# Text input for user to input a sentence
text_input = st.text_area("Enter a text to detect the language:")


# When the user presses the "Detect Language" button
if st.button("Detect Language", type='primary'):
    if text_input:

        # Send request to FastAPI for prediction
        response = requests.post("http://127.0.0.1:8000/predict/", json={"text": text_input} )

        if response.status_code == 200:
            prediction = response.json()

            with st.spinner('Wait for it...'):
                time.sleep(1)
            st.write(f"Detected Language  :  {prediction}")

    else:
        st.write(f"Error: Unable to get response. Status code: {response.status_code}")

