/**
 * Created by ylfa on 04/04/2017.
 */

import React, { Component } from 'react';
import 'whatwg-fetch';
import {
  Link
} from 'react-router-dom';

class Region extends Component {
  constructor(props) {
    super(props);

    this.state = {
      region: []
    }
  }
  componentDidMount() {
    const id = this.props.match.params.id;
    this.fetchData(id);
  }

  fetchData(id) {
      fetch('http://localhost:5000/api/farm_names')
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
    const { region, error } = this.state;
    const list = region.map((region) => {
      const link = '/region/'+region.area_id+'/' + region.farm_id;
      return (
        <li key={region.farm_id }><Link to={link}>{region.farm_name}</Link></li>
      );
    })

    return (
      <div>
        <h2>Svæði Region</h2>
        <br/>bleble
          {error ? (<p>Villa við að sækja gögn!</p>) : null}
        <ul className="link-list">
          {list + 'belble'}
        </ul>
        <Link to="/">Til baka</Link>
      </div>
    );
  }
}

export default Region;
