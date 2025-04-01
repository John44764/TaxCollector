import streamlit as st
import pandas as pd

def submitUserInfos(table):
    if submitButton and name and schulden:
        st.session_state.infos["Name"].append(f"{name}")
        st.session_state.infos["Schulden"].append(f"{schulden}")

        return table
    elif submitButton and name:
        st.error("Error: schulden ist leer")
    elif submitButton and schulden:
        st.error("Error: name ist leer")
    elif submitButton:
        st.error("Error: name und schulden sind leer")

if "infos" not in st.session_state:
    st.session_state.infos = {"Name": [], "Schulden": []}

#table init
table = pd.DataFrame(st.session_state.infos)

with st.form(key="my_form"):
    name = st.text_input("Name")
    schulden = st.text_input("Schulden")
    submitButton = st.form_submit_button("hinzufügen")

submitUserInfos(table)

#table last update before deploy
table = pd.DataFrame(st.session_state.infos)
st.write(table)