import React from 'react';

class Timer extends React.Component {
  constructor(props) {
    super(props);
    const timeLimit = props.limit;
    this.state = {
        currentTime: timeLimit
      };
  }
  render() {
    return (
        <div>
            <text>Pose in: </text>
            <span>{this.state.currentTime}</span>
        </div>
    );
  }
  componentDidMount() {
    this.interval = setInterval(this.tick.bind(this), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  tick() {
    if (this.state.currentTime > 0) {
        this.setState({
            currentTime: this.state.currentTime - 1
          })
    }
    else if (this.state.currentTime === 0) {
      clearInterval(this.interval);
      // Take photo
      this.props.parent.triggerPhotoCapture();
      setTimeout(function(){
        this.setState({
            currentTime: this.props.limit
          })
        this.interval = setInterval(this.tick.bind(this), 1000);
        this.props.parent.triggerVideoOn();
        this.props.parent.triggerNewExpression();
      }.bind(this), 3000);
    }
  }
}

export default Timer;