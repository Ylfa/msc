/**
 * Created by ylfa on 04/04/2017.
 */
import React, { Component } from 'react';
import 'whatwg-fetch';
import 'react-json-table';
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
      fetch('http://localhost:5000/api/farm_id/'+id)
        .then(response => response.json())
        .then((data) => {
            console.log('data farm', data);
            this.setState({
//                farm: data.objects,
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

    return (
        <div>
            <br/><h2>{farm.area_name}, {farm.farm_name}</h2>
            {(farm.fams || []).map((fam, i) => {
                return (
                        <table className="FarmTable" key={i}>
                            <tr>
                                <th>Ár</th>
                                <th>Ábúendur</th>
                            </tr>
                            {(farm.persons || []).map((person, j) => {
                                return (
                                  <tr key={j}>
                                      <td>{JSON.parse(person.family_year)}</td>
                                      <td>{JSON.parse(person.family_data)}</td>
                                  </tr>
                                );
                            })}
                        </table>

                )
            })}
            {error ? (<p>Villa við að sækja gögn!</p>) : null}
            <Link to="/">Tilbaka</Link>
        </div>
    )
  }
}
export default Farm;
