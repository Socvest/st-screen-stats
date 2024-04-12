import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"

const ScreenData: React.FC<ComponentProps> = (props) => {

  const { args } = props

  const setTime: any = args['setTime'] || 1000
  let windowType: any = args["windowType"]

  const [windowTopWidth, setWindowTopWidth] = useState({
    screen: {
      height: window.top?.screen.height,
      width: window.top?.screen.width,
      availHeight: window.top?.screen.availHeight,
      availWidth: window.top?.screen.availWidth,
      colorDepth: window.top?.screen.colorDepth,
      pixelDepth: window.top?.screen.pixelDepth,
      screenOrientation: {
        angle: window.top?.screen.orientation.angle,
        type: window.top?.screen.orientation.type
      }
    },
    innerWidth: window.top?.innerWidth,
    innerHeight: window.top?.innerHeight
  })

  const [windowWidth, setWindowWidth] = useState({
    screen: {
      height: window.screen.height,
      width: window.screen.width,
      availHeight: window.screen.availHeight,
      availWidth: window.screen.availWidth,
      colorDepth: window.screen.colorDepth,
      pixelDepth: window.screen.pixelDepth,
      screenOrientation: {
        angle: window.screen.orientation.angle,
        type: window.screen.orientation.type
      }
    },
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight

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
        height: window.screen.height,
        width: window.screen.width,
        availHeight: window.screen.availHeight,
        availWidth: window.screen.availWidth,
        colorDepth: window.screen.colorDepth,
        pixelDepth: window.screen.pixelDepth,
        screenOrientation: {
          angle: window.screen.orientation.angle,
          type: window.screen.orientation.type
        }
      },
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight
    })

  })

  const delayedScreenWidthTop = debounce(function detectSizeTop() {
    setWindowTopWidth({
      screen: {
        height: window.top?.screen.height,
        width: window.top?.screen.width,
        availHeight: window.top?.screen.availHeight,
        availWidth: window.top?.screen.availWidth,
        colorDepth: window.top?.screen.colorDepth,
        pixelDepth: window.top?.screen.pixelDepth,
        screenOrientation: {
          angle: window.top?.screen.orientation.angle,
          type: window.top?.screen.orientation.type
        }
      },
      innerWidth: window.top?.innerWidth,
      innerHeight: window.top?.innerHeight

    })
  })

  useEffect(() => {

    switch (windowType) {
      case "window":
        Streamlit.setComponentValue(windowWidth)
        Streamlit.setComponentReady()
        break
      default:
        break
    }

    window.addEventListener('resize', delayedScreenWidth)

    return () => {
      window.removeEventListener('resize', delayedScreenWidth)
    }
  }, [windowWidth])

  useEffect(() => {

    switch (windowType) {
      case "windowTop":
        
        Streamlit.setComponentValue(windowTopWidth)
        Streamlit.setComponentReady()
        break
      default:
        break
    }

    window.top?.addEventListener('resize', delayedScreenWidthTop)

    return () => {
      window.top?.removeEventListener('resize', delayedScreenWidthTop)
    }

  }, [windowTopWidth])


  return (
    <div style={{ display: "none" }}></div>
  )
}



export default withStreamlitConnection(ScreenData)