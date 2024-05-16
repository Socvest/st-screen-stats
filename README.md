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

## You can now use the on_change parameter. 
# The component works such that on first mount/app load it sends the value to streamlit. 
# Subsequent app reloads will most likely return None or the value selected for the `default` parameter unless there has been a change in the size of the screen. 
# To make sure you only get a value when there has been a legitimate change in the screen width/size, utilise the on_change parameter to set the results on change of the screen width to a session_state value.
# Example:

def onScreenSizeChange(updated_screen, component_function_):

    st.session_state[updated_screen] = st.session_state[component_function_]

if "screen_stats_result" not in st.session_state:
    st.session_state["screen_stats_result"] = screenD.st_screen_data(key="screen_stats_")
else:
    helper_screen_stats.window_range_width(min_width=1000, max_width=1100, on_change=onScreenSizeChange, args=("screen_stats_result", "screen_stats_post_first_mount_",) key="screen_stats_post_first_mount_")

st.write(st.session_state["screen_stats_result"]) 

# using sctreamlit native widget and some custom components
# Requirements:
#  Need to install from pypi:
#    - streamlit-browser-session-storage (pip install streamlit-browser-session-storage)
#    - streamlit-local-storage (pip install streamlit-local-storage)
screenDN = StreamlitNativeWidgetScreen(setTimeout=1000) 
screen_stats_window = screenDN.get_window_screen_stats()
st.write(screen_stats_window)

# Query window screen like you would when using CSS @media () {}
# Returns dictionary result `{'status':True}` if conditions are met

## Some considerations. Because of how streamlit, there must be a default value sent to the component before the component mounts/loads completely. Even if `default=None` is used, it will send `None` to streamlit before the actual data we desire. This will cause a slight glitch/error when the component is loading. 

# A few solutions:
# 1. You could use a simple time.sleep(1) after you instantiate the class method:
    # example 
    window_width_query_raw = WindowQuerySize()
    window_width_res = window_width_query_raw.mediaQuery(mediaMatchQ="(max-width: 700px)")
    time.sleep(1.5)
# 2. You could send an assumption into the default variable. This will make sure the component at least loads the structure of the end data result and load the app without errors. Though if it loads the default and the component loads the antithesis, it may mean switches in between your if conditions (though it is instant, like a blink).
    # example
    window_width_query_raw = WindowQuerySize()
    window_width_res = window_width_query_raw.mediaQuery(mediaMatchQ="(max-width: 700px)", default={"status":False})
#3. Use the pause parameter built in. This pauses the component for a period of time to give it time to load/mount to load the actual data. Though thereafter, the pause will no longer be needed/implemented as the data will be provided when the screen width changes instantly. 
    # example
    window_width_query_raw = WindowQuerySize(pause=1.5)
    window_width_res = window_width_query_raw.mediaQuery(mediaMatchQ="(max-width: 700px)", default={"status":False})

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
# The component works such that on first mount/app load it sends the value to streamlit. 
# Subsequent app reloads will most likely return None or the value selected for the `default` parameter unless there has been a change in the size of the screen. 
# To make sure you only get a value when there has been a legitimate change in the screen width/size, utilise the on_change parameter to set the results on change of the screen width to a session_state value.
# Example:

def onScreenSizeChange(updated_screen, component_function_):

    st.session_state[updated_screen] = st.session_state[component_function_]

if "large_screen_size_" not in st.session_state:
    st.session_state["large_screen_size_"] = helper_screen_stats.window_range_width(min_width=1000, max_width=1100, key="lg_screen")
else:
    helper_screen_stats.window_range_width(min_width=1000, max_width=1100, on_change=onScreenSizeChange, args=("large_screen_size_", "lg_screen_post_first_mount",) key="lg_screen_post_first_mount")

if st.session_state["large_screen_size_"]["status"]:
    st.write("rest of code here")

```
