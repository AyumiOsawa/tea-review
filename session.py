import streamlit as st

from db import load_data


def session_update(new_session_dict):
    st.session_state.update(new_session_dict)


def session_init():
    init_settings = {
        "submitted": False,
        "df": load_data(n=30)
    }
    session_update(init_settings)