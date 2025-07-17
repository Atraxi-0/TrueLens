<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>TrueLens - Project README</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      max-width: 900px;
      margin: auto;
      padding: 2rem;
      background-color: #f8f9fa;
      color: #212529;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code, pre {
      background-color: #eee;
      padding: 0.3em 0.5em;
      border-radius: 4px;
      font-family: Consolas, monospace;
    }
    pre {
      overflow-x: auto;
      padding: 1em;
      background: #272822;
      color: #f8f8f2;
    }
    .emoji {
      font-size: 1.2em;
    }
    ul {
      margin-top: 0;
    }
    a {
      color: #007acc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .section {
      margin-bottom: 2rem;
    }
  </style>
</head>
<body>
  <h1 class="emoji">🕵️‍♂️ TrueLens: See Truth Through Falsehoods</h1>

  <p>
    TrueLens is a powerful AI-driven fake news detection web application tailored for the Indian media landscape. Using advanced machine learning techniques and a real-world dataset, TrueLens helps identify whether a news article is real or fake, supporting media literacy and critical consumption of information.
  </p>

  <div class="section">
    <h2>🚀 Features</h2>
    <ul>
      <li>📰 Detects whether input news is <strong>real</strong> or <strong>fake</strong></li>
      <li>🎯 Provides <strong>confidence scores</strong> for each prediction</li>
      <li>🔁 Includes buttons to try <strong>sample real and fake news</strong></li>
      <li>🔎 Built with a modular <strong>React + Flask</strong> architecture</li>
      <li>📁 Easy setup and deployment using virtual environments</li>
      <li>📊 Custom-trained model using cleaned datasets (Kaggle, BoomLive, Alt News)</li>
    </ul>
  </div>

  <div class="section">
    <h2>📂 Project Structure</h2>
    <pre>
TrueLens/
├── client/                  # React frontend
│   ├── public/
│   └── src/
│       └── App.js
│       └── index.js
├── model_api/              # Python Flask backend
│   ├── app.py              # API server for predictions
│   ├── model.pkl           # Trained ML model
│   ├── vectorizer.pkl      # TF-IDF vectorizer
│   ├── sample_news.py      # Sample news text loader
│   ├── sample_data.csv     # Pool of real/fake sample news
│   └── requirements.txt
├── README.md               # Project documentation
└── .gitignore
    </pre>
  </div>

  <div class="section">
    <h2>🛠️ Tech Stack</h2>
    <ul>
      <li><strong>Frontend:</strong> React, JavaScript, Axios</li>
      <li><strong>Backend:</strong> Python, Flask</li>
      <li><strong>ML:</strong> Scikit-learn, Pandas, TF-IDF Vectorizer</li>
      <li><strong>Deployment Ready:</strong> Yes</li>
    </ul>
  </div>

  <div class="section">
    <h2>💻 How to Run Locally</h2>

    <h3>1. Clone the Repository</h3>
    <pre>
git clone https://github.com/Atraxi-0/TrueLens.git
cd TrueLens
    </pre>

    <h3>2. Setup Backend (Flask)</h3>
    <pre>
cd model_api
python -m venv venv
venv\Scripts\activate          # Windows
# Or: source venv/bin/activate # macOS/Linux

pip install -r requirements.txt
python app.py
    </pre>
    <p>Flask server will run on <code>http://localhost:5000</code></p>

    <h3>3. Setup Frontend (React)</h3>
    <pre>
cd client
npm install
npm start
    </pre>
    <p>Frontend will run on <code>http://localhost:3000</code></p>
  </div>

  <div class="section">
    <h2>✨ Example Usage</h2>
    <ul>
      <li>Paste or type a news article into the textarea.</li>
      <li>Click <strong>"Check News"</strong>.</li>
      <li>You'll get:
        <ul>
          <li>✅ Prediction: Fake or Real</li>
          <li>📊 Confidence Score</li>
        </ul>
      </li>
      <li>Or try quick examples:
        <ul>
          <li>🔘 "Try Real News"</li>
          <li>🔘 "Try Fake News"</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="section">
    <h2>🧠 Model Training</h2>
    <p>The ML model was trained on:</p>
    <ul>
      <li>Indian Fake News dataset from Kaggle</li>
      <li>Scraped real articles from Alt News and BoomLive</li>
      <li>TF-IDF vectorization + Logistic Regression</li>
      <li>Trained and exported via <code>model.pkl</code> and <code>vectorizer.pkl</code></li>
    </ul>
  </div>

  <div class="section">
    <h2>📌 Future Improvements</h2>
    <ul>
      <li>Upgrade to BERT or multilingual transformer models</li>
      <li>Scraper scheduler and database integration</li>
      <li>Track sources and article metadata</li>
      <li>Deploy on cloud (Render, Vercel, or Railway)</li>
    </ul>
  </div>

  <div class="section">
    <h2>📄 License</h2>
    <p>This project is licensed under the MIT License – see <a href="#">LICENSE</a> for details.</p>
  </div>

  <div class="section">
    <h2>🤝 Acknowledgments</h2>
    <ul>
      <li><a href="https://www.altnews.in/">Alt News</a></li>
      <li><a href="https://www.boomlive.in/">BoomLive</a></li>
      <li><a href="https://scikit-learn.org/">Scikit-learn</a></li>
      <li><a href="https://www.kaggle.com/">Kaggle Dataset</a></li>
    </ul>
  </div>

  <div class="section">
    <h2>📬 Contact</h2>
    <p>Made with ❤️ by <a href="https://github.com/Atraxi-0" target="_blank">Krishna Kant Pathak</a></p>
    <p>Feel free to open an issue or pull request to contribute!</p>
  </div>
</body>
</html>
