/**
 * Created by ylfa on 07/04/2017.
 */
import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';

class About extends Component {
  render() {
    return (
      <div>
        <h2>Um verkefnið</h2>
        <p>
            Uppsetning þessara vefsíðu var meistaraverkefni Ylfu Ólafsdóttir í hugbúnaðarverkfræði.
            Markmiðið var að búa til heimasíðu sem birtir gögn úr ábúendatali frá Austur-Húnavatnssýslu
            sem safnað hefur verið saman í Excelskjal af Þorsteini Guðmundsson. <br/>

            Til þess að ná markmiði verkefnisins var búið til forrit sem vinnur gögnin upp úr Excelskjalinu
            og skráir þau í  SQLite gagnasafn. Gögnin eru gerð aðgengileg á netinu með forritaskil sem sér
            um samskipti við vefsíðuna. <br/>
            Á vefsíðunni er hægt að skoða gögnin þar sem þau eru flokkuð eftir hreppum, bæjum og tímabilum. </p>
          <Link to="/">Til baka</Link>
      </div>
    );
  }
}

export default About;