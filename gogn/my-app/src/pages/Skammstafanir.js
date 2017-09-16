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
    console.log(words);

    return(

    <div>

        {words.map((words) => {
            return (
                <table><tbody>
                    <tr>
                        <td><dl key={words.lykill}>
                            <dt>{words.skm}</dt>
                            <dd>{words.full_name}</dd>
                        </dl></td>
                    </tr>
                </tbody></table>
        )
    })}
    {error ? (<p>Villa við að sækja gögn!</p>) : null}
    <Link to="/">Tilbaka</Link>
    </div>
   )
}
}
export default Skammstafanir;

