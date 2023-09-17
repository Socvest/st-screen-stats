import streamlit as st
from __init__ import st_screen_data

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.

num_clicks = st_screen_data()
st.write(num_clicks)


