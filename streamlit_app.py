import requests
import streamlit as st

# data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
response = requests.get("http://api.open-notify.org/astros.json")
st.write(response)

# st.write(data)
