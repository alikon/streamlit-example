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

@st.cache
def loadData(api) :
    response = requests.get("https://developer.joomla.org/stats/" + api)
    return response

st.title("Joomla Streamlit App")

with st.sidebar:
    ## with st.echo():
    ##    st.write("Settings.")
    st.write("Settings.")
    option = st.selectbox(
    'What data ?',
    ('CMS', 'PHP', 'Database'))

    # st.write('You selected:', option)
    # perc = st.slider('Filter on %', 0, 100, 5)
    # st.write("selected ", perc, '%')
    #with st.spinner("Loading..."):
    #    time.sleep(5)
    #st.success("Done!")
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
    st.write("Set label visibility 👇")
    st.radio(
        "",
        ["visible", "hidden"],
        key="visibility",
        label_visibility=st.session_state.visibility,
    )

api = apiendpoint(option)
data = loadData(api)

json = data.json() # This method is convenient when the API returns JSON

versions = json['data'][api]
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

if st.session_state.visibility == "visible" :
    st.write(data)
    st.write(json)
    # st.json(json['data']['cms_version'])
    # versions = json['data']['cms_version']