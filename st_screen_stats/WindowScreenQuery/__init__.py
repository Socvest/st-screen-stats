import os
import time 
import streamlit as st
import streamlit.components.v1 as components
from st_screen_stats import IS_RELEASE


if not IS_RELEASE:
    _st_window_query_size = components.declare_component(

        "st_screen_data",

        url="http://localhost:3001",
    )
else:
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_window_query_size = components.declare_component("st_window_query_size", path=build_dir)


class WindowQuerySize:
    """
    Query screen using window.matchMedia() which works similarly to css' `@media () {}` query.

    Params on init:
        - pause [int]: time to first pause the component to give it time to mount/load. Will only be implemented once when the app first loads. (uses st.session_state - parameter named per method)

    ### Methods:
        - mediaQuery()
        - mediaQueryT()
    """

    def __init__(self, pause:int=1.5) -> None:
        """
            Pause 
        """
        self.pause = pause

        if self.pause != None:
            if "firstRunComponentMediaQuery" not in st.session_state:
                st.session_state["firstRunComponentMediaQuery"] = False
            if "firstRunComponentMediaQueryT" not in st.session_state:
                st.session_state["firstRunComponentMediaQueryT"] = False

    def mediaQuery(self, mediaMatchQ:str=None, default=None, key=None):
        """
        Boolean result after query screen window (browser tab/iframe/lower window).
        Args:
            - mediaMatchQ: string query. 
                Example: "(max-width: 700px)" which will return boolean result `{status:True}` if the window size is lower or `{status:False}` if window size is greater.

        """

        if mediaMatchQ == None or type(mediaMatchQ) != str:
            return

        value = _st_window_query_size(windowType="window", mediaMatchQ=mediaMatchQ, key=key, default=default)
        if "firstRunComponentMediaQuery" in st.session_state and not st.session_state["firstRunComponentMediaQuery"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponentMediaQuery"] = True

        return value

    def mediaQueryT(self, mediaMatchQ:str=None, default=None, key=None):
        """
        Boolean result after query screen size of browser window.
        Args:
            - mediaMatchQ: string query. 
                Example: "(max-width: 700px)" which will return boolean result `{status:True}` if the window size is lower or `{status:False}` if window size is greater.

        """

        if mediaMatchQ == None or type(mediaMatchQ) != str:
            return

        value = _st_window_query_size(windowType="windowTop", mediaMatchQ=mediaMatchQ, key=key, default=default)
        if "firstRunComponentMediaQueryT" in st.session_state and not st.session_state["firstRunComponentMediaQueryT"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponentMediaQueryT"] = True

        return value

class WindowQueryHelper:

    """
        Simplifies creating a query for the top window (main browser window) and window (tab window/iframe and other 'lower' windows)
        Params on init:
        - pause [int]: time to first pause the component to give it time to mount/load. Will only be implemented once when the app first loads. (uses st.session_state - parameter named per method)
        
        ### Methods:
            - minimum_window_size()
            - maximum_window_size()
            - minimum_window_size_top()
            - maximum_window_size_top()
            - window_range_width() 
            - window_top_range_width()

    """

    def __init__(self, pause:int=1.2) -> None:
        self.pause = pause

        if self.pause != None:
            if "firstRunComponent_minimum_window_size" not in st.session_state:
                st.session_state["firstRunComponent_minimum_window_size"] = False
            if "firstRunComponent_maximum_window_size" not in st.session_state:
                st.session_state["firstRunComponent_maximum_window_size"] = False
            if "firstRunComponent_minimum_window_size_top" not in st.session_state:
                st.session_state["firstRunComponent_minimum_window_size_top"] = False
            if "firstRunComponent_maximum_window_size_top" not in st.session_state:
                st.session_state["firstRunComponent_maximum_window_size_top"] = False
            if "firstRunComponent_window_range_width" not in st.session_state:
                st.session_state["firstRunComponent_window_range_width"] = False
            if "firstRunComponent_window_top_range_width" not in st.session_state:
                st.session_state["firstRunComponent_window_top_range_width"] = False

    def minimum_window_size(self, min_width:int=None, key="min_width_window", default=None):

        """
            Returns a boolean (True) if the width of the screen window (browser tab/iframe/lower window) is greater than `min_width` parameter. False if its lower.
        """
        if min_width == None or type(min_width) != int:
            return
        
        query_result = f"(min-width: {min_width}px)"

        value = _st_window_query_size(windowType="window", mediaMatchQ=query_result, key=key, default=default)
        if "firstRunComponent_minimum_window_size" in st.session_state and not st.session_state["firstRunComponent_minimum_window_size"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponent_minimum_window_size"] = True

        return value
    
    def maximum_window_size(self, max_width:int=None, key="max_width_window", default=None):

        """
            Returns a boolean (True) if the width of the screen window (browser tab/iframe/lower window) is lower than `max_width` parameter. False if its greater.
        """
        if max_width == None or type(max_width) != int:
            return
        
        query_result = f"(max-width: {max_width}px)"

        value = _st_window_query_size(windowType="window", mediaMatchQ=query_result, key=key, default=default)
        if "firstRunComponent_maximum_window_size" in st.session_state and not st.session_state["firstRunComponent_maximum_window_size"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponent_maximum_window_size"] = True
        
        return value
    
    def minimum_window_size_top(self, min_width:int=None, key="min_width_window", default=None):

        """
            Returns a boolean (True) if the width of the screen window (browser window) is greater than `min_width` parameter. False if its lower.
        """
        if min_width == None or type(min_width) != int:
            return
        
        query_result = f"(min-width: {min_width}px)"

        value = _st_window_query_size(windowType="windowTop", mediaMatchQ=query_result, key=key, default=default)
        if "firstRunComponent_minimum_window_size_top" in st.session_state and not st.session_state["firstRunComponent_minimum_window_size_top"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponent_minimum_window_size_top"] = True

        return value
    
    def maximum_window_size_top(self, max_width:int=None, key="max_width_window", default=None):

        """
            Returns a boolean (True) if the width of the screen window (browser window) is lower than `max_width` parameter. False if its greater.
        """
        if max_width == None or type(max_width) != int:
            return
        
        query_result = f"(max-width: {max_width}px)"

        value = _st_window_query_size(windowType="windowTop", mediaMatchQ=query_result, key=key, default=default)
        if "firstRunComponent_maximum_window_size_top" in st.session_state and not st.session_state["firstRunComponent_maximum_window_size_top"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponent_maximum_window_size_top"] = True

        return value
    
    def window_range_width(self, min_width:int=None, max_width:int=None, default=None, key="window_min_max_range"):
        
        """
            Returns boolean (True) if width of window (browser tab/iframe/lower window) is within the range of `min_width` and `max_width` specified. If not, it returns False.
        """

        if min_width == None or max_width == None or type(min_width) != int or type(max_width) != int:
            return
        
        query_result = f'(min-width: {min_width}px) and (max-width: {max_width}px)'

        value = _st_window_query_size(windowType="window", mediaMatchQ=query_result, key=key, default=default)
        if "firstRunComponent_window_range_width" in st.session_state and not st.session_state["firstRunComponent_window_range_width"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponent_window_range_width"] = True

        return value
    
    def window_top_range_width(self, min_width:int=None, max_width:int=None, default=None, key="window_min_max_range"):
        
        """
            Returns boolean (True) if width of window (browser window) is within the range of `min_width` and `max_width` specified. If not, it returns False.
        """

        if min_width == None or max_width == None or type(min_width) != int or type(max_width) != int:
            return
        
        query_result = f'(min-width: {min_width}px) and (max-width: {max_width}px)'

        value = _st_window_query_size(windowType="windowTop", mediaMatchQ=query_result, key=key, default=default)
        if "firstRunComponent_window_top_range_width" in st.session_state and not st.session_state["firstRunComponent_window_top_range_width"] and self.pause != None:
            time.sleep(self.pause)
            st.session_state["firstRunComponent_window_top_range_width"] = True

        return value
    
