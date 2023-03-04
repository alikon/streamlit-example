import requests
import streamlit as st

import numpy as np
import pandas as pd


st.title("Simple Streamlit App")

st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
)

# data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
response = requests.get("https://developer.joomla.org/stats/cms_version")
st.write(response)

json = response.json() # This method is convenient when the API returns JSON
st.write(json)
st.json(json['data']['cms_version'])

versions = json['data']['cms_version']
for version in versions:
    st.write(version)
    st.write(version.value)
