import React, { Component } from "react";
import "./App.css";
import axios from "axios";

class App extends Component {
  constructor() {
    super();

    this.state = {
      response: [],
      info: []
    };
  }

  componentDidMount() {
    axios.get("http://localhost:5000/test").then(response => {
      this.setState({
        response: response.data
      });
    });

    axios.get("http://localhost:5000/api/getinfo").then(response => {
      console.log(response);
      this.setState({
        info: response.data
      });
    });
  }

  render() {
    let { response } = this.state;
    console.log(response);
    return (
      <div className="App">
        <h1>This is a React application with a Flask backend.</h1>
        <p>{response}</p>
      </div>
    );
  }
}

export default App;
