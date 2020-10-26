import React, { Component} from 'react';
import logo from './logo.svg';
import './App.css';
 import axios from "axios";
class App extends Component {
 constructor (){
   super()
   this.state ={
        temperature: 0,
        precip_type: 'rain',
        precip_chance: 80
      }}
 
 componentDidMount =()=>{
  async function mounted () {
      await axios({ method: "GET", "url": "http://localhost/temperature" })
          .then(result => {
            console.log("result", result)
            this.setState(prevState =>({...prevState, temperature:result.data['temperature_c'] }))
            // this.temperature = result.data['temperature_c'];
          }, error => {
            console.error(error);
          });
      await axios({ method: "GET", "url": `http://localhost/precipitation?temp=${this.temperature}` })
          .then(result => {
            console.log("result", result)

            this.setState(prevState =>({...prevState, precip_chance:result.data['precip_chance'] }))
            this.setState(prevState =>({...prevState, precip_type:result.data['type'] }))

            // this.precip_chance = result.data['precip_chance'];
            // this.precip_type = result.data['type'];
          }, error => {
            console.error(error);
          });
  }
mounted()

}
   
    
  render(){
    return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )};
}

export default App;
