import React from 'react';
import './Formation.css'; // Import the CSS file for styling

const Formation = ({ players }) => {
  // Split players by position
  const goalkeepers = players.filter(player => player.position === 'GKP');
  const defenders = players.filter(player => player.position === 'DEF');
  const midfielders = players.filter(player => player.position === 'MID');
  const forwards = players.filter(player => player.position === 'FWD');

  return (
    <div className="football-field">
      <div className="row">
        {goalkeepers.map(player => (
          <div className="player goalkeeper" key={player.name}>
            <div className="player name">
                {player.name}
            </div>
            <div className="player xPoints">
               xPoints: {player.xPoints.toFixed(2)}
            </div>
          </div>
        ))}
      </div>
      <div className="row">
        {defenders.map(player => (
          <div className="player defender" key={player.name}>
            <div className="player name">
                {player.name}
            </div>
            <div className="player xPoints">
               xPoints: {player.xPoints.toFixed(2)}
            </div>
          </div>
        ))}
      </div>
      <div className="row">
        {midfielders.map(player => (
          <div className="player midfielder" key={player.name}>
            <div className="player name">
                {player.name}
            </div>
            <div className="player xPoints">
               xPoints: {player.xPoints.toFixed(2)}
            </div>
          </div>
        ))}
      </div>
      <div className="row">
        {forwards.map(player => (
          <div className="player forward" key={player.name}>
            <div className="player name">
                {player.name}
            </div>
            <div className="player xPoints">
               xPoints: {player.xPoints.toFixed(2)}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Formation;
