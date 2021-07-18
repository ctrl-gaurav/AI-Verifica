import React from 'react'
import '../App.css'
import bubbles from './image/bubbles.png'
import processing from './image/processing.png'
import imageupload from './image/imageupload.png'


const Upload = ()=>{
    
    return(
        <div className = "upload">
            <div className = "bubbles_container">
                <img src = {bubbles} class="bubbles" ></img>
                <img src = {imageupload} class = "process" onClick  = {()=> alert("Processing..")}></img>

            </div>
        </div>
    )
}

export default Upload