import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"


const ScreenData: React.FC<ComponentProps>  = (props) => {

  const { args } = props

  const setTime:any = args['setTime'] || 1000

  const [windowWidth, setWindowWidth] = useState({
    screen: {
      height:window.screen.height,
      width: window.screen.width,
      availHeight: window.screen.availHeight,
      availwidth: window.screen.availWidth,
      colorDepth: window.screen.colorDepth,
      pixelDepth: window.screen.pixelDepth,
      screenOrientation: {
        angle:window.screen.orientation.angle,
        type: window.screen.orientation.type
      } 
    },    
    innerWidth: window.innerWidth, 
    innerHeight: window.innerHeight
  
  })

  function debounce(func:any, time=setTime){
    var timer:any;
    return function(event:any){
        if(timer) clearTimeout(timer);
        timer = setTimeout(func, time, event);
    };
  }

  const delayedScreenWidth = debounce(function detectSize () {
    setWindowWidth({
      screen: {
        height:window.screen.height,
        width: window.screen.width,
        availHeight: window.screen.availHeight,
        availwidth: window.screen.availWidth,
        colorDepth: window.screen.colorDepth,
        pixelDepth: window.screen.pixelDepth,
        screenOrientation: {
          angle:window.screen.orientation.angle,
          type: window.screen.orientation.type
        } 
      },
      innerWidth: window.innerWidth, 
      innerHeight: window.innerHeight
    })

  })
  
    useEffect(() => {

      Streamlit.setComponentValue(windowWidth)
      Streamlit.setComponentReady()

      window.addEventListener('resize', delayedScreenWidth)

      return () => {
        window.removeEventListener('resize', delayedScreenWidth)
      }
    }, [windowWidth])
  return (
    <div style={{display:"none"}}></div>
  )
}



export default withStreamlitConnection(ScreenData)
