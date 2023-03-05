import requests
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import time


st.title("Joomla Streamlit App")

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

# st.write("Here's our first attempt at using data to create a table:")
"""
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4]})
)
"""
# data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
response = requests.get("https://developer.joomla.org/stats/cms_version")
st.write(response)

json = response.json() # This method is convenient when the API returns JSON
st.write(json)
st.json(json['data']['cms_version'])

versions = json['data']['cms_version']
for version in versions:
    st.write(version)
columnVersion = []
valueVersion = []
for key, val in versions.items():
    # st.write(key)
    columnVersion.append(key)
    # st.write(val)
    valueVersion.append(val)

# st.write(columnVersion)
""" 
chart_data = pd.DataFrame(
    valueVersion
    )
# chart_data.columns=np.array(columnVersion)

st.line_chart(chart_data)


source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

c = alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)

st.altair_chart(c, use_container_width=True)
"""
#-----
joomla = pd.DataFrame({
    'version': columnVersion,
    'perc': valueVersion
})

v = alt.Chart(joomla).mark_bar().encode(
    x='version',
    y='perc',
    color='version:N'
)

st.altair_chart(v, use_container_width=True)