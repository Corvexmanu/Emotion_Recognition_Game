import React from 'react'
import Camera from './Camera';
import Timer from './Timer';
import Score from './Score';

class GameFrame extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <Timer limit={5} parent={this} />
                <Camera ref={camera => this.camera = camera} size={240} />
                <Score />
            </div>
        )
    }

    triggerPhotoCapture() {
        this.camera.takePhoto();
    }
}

export default GameFrame;