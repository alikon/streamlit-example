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

@st.cache(suppress_st_warning=True)
def loadData(api, days = 1) :
    try:
        response = requests.get("https://developer.joomla.org/stats/" + api + "?timeframe=" + days)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        st.write(errh)
    except requests.exceptions.ConnectionError as errc:
        st.write(errc)
    except requests.exceptions.Timeout as errt:
        st.write(errt)
    except requests.exceptions.RequestException as err:
        st.write(err)
    finally:
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
    days = st.slider('Filter on days', 1, 1000, 5)
    # st.write("selected ", perc, '%')
    #with st.spinner("Loading..."):
    #    time.sleep(5)
    #st.success("Done!")
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
    #st.write("Set label visibility 👇")
    showRaw = st.radio(
        "Set raw data visibility 👇",
        ["visible", "hidden"],
    )
st.write('days' + days)
api = apiendpoint(option)
data = loadData(api, days)
if (data.status_code != 200):
    st.warning('Unable to load data.')
    st.stop()

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

# if st.session_state.visibility == "visible" :
if showRaw == "visible" :
    st.write(data)
    st.write(json)
    # st.json(json['data']['cms_version'])
    # versions = json['data']['cms_version']