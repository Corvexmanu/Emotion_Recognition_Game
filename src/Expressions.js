import React from 'react';

class Expressions extends React.Component {
    constructor(props) {
        super(props);
        var expressions = ['Angry', 'Fear', 'Disgust', 'Happy', 'Surprise'];
        var expressionID = Math.floor(Math.random() * expressions.length);
        var nextExpression = expressions[expressionID];
        this.state = {expression: nextExpression}
        this.newExpression= this.newExpression.bind(this);

    }
    newExpression() {
        var expressions = ['Angry', 'Fear', 'Disgust', 'Happy', 'Surprise'];
        var expressionID = Math.floor(Math.random() * expressions.length);
        var nextExpression = expressions[expressionID];
        this.setState({
            expression: nextExpression
          })
    }
    render() {
      return (
            <span>
                <h2>{this.props.name}</h2>
                <h2>Pull Expression: {this.state.expression}</h2>
            </span>
      );
    }
    componentDidMount() {
        
    }
  }

  export default Expressions;