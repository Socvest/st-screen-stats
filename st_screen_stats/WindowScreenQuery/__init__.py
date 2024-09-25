import uuid
import os
import time 
import streamlit as st
from typing import Literal, Optional, Union
import streamlit.components.v1 as components 
from st_screen_stats import IS_RELEASE

if not IS_RELEASE:
    _st_window_query_size = components.declare_component(
        "st_screen_data",
        url="http://localhost:3001" 
    )
else:
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_window_query_size = components.declare_component("st_window_query_size", path=build_dir)

class WindowQuerySize:
    """
    Query screen using window.parent.matchMedia() which works similarly to css' `@media () {}` query.

    ### Methods:
        - mediaQuery()
    """

    def __init__(self) -> None:
        pass

    def mediaQuery(self, mediaMatchQ:str=None, on_change=None, default={"status":None}, key=None):
        """
        
        ### Arguments
        - mediaMatchQ: string query. 
            Example: "(max-width: 700px)" which will return boolean result `{status:True}` if the window size is lower or `{status:False}` if window size is greater.
        - key: An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key.
        - on_change: callback to get stats only when screen size changes

        ### Results
        - Boolean result after query screen size of the parent window screen (streamlit app). 

        """

        if mediaMatchQ == None or type(mediaMatchQ) != str:
            return
        
        value = _st_window_query_size(mediaMatchQ=mediaMatchQ, on_change=on_change, key=key, default=default)
        while value is None or st.session_state[key] is None:
            time.sleep(0.1)        

        return value


class WindowQueryHelper:

    """
        Simplifies creating a query for the parent window screen (streamlit app)
        Params on init:
        - pause [int]: time to first pause the component to give it time to mount/load. Will only be implemented once when the app first loads. (uses st.session_state - parameter named per method)
        
        ### Methods:
            - minimum_window_size()
            - maximum_window_size()
            - window_range_width() 

    """

    def __init__(self) -> None:
        pass

    def minimum_window_size(self, min_width:int=None, key="min_width_window", on_change=None, default=None):

        """
            ### Arguments
            - min_width: the lowest width of the screen. For example 1000 means that when the screen width is >= 1000 the component will return {status:true}. If not it will return {status:false}
            - key: An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key.
            - on_change: callback to get stats only when screen size changes

            ### Returns
            Returns a boolean (True) if the width of the parent window screen (streamlit app) is greater than `min_width` parameter. False if its lower.
        """
        if min_width == None or type(min_width) != int:
            return
        
        query_result = f"(min-width: {min_width}px)"

        value = _st_window_query_size(mediaMatchQ=query_result, on_change=on_change, key=key, default=default)
        
        while value is None or st.session_state[key] is None:
            time.sleep(0.1)

        
        return value
    
    def maximum_window_size(self, max_width:int=None, key="max_width_window", on_change=None, default=None):

        """
            ### Arguments
            - max_width: the lowest width of the screen. For example 1000 means that when the screen width is <= 1000 the component will return {status:true}. If not it will return {status:false}
            - key: An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key.
            - on_change: callback to get stats only when screen size changes

            ### Returns
            Returns a boolean (True) if the width of the parent window screen (streamlit app) is lower than `max_width` parameter. False if its greater.
        """
        if max_width == None or type(max_width) != int:
            return
        
        query_result = f"(max-width: {max_width}px)"

        value = _st_window_query_size(mediaMatchQ=query_result, on_change=on_change, key=key, default=default)
        while value is None or st.session_state[key] is None:
            time.sleep(0.1)        
        
        return value
    
    def window_range_width(self, min_width:int=None, max_width:int=None, default=None, on_change=None, key="window_min_max_range"):
        
        """
            ### Arguments
            - min_width: the lowest width of the screen. 
            - max_width: the lowest width of the screen. 
            - key: An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key.
            - on_change: callback to get stats only when screen size changes 

            ### Returns
            Returns boolean (True) if width of parent window screen (streamlit app) is within the range of `min_width` and `max_width` specified. If not, it returns False.
        """

        if min_width == None or max_width == None or type(min_width) != int or type(max_width) != int:
            return
        
        query_result = f'(min-width: {min_width}px) and (max-width: {max_width}px)'

        value = _st_window_query_size(mediaMatchQ=query_result, on_change=on_change, key=key, default=default)
        while value is None or st.session_state[key] is None:
            time.sleep(0.1)

        return value
    
    