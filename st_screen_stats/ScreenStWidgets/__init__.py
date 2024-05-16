import os
import streamlit as st
import streamlit.components.v1 as components


class StreamlitNativeWidgetScreen:

    """
    Component that uses streamlit's component.html method to derive various window screen stats. This may provide better performance than the other class.
    Methods:
        st_screen_data_window() - get screen stats based on size of streamlit app
        
    
        Args:
            - setTimeout: this dictates period pause until data is received after resize. Default is 1000[ms] (1 second)
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
    
    def st_screen_data_window(self):
        """
        Using javascript to get and store the window parent screen (streamlit app) data to session or local storage
        """

        js_el = f'''

                    <script>
                        function delay(time) {{
                            return new Promise(resolve => setTimeout(resolve, time));
                            }}

                        function storeScreenStats (e) {{
                        
                            const screenData = {{"screenStats":{{"screen": {{
                                    "height":window.parent.height,
                                    "width":window.parent.width,
                                    "availHeight":window.parent.availHeight,
                                    "availWidth":window.parent.availWidth,
                                    "colorDepth": window.parent.colorDepth,
                                    "pixelDepth": window.parent.pixelDepth,
                                    "screenOrientation": {{
                                            "angle":window.parent.orientation.angle,
                                            "type":window.parent.orientation.type
                                        }},
                                    }},
                                    "innerWidth":window.parent.innerWidth,
                                    "innerHeight":window.parent.innerHeight  
                                }}
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
        Using local storage or session storage libraries to get the screen data from browser storage into streamlit frontend
        """
        if self.setTimeout != None:
            pause = (self.setTimeout/1000)+1
        else: 
            pause = None

        if self.localSessionStorage == "sessionStorage":
            sessionS = self.SessionStorage(key=key, pause=pause)
            current_stats_ = sessionS.getItem("screenStats", key=key)
        else:
            localS = self.LocalStorage(key=key, pause=pause) 
            current_stats_ = localS.getItem(itemKey="screenStats")

        return current_stats_



