import React from 'react';

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
                <h1>{this.state.score}</h1>
                <button onClick={this.increaseScore}>+2</button>
            </span>
      );
    }
    componentDidMount() {
        
    }
  }
  

  export default Score;