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
//                region: data.object,
                region: data,

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
          const {region, error} = this.state;
          console.log(region);
          //var a = JSON.parseJSON(region.farms);

          const list = (region.farms || []).map((farm) => {
              const link = '/region/'+farm.area_id+'/farm/' + farm.farm_id; //BREYTTI HÉR Í AÐ TAKA ÚT REGION

              return (
                  <li key={farm.farm_id}><Link to={link}> {region.area_name} -
                      <bold></bold>{farm.farm_name} </Link></li>
              );
          })

          return (
              <div>
                  <h2>Svæði: </h2>
                  <br/>
                  {error ? (<p>Villa við að sækja gögn!</p>) : null}
                  <ul className="link-list">
                      {list}
                  </ul>
                  <Link to="/">Til baka</Link>
              </div>
          );
  }
}


export default Region;
