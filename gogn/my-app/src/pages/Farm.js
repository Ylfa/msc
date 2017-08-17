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
        farm: []
    }
  }
  componentDidMount() {
    //const regionid = this.props.match.params.areaid;
    const id = this.props.match.params.farmid;
    console.log('id', id);
    this.fetchData(id); //(regionid, farmid);
  }


  fetchData(id) {
      //api?area=6&family=7
      //sida.is/area/
      fetch('http://localhost:5000/api/farm_id/'+id)
        .then(response => response.json())
        .then((data) => {
            console.log('data farm', data);
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
    console.log(farm);
    const list = (farm.fams || []).map((fam) => {
        const link = '/region/'+farm.area_id+'/farm/' + farm.farm_id; // + '/family/' + fams.family_id; BETRA MEÐ AÐ ÞAÐ FLETTIST STÆRRA ÚT
        //

        return (
            <li key={fam.family_id}><Link to={link}>{farm.area_name},
                {farm.farm_name}<br/>
                <bold></bold> {JSON.parse(fam.family_year)} <br/> {JSON.parse(fam.family_data)}<br/>
                <bold></bold>  <br/></Link></li>
        );
    })


    return (
        <div>
            <br/>
                <ul className="List">
                    {list}
                </ul>
        <br/>
            {error ? (<p>Villa við að sækja gögn!</p>) : null}
        <Link to="/">Tilbaka</Link>
        </div>
    );
  }
}
export default Farm;
