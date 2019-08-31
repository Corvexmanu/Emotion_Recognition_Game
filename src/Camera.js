import React from 'react';
import './Camera.css';

class Camera extends React.Component {
  render() {
    return (
      <video autoPlay="true" id="videoElement">
      </video>
    );
  }
  componentDidMount() {
    var video = document.querySelector("#videoElement");

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
}

export default Camera;
