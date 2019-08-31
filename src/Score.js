import React from 'react';
import Button from '@material-ui/core/Button';

class Score extends React.Component {
    constructor(props) {
      super(props);
      this.state = {score: 0}
      this.increaseScore = this.increaseScore.bind(this);
    }
    increaseScore() {
        this.setState({
          score: this.state.score + 2
        });
    } 
    render() {
      return (
            <span>
                <h2>{this.props.name}</h2>
                <h2>Score: {this.state.score}</h2>
                <Button color="primary" onClick={() => { 
                    this.setState({
                        score: this.state.score = 0
                      });
                 }}>
                    New Game
                </Button>
                <button onClick={this.increaseScore}>+2</button>
            </span>
      );
    }
    componentDidMount() {
        
    }
  }

  export default Score;