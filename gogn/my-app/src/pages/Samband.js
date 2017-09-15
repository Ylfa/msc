/**
 * Created by ylfa on 2017-09-07.
 */
import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';

class Samband extends Component {
  render() {
    return (
      <div className="Samband">
        <h2>Hafa samband</h2>
        <p>
            Hægt er að ná samband við Þorstein Guðmundsson í gegnum skilaboðskassanum hér að neðan.
            <br/>
            <br/>
            <form action="mailto:iyo1@hi.is">
                <div>
                    <label for="name">Nafn:</label>
                    <input type="text" id="nafn" name="user_name"></input>
                </div>
                <div>
                    <label for="mail">Tölvupóstfang:</label>
                    <input type="email" id="mail" name="user_mail"></input>
                </div>
                <div>
                    <label for="msg">Skilaboð:</label>
                    <textarea id="msg" name="user_message"></textarea>
                </div>

                <div class="button">
                  <button type="submit">Senda skilaboð</button>
                </div>
            </form>
            </p>
          <Link to="/">Til baka</Link>
      </div>
    );
  }
}

export default Samband;