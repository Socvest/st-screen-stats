# streamlit-screen-stats

Streamlit component that allows you to do get various stats for your screeen to build repsonsive apps for your users with different devices.

## Installation instructions

```sh
pip install streamlit-screen-stats
```

## Usage instructions

```python
import streamlit as st
from st_screen_stats import ScreenData, StreamlitNativeWidgetScreen, WindowQuerySize, WindowQueryHelper

# using react component
screenD = ScreenData(setTimeout=1000)
screen_d = screenD.st_screen_data()
st.write(screen_d)

## You can now use the on_change parameter on all class methods of this package. 
def onScreenSizeChange(variable):
    ## do something when the screen size has changed.
    #example
    print(variable)
    
screen_stats_result = screenD.st_screen_data(key="screen_stats_", on_change=onScreenSizeChange("this works")) 
st.write(st.session_state["screen_stats_"]) 

# using sctreamlit native widget and some custom components
# Requirements:
#  Need to install from pypi:
#    - streamlit-browser-session-storage (pip install streamlit-browser-session-storage)
#    - streamlit-local-storage (pip install streamlit-local-storage)
screenDN = StreamlitNativeWidgetScreen(setTimeout=1000) 
screen_stats_window = screenDN.get_window_screen_stats()
st.write(screen_stats_window)

# Query window screen like you would when using CSS @media () {}
# Returns dictionary result `{'status':True}` if conditions are met else `{'status':False}` if conditions are not met.
window_width_query_raw = WindowQuerySize()
window_width_res = window_width_query_raw.mediaQuery(mediaMatchQ="(max-width: 700px)") # returns dictionary result {'status':True} if window screen width is lower than 700px else {'status':False} if window screen width is greater than 700px
st.write(window_width_res)


# Query window screen helper - simplifies the above (CSS @media () {}) method
helper_screen_stats = WindowQueryHelper()
max_width_window = helper_screen_stats.maximum_window_size(max_width=800, key="window_1")
st.write("max_width",max_width_window)
min_width_window = helper_screen_stats.minimum_window_size(min_width=800, key="window_2")
st.write("min_width",min_width_window) 

window_range = helper_screen_stats.window_range_width(min_width=1000, max_width=1100)
st.write("range", window_range) 

## You can now use the on_change parameter. 
# Example:

def onScreenSizeChange(value):
    
    print(value)

large_screen_size_ = helper_screen_stats.window_range_width(min_width=1000, max_width=1100, on_change=onScreenSizeChange(value) key="lg_screen")

if large_screen_size_["status"] or st.session_state["lg_screen"]["status"]:
    st.write("rest of code here")

```
