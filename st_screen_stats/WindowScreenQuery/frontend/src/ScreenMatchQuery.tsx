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
  let windowType: any = args["windowType"]

  useEffect(() => {

    switch (windowType) {
      case "window":
        let mediaMatch_ = window.matchMedia(mediaMatchQ).matches;

        Streamlit.setComponentValue({ status: mediaMatch_ })
        Streamlit.setComponentReady()
        break
      case "windowTop":
        let mediaMatch_2 = window.top?.matchMedia(mediaMatchQ).matches

        Streamlit.setComponentValue({ status: mediaMatch_2 })
        Streamlit.setComponentReady()
        break
      default:
        break
    }


  }, [])

  useEffect(() => {

    let matchQueryWindow = window.matchMedia(mediaMatchQ);

    const MediaMatchWindow = () => {
      switch (windowType) {
        case "window":
          let mediaMatch_1 = window.matchMedia(mediaMatchQ).matches;
          Streamlit.setComponentValue({ status: mediaMatch_1 })
          Streamlit.setComponentReady()
          break;
        default:
          break;
      }
    };
    matchQueryWindow.addEventListener("change", MediaMatchWindow);

    return () => {
      matchQueryWindow.removeEventListener("change", MediaMatchWindow);
    };
  }, []);


  useEffect(() => {
    let matchQueryWindow = window.top?.matchMedia(mediaMatchQ)

    const MediaMatchWindow = () => {
      switch (windowType) {
        case "windowTop":
          let mediaMatch_2 = window.top?.matchMedia(mediaMatchQ).matches
          Streamlit.setComponentValue({ status: mediaMatch_2 })
          Streamlit.setComponentReady()
          break;
        default:
          break;
      }
    };


    matchQueryWindow?.addEventListener("change", MediaMatchWindow);

    return () => {
      matchQueryWindow?.removeEventListener("change", MediaMatchWindow);
    };
  }, []);


  return (
    <div style={{ display: "none" }}></div>
  )
}



export default withStreamlitConnection(ScreenMatchQuery)