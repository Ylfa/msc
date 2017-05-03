/**
 * Created by ylfa on 04/04/2017.
 */
import React, { Component } from 'react';
import 'whatwg-fetch';
import {
  Link
} from 'react-router-dom';

class Farm extends Component {

  constructor(props) {
    super(props);

    this.state = {
      farm: {}
    }
  }
  componentDidMount() {
    const regionid = this.props.match.params.regionid;
    const farmid = this.props.match.params.farmid;
    this.fetchData(regionid, farmid);
  }

  fetchData(regionid, farmid) {
      fetch('http://localhost:5000/api/farm_names/' + farmid)
        .then(response => response.json())
        .then((data) => {
            console.log('data', data);
            this.setState({
                farm: data,

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
    const { farm, error } = this.state;
    console.log('farm', farm)
    const name = farm && farm.farm_name ? farm.farm_name : '';
    const area = farm.area_name;
    return (
      <div>
        <h2>Bær {name}</h2>
        <br/>blabla
          {error ? (<p>Villa við að sækja gögn!</p>) : null}
        <Link to="/">Til baka</Link>
      </div>
    );
  }
}

export default Farm;
