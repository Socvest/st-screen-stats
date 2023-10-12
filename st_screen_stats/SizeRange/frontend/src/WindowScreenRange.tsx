import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { ReactNode, useState, useEffect } from "react"


const WindowScreenRange: React.FC<ComponentProps> = (props) => {

  const { args } = props

  const upperRange:any = args["upperRange"]
  const lowerRange:any = args["lowerRange"]
  let rangeType:any = args["rangeType"]
  let heightWidth:any = args["heightWidth"]
  let windowType:any = args['windowType']
  

  const [innerWidthS, setInnerWidthS] = useState(false)
  const [innerHeightS, setInnerHeightS] = useState(false)
  const [jointInnerWidth, setJointInnerWidth] = useState(false)
  const [jointInnerHeight, setJointInnerHeight] = useState(false)

  const [innerWidthSTop, setInnerWidthSTop] = useState(false)
  const [innerHeightSTop, setInnerHeightSTop] = useState(false)
  const [jointInnerWidthTop, setJointInnerWidthTop] = useState(false)
  const [jointInnerHeightTop, setJointInnerHeightTop] = useState(false)



  const WidthHeightRange = () => {
    if (heightWidth === "width"){
      if (rangeType === "upper"){
        if (window.innerWidth <= upperRange ) {
          setInnerWidthS(true)
        } else {
          setInnerWidthS(false)
        }
      } else if (rangeType === "lower") {
        if (window.innerWidth >= lowerRange ) {
          setInnerWidthS(true)
        } else {
          setInnerWidthS(false)
        }
      }
  
    } else if (heightWidth === "height"){
      if ( rangeType === "upper"){
        if (window.innerHeight <= upperRange ) {
          setInnerHeightS(true)
        } else {
          setInnerHeightS(false)
        }
      } else if ( rangeType === "lower" ){
        if (window.innerHeight >= lowerRange ) {
          setInnerHeightS(true)
        } else {
          setInnerHeightS(false)
        }
      }
      
    }
  }

  const WidthHeightJointRange = () => {
    if (heightWidth === "width"){
      if ( window.innerWidth >= lowerRange && window.innerWidth <= upperRange ) {
        setJointInnerWidth(true)
      } else {
        setJointInnerWidth(false)
      }
  
    } else if (heightWidth === "height"){
      if ( window.innerHeight >= lowerRange && window.innerHeight <= upperRange ) {
        setJointInnerHeight(true)
      } else {
        setJointInnerHeight(false)
      }
    }
}

  const WidthHeightRangeTop = () => {
    if (heightWidth === "width"){
      if (rangeType === "lower"){
        if (window.innerWidth <= upperRange ) {
          setInnerWidthSTop(true)
        } else {
          setInnerWidthSTop(false)
        }
      } else if (rangeType === "upper"){
        if (window.innerWidth >= lowerRange ) {
          setInnerWidthSTop(true)
        } else {
          setInnerWidthSTop(false)
        }
      }
        
      
        
    } else if (heightWidth === "height"){
      if (rangeType === "upper"){
        if (window.innerHeight <= upperRange ) {
          setInnerHeightSTop(true)
        } else {
          setInnerHeightSTop(false)
        }
      } else if (rangeType === "lower"){
        if (window.innerHeight >= lowerRange ) {
          setInnerHeightSTop(true)
        } else {
          setInnerHeightSTop(false)
        }
      }
      
    }
  }

  const WidthHeightJointRangeTop = () => {
    if (window.top){
      if (heightWidth === "width"){
      
        if ( window.top.innerWidth >= lowerRange && window.top.innerWidth <= upperRange ) {
          setJointInnerWidthTop(true)
        } else {
          setJointInnerWidthTop(false)
        }
      } else if (heightWidth === "height"){
          if ( window.top.innerHeight >= lowerRange && window.top.innerHeight <= upperRange ) {
            setJointInnerHeightTop(true)
          } else {
            setJointInnerHeightTop(false)
          }
        }
      
      } 
  }

 

  useEffect(() => {
    switch (windowType) {

      case "windowSingleRange":
        switch(heightWidth){
          case "width":
            switch(rangeType){
              case "upper":
                Streamlit.setComponentValue(innerWidthS)
                Streamlit.setComponentReady()
                break
              case "lower":
                Streamlit.setComponentValue(innerWidthS)
                Streamlit.setComponentReady()
                break
              default:
                break
            }
            break
          case "height":
            switch (rangeType){
              case "upper":
                Streamlit.setComponentValue(innerHeightS)
                Streamlit.setComponentReady()
                break
              case "lower":
                Streamlit.setComponentValue(innerHeightS)
                Streamlit.setComponentReady()
                break
              default:
                break
            }
            break
          default:
            break
        }
        break
      default:
        break
    }
      
    window.addEventListener('resize', WidthHeightRange)

    return () => {
      window.removeEventListener('resize', WidthHeightRange)
    }
    
  }, [innerWidthS, innerHeightS, rangeType, heightWidth])

  useEffect(() => {

    switch (windowType) {
      case "windowUpperLowerJoint":
          switch(heightWidth){

            case "width":
              Streamlit.setComponentValue(jointInnerWidth)
              Streamlit.setComponentReady()
              break
            case "height":
              Streamlit.setComponentValue(jointInnerHeight)
              Streamlit.setComponentReady()
              break
            default:
              break
          }
          break
        default:
          break
      }

      window.addEventListener('resize', WidthHeightJointRange)

      return () => {
        window.removeEventListener('resize', WidthHeightJointRange)
      }
  }, [jointInnerWidth, jointInnerHeight, heightWidth])


  useEffect(() => {
    switch (windowType) {

      case "windowTopSingleRange":
        switch(heightWidth){
          case "width":
            switch(rangeType){
              case "upper":
                Streamlit.setComponentValue(innerWidthS)
                Streamlit.setComponentReady()
                break
              case "lower":
                Streamlit.setComponentValue(innerWidthS)
                Streamlit.setComponentReady()
                break
              default:
                break
            }    
            break     
          case "height":
            switch(rangeType){
              case "upper":
                Streamlit.setComponentValue(innerHeightS)
                Streamlit.setComponentReady()
                break
              case "lower":
                Streamlit.setComponentValue(innerHeightS)
                Streamlit.setComponentReady()
                break
              default:
                break
            }
            break
          default:
            break
        }
        break
      default:
        break
    }
      
    window.addEventListener('resize', WidthHeightRangeTop)

    return () => {
      window.removeEventListener('resize', WidthHeightRangeTop)
    }
    
  }, [innerWidthSTop, innerHeightSTop, rangeType, heightWidth])

  useEffect(() => {

    switch (windowType) {
    case "windowTopUpperLowerJoint":
        switch(heightWidth){

          case "width":
            Streamlit.setComponentValue(jointInnerWidth)
            Streamlit.setComponentReady()
          break
          case "height":
            Streamlit.setComponentValue(jointInnerHeight)
            Streamlit.setComponentReady()
          break
          default:
            break
        }
        break
      default:
        break
      }

      window.addEventListener('resize', WidthHeightJointRangeTop)

      return () => {
        window.removeEventListener('resize', WidthHeightJointRangeTop)
      }
  }, [jointInnerWidthTop, jointInnerHeightTop])

 
  return (
    <div style={{display:"none"}}></div>
  )
}



export default withStreamlitConnection(WindowScreenRange)