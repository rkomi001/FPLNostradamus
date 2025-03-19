import React, { useState, useEffect } from 'react';
import Formation from './Formation';
import './App.css'; // Import the CSS file for styling


function App() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    // Fetch the player data from the backend API
    fetch('http://localhost:5000/my_team') // Adjust the API URL accordingly
      .then(response => response.json())
      .then(data => setPlayers(data))
      .catch(error => console.error('Error fetching players:', error));
  }, []);

  return (
    <div className="App">
      <h1>Najbolja FPL ekipa je...</h1>
      {players.length > 0 ? (
        <Formation players={players} />
      ) : (
        <p>Ucitavanje...</p>
      )}
    </div>
  );
}

export default App;
