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
import Samband from './pages/Samband.js';
import Skammstafanir from './pages/Skammstafanir.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>
              <img src={logo} className="App-logo" alt="logo" />
              <span> Ábúendatal Austur-Húnavatnssýslu</span>
          </h2>
        </div>
            <nav className="navigation">
                <ul className="mainmenu">
                    <li><a href="/">Hreppir</a></li>
                    <li><a href="/Skammstafanir">Skammstafanir</a></li>
                    <li><a href="/about">Um verkefnið</a></li>
                    <li><a href="/Samband">Hafa samband</a></li>
                </ul>
            </nav>


          <div className="App-intro">
            <Router>
                <div>
                    <Route exact path="/" component={Home}/>
                    <Route exact path="/region/:id" component={Region}/>
                    <Route path="/region/:regionid/farm/:farmid" component={Farm}/>
                    <Route path="/about" component={About}/>
                    <Route path="/Samband" component={Samband}/>
                    <Route path="/Skammstafanir" component={Skammstafanir}/>
                </div>
            </Router>
        </div>
      </div>
    );
  }
}

export default App;


