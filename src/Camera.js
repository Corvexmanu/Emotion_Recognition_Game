import React from 'react';
import './Camera.css';

class Camera extends React.Component {
  render() {
    return (
      <div>
        <video autoPlay={true} id="videoElement" width={this.props.size} height={this.props.size} style={{ 'object-fit': 'fill' }}></video>
        <canvas id="canvas"></canvas>
      </div >
    );
  }
  componentDidMount() {
    let video = document.querySelector("#videoElement");

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
          video.srcObject = stream;
        })
        .catch(function (err0r) {
          console.log("Something went wrong!");
        });
    }
  }

  takePhoto() {
    let videoSnapshot = document.getElementById("videoElement");
    let canvas = document.getElementById("canvas");
    canvas.width = 500;
    canvas.height = 500;
    let ctx = canvas.getContext("2d");
    ctx.drawImage(videoSnapshot, 0, 0, canvas.width, canvas.height);
    console.log(ctx.getImageData(0, 0, canvas.width, canvas.height));
  }
}

export default Camera;
