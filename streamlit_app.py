import requests
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import time

def apiendpoint(option) :
    if option == 'CMS':
        return 'cms_version'
    elif option == 'PHP':
        return 'php_version'
    elif option == 'Database':
        return 'db_version'

def loadData(api) :
    response = requests.get("https://developer.joomla.org/stats/" + api)
    st.write(response)

    json = response.json() # This method is convenient when the API returns JSON
    st.write(json)
    # st.json(json['data']['cms_version'])

    # versions = json['data']['cms_version']
    return json['data'][api]

st.title("Joomla Streamlit App")

with st.sidebar:
    ## with st.echo():
    ##    st.write("Settings.")
    st.write("Settings.")
    option = st.selectbox(
    'What data ?',
    ('CMS', 'PHP', 'Database'))

    st.write('You selected:', option)
    perc = st.slider('Filter on %', 0, 100, 5)
    st.write("selected ", perc, '%')
    #with st.spinner("Loading..."):
    #    time.sleep(5)
    #st.success("Done!")

api = apiendpoint(option)
version = loadData(api)

columnVersion = []
valueVersion  = []

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