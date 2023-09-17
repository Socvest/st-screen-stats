# streamlit-custom-component

Streamlit component that allows you to do X

## Installation instructions

```sh
pip install streamlit-custom-component
```

## Usage instructions

```python
import streamlit as st

from st_screen_stats import st_screen_data

value = st_screen_data(
    setTime=1000 # this dictates pause until data is received. Done to prevent constant refreshing of app. Default is 1000
)

st.write(value)
```