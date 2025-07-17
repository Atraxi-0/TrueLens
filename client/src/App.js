import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [confidence, setConfidence] = useState(null);

  const handleChange = (e) => {
    setText(e.target.value);
    setResult('');
    setConfidence(null);
  };

  const handleSubmit = async () => {
    if (!text.trim()) {
      setResult('⚠️ Please enter some news text');
      return;
    }

    try {
      const response = await axios.post('http://localhost:5000/predict', { text });
      const data = response.data;

      if (data && data.prediction) {
        setResult(data.prediction === 'REAL' ? '🧠 Real News' : '🚨 Fake News');
        setConfidence(`Confidence: ${(data.confidence * 100).toFixed(2)}%`);
      } else {
        setResult('❌ Invalid response from server');
      }
    } catch (error) {
      console.error('Prediction error:', error);
      setResult('❌ Server error. Please try again.');
    }
  };

  const fetchSample = async (label) => {
    try {
      const res = await axios.get(`http://localhost:5000/sample/${label}`);
      setText(res.data.text);
      setResult('');
      setConfidence(null);
    } catch (error) {
      console.error('Sample fetch error:', error);
      setResult('❌ Could not fetch sample news');
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>📰 Fake News Detector</h2>
      <textarea
        rows="6"
        cols="60"
        placeholder="Paste or type your news here..."
        value={text}
        onChange={handleChange}
      />
      <br />
      <button onClick={handleSubmit}>Check News</button>{' '}
      <button onClick={() => fetchSample('real')}>Try Real News</button>{' '}
      <button onClick={() => fetchSample('fake')}>Try Fake News</button>
      <div style={{ marginTop: 20, fontSize: '18px' }}>
        {result && <p><strong>{result}</strong></p>}
        {confidence && <p>{confidence}</p>}
      </div>
    </div>
  );
}

export default App;
