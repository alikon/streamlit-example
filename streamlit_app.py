import requests
import streamlit as st

import numpy as np
import pandas as pd


st.title("Simple Streamlit App")

st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4]})
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
columnVersion = np.array
valueVersion = []
for key, val in versions.items():
    st.write(key)
    columnVersion.append(key)
    st.write(val)
    valueVersion.append(val)

st.write(columnVersion)
 
chart_data = pd.DataFrame(
    valueVersion,
    columns=np.array(columnVersion))

st.line_chart(chart_data)
