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
            region: [],
            error: false,

        }
  }

  componentDidMount() {
    const id = this.props.match.params.id;
    this.fetchData(id);
  }


  fetchData(id) {
      fetch('http://localhost:5000/api/area_id/'+id)
        .then(response => response.json())
        .then((data) => {
            console.log('data', data);
            this.setState({
                region: data.objects,

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
//      if (this.state.region) {
          const {region, error} = this.state;
          console.log(region);
          const list = (region || []).map((region) => {
              const link = '/region/' + region.id + '/farm/' + region.farm_id;

              return (
                  <li key={region.farm_id}><Link to={link}>Hreppur: {region.area_name} -
                      <bold>Bær:</bold>{region.farm_name} </Link></li>
              );
          })

          return (
              <div>
                  <h2>Svæði Region</h2>
                  <br/>
                  {error ? (<p>Villa við að sækja gögn!</p>) : null}
                  <ul className="link-list">
                      {list}
                  </ul>
                  <Link to="/">Til baka</Link>
              </div>
          );
      }
 // }


}

export default Region;

//render() { if(this.state.region) { ...}
