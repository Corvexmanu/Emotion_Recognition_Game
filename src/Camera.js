import React from 'react';
import './Camera.css';

class Camera extends React.Component {

  render() {

    let parentStyle = {
      'overflow': 'hidden',
      'width': this.props.size + 'px',
      'height': this.props.size + 'px'
    }

    let stylingProperties = {
      'height': '100%',
      'position': 'relative',
      'left': '-25%'
    };

    return (

      <div style={parentStyle}>
        <video autoPlay={true} id="videoElement" style={stylingProperties}></video>
        <canvas id="canvas" width={this.props.size + 'px'} height={this.props.size + 'px'}></canvas>
      </div >
    );
  }
  componentDidMount() {
    this.videoElement = document.querySelector("#videoElement");

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
          this.videoElement.srcObject = stream;
        }.bind(this))
        .catch(function (err0r) {
          console.log("Something went wrong!", err0r);
        });
    }
  }

  takePhoto() {
    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");

    // TODO: Fix aspect ratio

    /*let w = this.videoElement.videoWidth;
    let h = this.videoElement.videoHeight;

    let mult = h / canvas.height;
    let actualW = w / mult;

    let xOffset = (actualW - canvas.width) / 2;
    console.log(xOffset);
    */
    ctx.drawImage(this.videoElement, 0, 0, canvas.width, canvas.height);
    this.videoElement.style.display = 'none';

    let dataArray = ctx.getImageData(0, 0, canvas.width, canvas.height).data;

    fetch('http://localhost:5000/predict', {
      method: 'post',
      headers: { 'Content-Type': 'text/plain' },
      body: dataArray.toString()
    }).then(res => {
      console.log(res);
      return res.text();
    })
      .then(res => {
        console.log(res);
      });
  }
}

export default Camera;
