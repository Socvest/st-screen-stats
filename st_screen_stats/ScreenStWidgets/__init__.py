import os
import streamlit as st
import streamlit.components.v1 as components


class StreamlitNativeWidgetScreen:

    """
    Component that uses streamlit's component.html method to derive various window screen stats. This may provide better performance than the other class.
    Two methods:
        1. st_screen_data_window() - get screen stats based on size of window/iframe. 
        2. st_screen_data_window_top() - get screen stats based on upper most window -> recommended
    
        Args:
            - setTimeout: this dictates period pause until data is received after resize. Default is 1000 (1 second)
            - localSessionStorage: where to store the screen data. 0 -> local storage, 1 -> session storage

        Requirements:
            Need to install from pypi:
            - streamlit-browser-session-storage (pip install streamlit-browser-session-storage)
            - streamlit-local-storage (pip install streamlit-local-storage)
    """

    from streamlit_local_storage import LocalStorage
    from streamlit_session_browser_storage import SessionStorage

    def __init__(self, setTimeout=1000, localSessionStorage=0) -> None:
        self.setTimeout = setTimeout
        self.localSessionStorage = ["localStorage", "sessionStorage"][localSessionStorage]
    
    def st_screen_data_window_top(self):
        """
        Using javascript to get and store the upper most window screen data to session or local storage
        """

        js_el = f'''

                    <script>
                        function delay(time) {{
                            return new Promise(resolve => setTimeout(resolve, time));
                            }}

                        function storeScreenStats (e) {{
                        
                            const screenData = {{"screen": {{
                                    "height":window.top.screen.height,
                                    "width":window.top.screen.width,
                                    "availHeight":window.top.screen.availHeight,
                                    "availWidth":window.top.screen.availWidth,
                                    "colorDepth": window.top.screen.colorDepth,
                                    "pixelDepth": window.top.screen.pixelDepth,
                                    "screenOrientation": {{
                                            "angle":window.top.screen.orientation.angle,
                                            "type":window.top.screen.orientation.type
                                        }},
                                    
                                    }},
                                    "innerWidth":window.top.innerWidth,
                                    "innerHeight":window.top.innerHeight                                    
                                                            
                                }}

                            {self.localSessionStorage}.setItem("screenStats", JSON.stringify(screenData)); 

                            }};
                        
                        let storageItem = JSON.parse({self.localSessionStorage}.getItem("screenStats"))

                        if ( storageItem === null || storageItem["screenStats"] === null ){{
                                storeScreenStats()
                            }} 
                        delay({self.setTimeout}).then(() => window.top.addEventListener("resize", storeScreenStats))
                    </script>

                '''
        st.components.v1.html(js_el, width=0, height=0) 
    
    def st_screen_data_window(self):
        """
        Using javascript to get and store the current window (bound by iframe fyi) data to session or local storage
        """

        js_el = f'''

                    <script>
                        function delay(time) {{
                            return new Promise(resolve => setTimeout(resolve, time));
                            }}

                        function storeScreenStats (e) {{
                        
                            const screenData = {{"screen": {{
                                    "height":window.screen.height,
                                    "width":window.screen.width,
                                    "availHeight":window.screen.availHeight,
                                    "availWidth":window.screen.availWidth,
                                    "colorDepth": window.screen.colorDepth,
                                    "pixelDepth": window.screen.pixelDepth,
                                    "screenOrientation": {{
                                            "angle":window.screen.orientation.angle,
                                            "type":window.screen.orientation.type
                                        }},
                                    }},
                                    "innerWidth":window.top.innerWidth,
                                    "innerHeight":window.top.innerHeight  
                                }}

                            {self.localSessionStorage}.setItem("screenStats", JSON.stringify(screenData)); 
                                
                            }};

                        let storageItem = JSON.parse({self.localSessionStorage}.getItem("screenStats"));
                        if ( storageItem === null || storageItem["screenStats"] === null ){{
                                storeScreenStats()
                            }} 
                        
                        delay({self.setTimeout}).then(() => window.addEventListener("resize", storeScreenStats))
                       

                    </script>

                '''
        st.components.v1.html(js_el) 

    def get_window_screen_stats(self, key="get_item"):
        """
        Using local storage or session storage libraries to get the screen data into streamlit
        """

        if self.localSessionStorage == "sessionStorage":
            sessionS = self.SessionStorage()
            current_stats_ = sessionS.getItem("screenStats", key=key)
        else:
            localS = self.LocalStorage()
            current_stats_ = localS.getItem("screenStats", key=key)

        return current_stats_



