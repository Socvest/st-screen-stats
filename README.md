# streamlit-screen-stats

Streamlit component that allows you to do get various stats for your screeen to build repsonsive apps for your users with different devices. 

## Installation instructions

```sh
pip install streamlit-screen-stats
```

## Usage instructions

```python
import streamlit as st

from st_screen_stats import st_screen_data

value = st_screen_data(
    setTime=1000 # this dictates pause until data is received. Done to prevent constant refreshing of app. Default is 1000 (1sec)
)

st.write(value)
```
