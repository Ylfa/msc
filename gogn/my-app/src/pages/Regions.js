/**
 * Created by ylfa on 04/04/2017.
 */
import React, { Component } from 'react';
import 'whatwg-fetch';

import {
  Link
} from 'react-router-dom';


class Regions extends Component {

  constructor(props) {
    super(props);

    this.state = {
      regions: [],
      error: false,
    }
  }

  componentDidMount() {
    this.fetchData();
  }

  fetchData() {
      fetch('http://localhost:5000/api/area_id')
        .then(response => response.json())
        .then((data) => {
            console.log('data', data);
            this.setState({
                regions: data.objects,
            });
        })
          .catch((err) => {
             console.log('villa', err)
              this.setState({
                  error: true,
              })
          });
  }

  render() {
    const { regions, error } = this.state;

    const list = regions.map((regions) => {
      const link = '/region/' + regions.area_id;
      return (

          <li key={regions.area_id}><Link to={link}>{regions.area_name}</Link></li>
      );
    })

    return (
      <div>
        <h2>Svæði:</h2>
          {error ? (<p>Villa við að sækja gögn!</p>) : null}
        <ul className="link-list">
          {list}
        </ul>
      </div>
    );
  }
}

export default Regions;