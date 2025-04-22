import streamlit as st
import pandas as pd

def submitUserInfos(table):
    if submitButton and name and schulden:
        st.session_state.infos["Namen"].append(f"{name}")
        st.session_state.infos["Schulden"].append(f"{schulden}")

        return table
    elif submitButton and name:
        st.error("Error: keine schulden eingetragen")
    elif submitButton and schulden:
        st.error("Error: kein name eingetragen")
    elif submitButton:
        st.error("Error: kein name und keine schulden eingetragen")

if "infos" not in st.session_state:
    st.session_state.infos = {"Namen": [], "Schulden": []}

#table init
table = pd.DataFrame(st.session_state.infos)


with st.form(key="my_form"):
    name = st.text_input("Name", placeholder="\"John Doe\"")
    schulden = st.number_input("Schulden $", placeholder="$", step=0.99999, format="%0.2f" )
    submitButton = st.form_submit_button("hinzufügen")
submitUserInfos(table

nameOfUserToDelete = st.selectbox("select", st.session_state.infos["Namen"])
deleteButton = st.button("Delete")

if deleteButton and st.session_state.infos["Namen"]:
    indexOfnameOfUserToDelete = st.session_state.infos["Namen"].index(nameOfUserToDelete)
    st.session_state.infos["Namen"].pop(indexOfnameOfUserToDelete)
    st.session_state.infos["Schulden"].pop(indexOfnameOfUserToDelete)
    st.rerun()
elif deleteButton:
    st.error("Error: can't delete with no entries in the table")

#table last update before deploy
table = pd.DataFrame(st.session_state.infos)
st.write(table)