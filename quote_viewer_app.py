import requests
import streamlit as st

st.title("Quote App")
clicked=st.button("Get Quote")

if clicked:
    response=requests.get("https://zenquotes.io/api/random")
    data=response.json()
    quote=data[0]["q"]
    author=data[0]["a"]
    st.write(quote)
    st.write(author)