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
                <Grid container spacing={12} justify="center" style={{padding: 12}}>
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
        console.log((Math.max(...match)))
        console.log(match.indexOf(Math.max(...match).toString()))
        this.Score.updateScore(match[this.Expressions.state.expression], match.indexOf(Math.max(...match).toString()));
    }
}
export default GameFrame;