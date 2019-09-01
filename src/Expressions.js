import React from 'react';

class Expressions extends React.Component {
    constructor(props) {
        super(props);
        // var expressions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'];
        // var expressionID = Math.floor(Math.random() * expressions.length);
        // var nextExpression = expressions[expressionID];
        this.expressions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'];
        this.state = {expression: 3}
        this.newExpression= this.newExpression.bind(this);
    }
    newExpression() {
        var expressionID = Math.floor(Math.random() * this.expressions.length);
        var nextExpression = this.expressions[expressionID];
        this.setState({
            expression: expressionID
          })
    }
    render() {
      return (
            <span>
                <h2>{this.props.name}</h2>
                <h2>Pull Expression: {this.expressions[this.state.expression]}</h2>
            </span>
      );
    }
    componentDidMount() {
        
    }
  }

  export default Expressions;