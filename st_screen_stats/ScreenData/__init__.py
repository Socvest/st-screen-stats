import os
import streamlit as st
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
    Two methods:
        1. st_screen_data_window() - get screen stats based on size of window/iframe
        2. st_screen_data_window_top() - get screen stats based on upper most window -> recommended
    
        Args:
            - setTimeout: this dictates period pause until data is received after resize. Default is 1000 (1 second)
    """

    def __init__(self, setTimeout=1000) -> None:
        self.setTimeout = setTimeout
        

    def st_screen_data_window(self, default=None, key=None):
        """
        Component to recieve screen stats to help you build a more responsive app.
        - default: default value for component 
        - key: unique identifier for streamlit (will be recognised by streamlit session state)
        """
        component_value = _st_screen_data(windowType="window", setTime=self.setTimeout, key=key, default=default)

        return component_value
    
    def st_screen_data_window_top(self, default=None, key=None):
        """
        Component to recieve screen stats to help you build a more responsive app.
        - default: default value for component 
        - key: unique identifier for streamlit (will be recognised by streamlit session state)
        """
        component_value = _st_screen_data(windowType="windowTop", setTime=self.setTimeout, key=key, default=default)

        return component_value
