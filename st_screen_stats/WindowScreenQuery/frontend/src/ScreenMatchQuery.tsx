import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"


const ScreenMatchQuery: React.FC<ComponentProps> = (props) => {

  const { args } = props
  let mediaMatchQ: any = args["mediaMatchQ"]

  const [screenWidthChange, setScreenWidthChange] = useState(window.parent.matchMedia(mediaMatchQ).matches)

  const MediaMatchWindow = () => {
    let mediaMatch_2 = window.parent.matchMedia(mediaMatchQ).matches;
    setScreenWidthChange(mediaMatch_2);
  }

  useEffect(() => {

    const mediaQuery = window.parent.matchMedia(mediaMatchQ);
    Streamlit.setComponentValue({ status: screenWidthChange })
    Streamlit.setComponentReady() 

    mediaQuery.addEventListener("change", MediaMatchWindow);

    return () => {
      mediaQuery.removeEventListener("change", MediaMatchWindow);
    };
  }, [screenWidthChange]);

  return (
    <div style={{ display: "none" }}></div>
  )
}



export default withStreamlitConnection(ScreenMatchQuery)