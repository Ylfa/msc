/**
 * Created by ylfa on 04/04/2017.
 */
import React, { Component } from 'react';
import 'whatwg-fetch';
import {
  Link
} from 'react-router-dom';

class Farm extends Component {
  render() {
    return (
      <div>
        <h1>Bær Farm</h1>
        <p>Hér kemur blob af upplýsingum.</p>
         <Link to="/">Til baka</Link>
      </div>
    );
  }
}

export default Farm;
