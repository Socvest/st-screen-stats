import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"

const ScreenData: React.FC<ComponentProps> = (props: any) => {

  const { args } = props

  const setTime: any = args['setTime'] || 1000

  const [windowWidth, setWindowWidth] = useState({
    screen: {
      height: window.parent.screen.height,
      width: window.parent.screen.width,
      availHeight: window.parent.screen.availHeight,
      availWidth: window.parent.screen.availWidth,
      colorDepth: window.parent.screen.colorDepth,
      pixelDepth: window.parent.screen.pixelDepth,
      screenOrientation: {
        angle: window.parent.screen.orientation.angle,
        type: window.parent.screen.orientation.type
      }
    },
    innerWidth: window.parent.innerWidth,
    innerHeight: window.parent.innerHeight

  })

  function debounce(func: any, time = setTime) {
    var timer: any;
    return function (event: any) {
      if (timer) clearTimeout(timer);
      timer = setTimeout(func, time, event);
    };
  }

  const delayedScreenWidth = debounce(function detectSize() {

    setWindowWidth({
      screen: {
        height: window.parent.screen.height,
        width: window.parent.screen.width,
        availHeight: window.parent.screen.availHeight,
        availWidth: window.parent.screen.availWidth,
        colorDepth: window.parent.screen.colorDepth,
        pixelDepth: window.parent.screen.pixelDepth,
        screenOrientation: {
          angle: window.parent.screen.orientation.angle,
          type: window.parent.screen.orientation.type
        }
      },
      innerWidth: window.parent.innerWidth,
      innerHeight: window.parent.innerHeight
    })

  })

  useEffect(() => {

    Streamlit.setComponentValue(windowWidth)
    Streamlit.setComponentReady()

    window.parent.addEventListener('resize', delayedScreenWidth)

    return () => {
      window.parent.removeEventListener('resize', delayedScreenWidth)
    }
  }, [windowWidth])


  return (
    <div style={{ display: "none" }}></div>
  )
}



export default withStreamlitConnection(ScreenData)