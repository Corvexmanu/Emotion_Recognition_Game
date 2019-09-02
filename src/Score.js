import React from 'react';
import Button from '@material-ui/core/Button';

class Score extends React.Component {
    constructor(props) {
      super(props);
      this.state = {score: 0}
      this.match = 0;
      this.round = 1;
      this.bestMatch = "";
      this.updateScore = this.updateScore.bind(this);
    }
    updateScore(match, bestMatch) {
      var expressions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise'];
      this.bestMatch = expressions[bestMatch];

      match = Number(match);
      console.log(match)
      this.round = this.round + 1;
      this.match = Math.floor(match*100);
      this.setState({
        score: this.state.score + Math.round(match*10)
      });
    }
    render() {
      return (
            <span>
              <center>
                <h2>{this.props.name}</h2>
                <h3>
                  Round: {this.round}
                  <br></br>
                  Match: {this.match}%
                  <br></br>
                  Best Match: {this.bestMatch}
                  <br></br>
                  Score: {this.state.score}
                </h3>
                <Button color="primary" onClick={() => { 
                    this.round = 1;
                    this.match = 0;
                    this.setState({
                        score: 0
                      });
                 }}>
                    Restart
                </Button>
                </center>
            </span>
      );
    }
    componentDidMount() {
        
    }
  }
  export default Score;