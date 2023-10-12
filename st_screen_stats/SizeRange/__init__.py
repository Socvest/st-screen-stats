import os
import streamlit as st
import streamlit.components.v1 as components

from st_screen_stats import IS_RELEASE

if not IS_RELEASE:
    _st_screen_ranges = components.declare_component(

        "st_screen_ranges",

        url="http://localhost:3001",
    )
else:
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_screen_ranges = components.declare_component("st_screen_ranges", path=build_dir)


class WindowScreenRange:
    """
    Built to help get updates you care about with regards to the window screen size. 
    Data is only sent if the desired window size chosen is met.
    """

    def __init__(self) -> None:
        pass

    def WidthUpperRange(self, upperRange:int=None, key=None, default=None):
        """
        Send boolean if window width is lower than or equal to selected upper range window width
        Args:
            - upperRange: integer upper range
        """

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_ranges(windowType="windowSingleRange", rangeType="upper", heightWidth="width", upperRange=upperRange, key=key, default=default)

        return value
    
    def WidthLowerRange(self, lowerRange:int=None, key=None, default=None):
        """
        Send boolean if window width is higher than or equal to selected lower range window width
        Args:
            - lowerRange: integer lower range
        """

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_ranges(windowType="windowSingleRange", rangeType="lower", heightWidth="width", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def HeightUpperRange(self, upperRange:int=None, key=None, default=None):
        """
        Send boolean if window height is lower than or equal to selected upper range window height
        Args:
            - upperRange: integer upper range
        """

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_ranges(windowType="windowSingleRange", rangeType="upper", heightWidth="height", upperRange=upperRange, key=key, default=default)

        return value
    
    def HeightLowerRange(self, lowerRange:int=None, key=None, default=None):
        """
        Send boolean if window height is higher than or equal to selected lower window height
        Args:
            - lowerRange: integer lower range
        """

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_ranges(windowType="windowSingleRange", rangeType="lower", heightWidth="height", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def WidthUpperRangeTop(self, upperRange:int=None, key=None, default=None):
        """
        Send boolean if window top (the upper most browser window) width is lower than or equal to selected upper window width
        Args:
            - upperRange: integer upper range
        """

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_ranges(windowType="windowTopSingleRange", rangeType="upper", heightWidth="width", upperRange=upperRange, key=key, default=default)

        return value
    
    def WidthLowerRangeTop(self, lowerRange:int=None, key=None, default=None):
        """
        Send boolean if window top (the upper most browser window) width is higher than or equal to desired lower window width
        Args:
            - lowerRange: integer lower range
        """

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_ranges(windowType="windowTopSingleRange", rangeType="lower", heightWidth="width", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def HeightUpperRangeTop(self, upperRange:int=None, key=None, default=None):
        """
        Send boolean if window top (the upper most browser window) height is lower than or equal to desired upper window height
        Args:
            - upperRange: integer upper range
        """

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_ranges(windowType="windowTopSingleRange", rangeType="upper", heightWidth="height", upperRange=upperRange, key=key, default=default)

        return value
    
    def HeightLowerRangeTop(self, lowerRange:int=None, key=None, default=None):
        """
        Send boolean if window top (the upper most browser window) height is higher than or equal to desired lower window height
        Args:
            - lowerRange: integer lower range
        """

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_ranges(windowType="windowTopSingleRange", rangeType="lower", heightWidth="height", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def WidthRange(self, lowerRange:int=None, upperRange:int=None, key=None, default=None):
        """
        Send boolean if window width is between the desired lower and upper range
        Args:
            - lowerRange: integer lower range
            - upperRange: integer upper range
        """

        if lowerRange == None or type(lowerRange) != int or upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_ranges(windowType="windowUpperLowerJoint", heightWidth="width", lowerRange=lowerRange, upperRange=upperRange, key=key, default=default)

        return value
    
    def HeightRange(self, lowerRange:int=None, upperRange:int=None, key=None, default=None):
        """
        Send boolean if window height is between the desired lower and upper range
        Args:
            - lowerRange: integer lower range
            - upperRange: integer upper range
        """

        if lowerRange == None or type(lowerRange) != int or upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_ranges(windowType="windowUpperLowerJoint", heightWidth="height", lowerRange=lowerRange, upperRange=upperRange, key=key, default=default)

        return value
    
    

