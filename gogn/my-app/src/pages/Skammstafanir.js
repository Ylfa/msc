/**
 * Created by ylfa on 2017-09-08.
 */
/**
 * Created by ylfa on 2017-09-07.
 */
import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';

class Skammstafanir extends Component {

  constructor(props) {
    super(props);

    this.state = {
      words: [],
      error: false,
    }
  }

  componentDidMount() {
    this.fetchData();
  }

  fetchData() {
      fetch('http://localhost:5000/api/skammstafanir')
        .then(response => response.json())
        .then((data) => {
            console.log('data', data);
            this.setState({
                words: data.objects,
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
    const { words, error } = this.state;
    const list = words.map((words) => {

      return (
          <li key={words.lykill}>{ words.skm } - {words.full_name}</li>
      );
    })

    return (
      <div>
          {error ? (<p>Villa við að sækja gögn!</p>) : null}
        <ul className="link-list">
            <h2> Styttingar og þýðing þeirra </h2>
            {list}
        </ul>
      </div>
    );
  }
}

export default Skammstafanir;