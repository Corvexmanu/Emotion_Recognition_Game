import React from 'react'
import Camera from './Camera';
import Timer from './Timer';
import Score from './Score';
import NavBar from './NavBar'
import Expressions from './Expressions'
import Grid from '@material-ui/core/Grid'

class GameFrame extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <NavBar />
                {/* spacing={24} style={{padding: 24}} */}
                {/* xs={12} sm={6} lg={4} xl={3} */}
                <Grid container spacing={24} style={{padding: 24}}>
                    { (
                        <div>
                            <Grid item>
                                <Expressions /> 
                                <Timer limit={5} parent={this} />
                                <Camera ref={camera => this.camera = camera} size={240} />
                            </Grid> 
                            <Grid item>
                                <Score /> 
                            </Grid> 
                        </div>
                    )}
                </Grid>
                {/* <Score />  */}
            </div>
        )
    }

    triggerPhotoCapture() {
        this.camera.takePhoto();
    }
}

export default GameFrame;