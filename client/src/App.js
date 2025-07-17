import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setPrediction(null);
    setConfidence(null);

    try {
      const res = await axios.post('http://127.0.0.1:5000/predict', { text });
      setPrediction(res.data.prediction);
      setConfidence(res.data.confidence);

      setHistory(prev => [
        ...prev,
        {
          text,
          prediction: res.data.prediction,
          confidence: res.data.confidence
        }
      ]);
    } catch (err) {
      console.error('Error predicting:', err);
      alert('Failed to get prediction.');
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <h2>📰 TrueLens: Fake News Detector</h2>

      <div>
        <button onClick={() => setText("Prime Minister announces new AI policy for schools.")}>
          Try Real News
        </button>
        <button onClick={() => setText("Aliens were spotted running Parliament in New Delhi.")}>
          Try Fake News
        </button>
      </div>

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

      {loading && <p>🔄 Checking for fake news...</p>}

      {prediction !== null && (
        <div className="result" style={{ color: prediction === 'FAKE' ? 'red' : 'green', fontWeight: 'bold' }}>
          <h3>Result: {prediction === 'FAKE' ? '🛑 Fake News' : '✅ Real News'}</h3>
          <p>Confidence: {confidence}</p>
        </div>
      )}

      {history.length > 0 && (
        <div className="history">
          <h3>🧾 Prediction History</h3>
          <ul>
            {history.map((item, index) => (
              <li key={index}>
                <span style={{ fontWeight: 'bold' }}>
                  {item.prediction === 'FAKE' ? '🛑' : '✅'} {item.prediction}
                </span>{" "}
                ({item.confidence}) → "{item.text.slice(0, 50)}..."
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
