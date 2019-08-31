import React from 'react';

class Timer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentTime: props.limit
    };
  }
  render() {
    return (
      <span>{this.state.currentTime}</span>
    );
  }
  componentDidMount() {
    this.interval = setInterval(this.tick.bind(this), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  tick() {
    this.setState({
      currentTime: this.state.currentTime - 1
    })

    if (this.state.currentTime === 0) {
      clearInterval(this.interval);
      // Take photo
      this.props.parent.triggerPhotoCapture();
    }
  }
}

export default Timer;