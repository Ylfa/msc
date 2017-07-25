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
      fetch('http://localhost:5000/api/farm_fams' + regionid + '/' + farmid)
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
    const area = farm.area_id;

    const name_data = farm.family_data;
    const year_data = farm.family_year;

    const list = farm.map((farm) => {
        return (
           <li key={farm.family_id}>
               <h4>Bær: {farm.farm_name} ártal: {farm.family_year} fjölla: {farm.family_data}</h4>
        )
    })
    return (
        <div>
            <h2>Bær {name} Svæði: {area}</h2>


        <br/><li className="List">{list}</li>

        <br/>{error ? (<p>Villa við að sækja gögn!</p>) : null}
        <Link to="/">Tilbaka</Link>
      </div>
    );
  }
}

export default Farm;
