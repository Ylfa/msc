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

    const families = [
        {
            people: [{
                family_year: '1990',
                family_data: 'FOo'
            },
            {
                family_year: '1999',
                family_data: 'Bar'
            }]
        },
        {
            people: [{
                family_year: '1800',
                family_data: 'FOo'
            },
            {
                family_year: '1900',
                family_data: 'Bar'
            }]
        },
    ]

    return (
        <div>

            {families.map((family, i) => {
                const people = family.people;
                return (
                    <table style={{border: '1px solid #000'}} key={i}>
                        <tr>
                            <th>Ár</th>
                            <th>Ábúendur</th>
                        </tr>
                        {people.map((person, i) => {
                            return (
                              <tr key={i}>
                                  <td>{person.family_year}</td>
                                  <td>{person.family_data}</td>
                              </tr>
                            );
                        })}
                    </table>
                )
            })}
        </div>
    );


    const list = (farm.persons || []).map((person) => {

/*
        var item = [JSON.parse(fam.family_data)];

        var columns = [{key: 'yr_item', label: 'Ártal'}, {key: 'nm_item', label: 'Ábúendur'}];
        React.render(<JsonTable rows={ item }columns={ columns } />, document.body);
*/
//GOAL: Búa til töflu. Fyrir hvert fjnr kemur listi af tími+nafn
        return (
            <li key={person.person_id}>{JSON.parse(person.family_year)} &nbsp; &nbsp; {JSON.parse(person.family_data)}
            <br/>
                <br/>
            </li>


        );
    })


    return (
        <div>
            <br/>
            <h2>{farm.area_name}, {farm.farm_name}</h2>
            <h3>Ártöl og nöfn ábúenda</h3>
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
