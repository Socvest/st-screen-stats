import os
import time
import streamlit as st
from typing import Literal, Optional, Union
import streamlit.components.v1 as components
from st_screen_stats import IS_RELEASE


if not IS_RELEASE:
    _st_screen_data = components.declare_component(

        "st_screen_data",

        url="http://localhost:3001",
    )
else:
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_screen_data = components.declare_component("st_screen_data", path=build_dir)


class ScreenData:
    """
    Component that uses react to derive various window screen stats.
    Methods:
        st_screen_data_window() - get screen stats based on size of parent window (streamlit app)

    """

    def __init__(self, setTimeout:Union[int,float]=1000, useNativePause:bool=True) -> None:
        """
            - setTimeout: amount of time for component to wait before sending traffic/data in ms default is 1000ms (1 sec).
        """
        self.setTimeout = setTimeout         
        
    def st_screen_data(self, on_change=None, default=None, key=None): 
        """
        Component to recieve screen stats to help you build a more responsive app.

        ### Arguments
        - default: default value for component 
        - key: unique identifier for streamlit (will be recognised by streamlit session state)
        - on_change: callback to get stats only when screen size changes 

        ### Returns
        A dictionary of important screen stats:
            {
                screen: {
                    height: value,
                    width: value,
                    availHeight: value,
                    availWidth: value,
                    colorDepth: value,
                    pixelDepth: value,
                    screenOrientation: {
                        angle: value,
                        type: value
                    }
                },
                innerWidth: value,
                innerHeight: value
            }

        """

        component_value = _st_screen_data(setTime=self.setTimeout, key=key, on_change=on_change, default=default) 
        while component_value is None or st.session_state[key] is None:
            time.sleep(0.1)        
        
        return component_value
        
    