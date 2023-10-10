# streamlit-screen-stats

Streamlit component that allows you to do get various stats for your screeen to build repsonsive apps for your users with different devices.

## Installation instructions

```sh
pip install streamlit-screen-stats
```

## Usage instructions

```python
import streamlit as st
from st_screen_stats import ScreenData, StreamlitNativeWidgetScreen

# using react component
screenD = ScreenData(setTimeout=1000)
screen_d = screenD.st_screen_data_window_top()
st.write(screen_d)

# using sctreamlit native widget and some custom components
# Requirements:
#             Need to install from pypi:
#             - streamlit-browser-session-storage (pip install streamlit-browser-session-storage)
#             - streamlit-local-storage (pip install streamlit-local-storage)
screenDN = StreamlitNativeWidgetScreen(setTimeout=1000)
screenDN.st_screen_data_window_top()
stats_ = screenDN.get_window_screen_stats()
st.write(stats_)

# decided to build alternatives in case one is less reliable than the other. 

```
