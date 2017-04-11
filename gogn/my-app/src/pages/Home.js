/**
 * Created by ylfa on 04/04/2017.
 */
import React, { Component } from 'react';
import Regions from '../Regions.js'

import {
  Link
} from 'react-router-dom';

class Home extends Component {
    render() {
        return (
            <div>
                <h1>Svæðin Home</h1>
                <Regions />
                <nav>
                    <ul>
                        <li><Link to="/about">Um verkefnið - Home</Link></li>
                    </ul>
                </nav>

            </div>
        );
    }
}
export default Home;