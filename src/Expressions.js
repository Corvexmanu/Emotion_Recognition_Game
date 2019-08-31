import React from 'react';

class Expressions extends React.Component {
    constructor(props) {
        super(props);
        var expressions = ['Angry', 'Fear', 'Disgust', 'Happy', 'Surprise'];
        var expressionID = Math.floor(Math.random() * expressions.length);
        var nextExpression = expressions[expressionID];
        this.state = {expression: nextExpression}
        this.setExpression= this.setExpression.bind(this);
    }
    setExpression() {
        this.setState({
          expression: this.state.expression
        });
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