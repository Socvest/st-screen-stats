import streamlit as st
from st_screen_stats import ScreenData, StreamlitNativeWidgetScreen


st.subheader("Component with constant args")

screenD = ScreenData()
screen_d = screenD.st_screen_data_window_top()

st.write(screen_d)


st.subheader("native widget method")
screenDN = StreamlitNativeWidgetScreen()
screenDN.st_screen_data_window_top()
stats_ = screenDN.get_window_screen_stats()
st.write(stats_)



