import React, { Component } from 'react';
import logo from '../public/hi.png';
import './App.css';

import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';

import Home from './pages/Home.js';
import Region from './pages/Region.js';
import Farm from './pages/Farm.js';
import About from './pages/About.js';
import Regions from './pages/Regions.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Ábúendatal Austur-Húnavatnssýslu</h2>
        </div>
        <div className="App-intro">
            <Router>
                <div>
                    <Route exact path="/" component={Home}/>
                    <Route exact path="/region/:id" component={Region}/>
                    <Route path="/region/:regionid/farm/:farmid" component={Farm}/>
                    <Route path="/about" component={About}/>
                    /*<Route path="/about/region/:regionid/farm/:farmid/:familyid" component={Regions}/>*/
                </div>
            </Router>
        </div>
      </div>
    );
  }
}

export default App;


