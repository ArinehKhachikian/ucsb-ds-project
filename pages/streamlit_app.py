import streamlit as st

# Title and subtitle of the webpage
st.title("Santa Barbara Housing Cost Predictor")
st.write(
    "Transparent rent estimates and market insights for UCSB students."
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Rent Predictor"):
        st.switch_page("pages/rent_predictor.py")

with col2:
    if st.button("Market Explorer"):
        st.switch_page("pages/market_explorer.py")
