import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"


const ScreenMatchQuery: React.FC<ComponentProps> = (props) => {

  const { args } = props
  let mediaMatchQ:any = args["mediaMatchQ"]

  const [mediaMatch, setMediaMatch] = useState({status:false})

  useEffect(() => {
    let matchQueryWindow = window.matchMedia(mediaMatchQ);

    const MediaMatchWindow = () => {
      let mediaMatch_ = window.matchMedia(mediaMatchQ).matches;
      mediaMatch.status = mediaMatch_;
      setMediaMatch(mediaMatch);
      Streamlit.setComponentValue(mediaMatch)
      Streamlit.setComponentReady()
    };

    
    
    matchQueryWindow.addEventListener("change", MediaMatchWindow)
    
    return () => {
      matchQueryWindow.removeEventListener("change", MediaMatchWindow)
    }
  }, [mediaMatch])

  return (
    <div style={{display:"none"}}></div>
  )
}



export default withStreamlitConnection(ScreenMatchQuery)