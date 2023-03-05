import requests
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import time


st.title("Joomla Streamlit App")

with st.sidebar:
    ## with st.echo():
    ##    st.write("Settings.")
    st.write("Settings.")
    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
    perc = st.slider('How old are you?', 0, 100, 5)
    st.write("selected ", perc, 'years old')

response = requests.get("https://developer.joomla.org/stats/cms_version")
st.write(response)

json = response.json() # This method is convenient when the API returns JSON
st.write(json)
# st.json(json['data']['cms_version'])

versions = json['data']['cms_version']
"""
for version in versions:
    st.write(version)
"""
columnVersion = []
valueVersion = []
for key, val in versions.items():
    # st.write(key)
    columnVersion.append(key)
    # st.write(val)
    valueVersion.append(val)

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