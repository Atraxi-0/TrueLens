import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post('http://127.0.0.1:5000/predict', { text });
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error('Error predicting:', err);
      alert('Failed to get prediction.');
    }
  };

  return (
    <div className="App">
      <h2>📰 Fake News Detector</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="8"
          cols="60"
          placeholder="Paste your news article here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        />
        <br />
        <button type="submit">Check News</button>
      </form>

      {prediction !== null && (
        <div className="result">
          <h3>Result: {prediction === 1 ? '🛑 Fake News' : '✅ Real News'}</h3>
        </div>
      )}
    </div>
  );
}

export default App;
