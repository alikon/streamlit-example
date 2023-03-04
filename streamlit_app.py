import requests
import streamlit as st

# data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
response = requests.get("https://developer.joomla.org/stats")
st.write(response)
# raw = response.content() # Return the raw bytes of the data payload
# st.write(raw)
# text = response.text() # Return a string representation of the data payload
# st.write(text)
json = response.json() # This method is convenient when the API returns JSON
st.write(json)
# st.write(data)
