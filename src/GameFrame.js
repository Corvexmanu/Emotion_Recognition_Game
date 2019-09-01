import React from 'react'
import Camera from './Camera';
import Timer from './Timer';
import Score from './Score';
import NavBar from './NavBar'
import Expressions from './Expressions'
import Grid from '@material-ui/core/Grid'

class GameFrame extends React.Component {
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
                                <Expressions ref={Expressions => this.Expressions = Expressions}/> 
                                <Timer limit={5} parent={this} />
                                <Camera ref={camera => this.camera = camera} size={240} parent={this} />
                            </Grid> 
                            <Grid item>
                                <Score ref={Score => this.Score = Score}/> 
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
    triggerVideoOn() {
        this.camera.turnVideoOn();
    }
    triggerNewExpression() {
        this.Expressions.newExpression();
    }
    triggerScoreUpdate(match) {
        console.log(this.Expressions.state.expression);
        console.log(match);
        this.Score.updateScore(match[this.Expressions.state.expression]);
    }
}

export default GameFrame;