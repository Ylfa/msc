/**
 * Created by ylfa on 07/04/2017.
 */
import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';

class About extends Component {
  render() {
    return (
      <div>
        <h2>Upplýsingar um verkefnið hér - About.js</h2>
        <p>Blablabla? - about</p>
          <Link to="/">Til baka</Link>
      </div>
    );
  }
}

export default About;