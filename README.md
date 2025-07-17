<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>
  <h1>🕵️‍♂️ TrueLens: See Truth Through Falsehoods</h1>

  <p>
    TrueLens is an AI-powered fake news detection web application tailored for Indian media. It utilizes machine learning models trained on a combination of real and fake news datasets to help users verify the authenticity of online news.
  </p>

  <div class="section">
    <h2>🚀 Features</h2>
    <ul>
      <li>📰 Classifies news as <strong>Real</strong> or <strong>Fake</strong></li>
      <li>📊 Confidence scores for each prediction</li>
      <li>🧪 Buttons to try real and fake sample news</li>
      <li>⚙️ React + Flask modular architecture</li>
      <li>🔧 Easy local setup with virtual environments</li>
      <li>🧠 Model trained on Kaggle, BoomLive, and Alt News data</li>
    </ul>
  </div>

  <div class="section">
    <h2>📂 Project Structure</h2>
    <pre>
TrueLens/
├── client/                 # React frontend
│   ├── public/
│   └── src/
│       ├── App.js
│       └── index.js
├── model_api/              # Python Flask backend
│   ├── app.py              # API server
│   ├── model.pkl           # Trained ML model
│   ├── vectorizer.pkl      # TF-IDF vectorizer
│   ├── sample_news.py      # Loads sample news
│   ├── sample_data.csv     # Sample real/fake articles
│   └── requirements.txt
├── README.md
└── .gitignore
    </pre>
  </div>

  <div class="section">
    <h2>🛠️ Tech Stack</h2>
    <ul>
      <li><strong>Frontend:</strong> React, JavaScript, Axios</li>
      <li><strong>Backend:</strong> Python, Flask</li>
      <li><strong>Machine Learning:</strong> Scikit-learn, TF-IDF Vectorizer</li>
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
python -m venv venv
      
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux

pip install -r requirements.txt

cd model_api
python app.py
    </pre>
    <p>Flask API will run at <code>http://localhost:5000</code></p>
    <h3>3. Setup Frontend (React)</h3>
    <pre>
cd client
npm install
npm start
    </pre>
    <p>React app will run at <code>http://localhost:3000</code></p>
  </div>

  <div class="section">
    <h2>✨ Example Usage</h2>
    <ul>
      <li>Paste news into the input box</li>
      <li>Click <strong>"Check News"</strong> to see prediction</li>
      <li>Try quick samples with:
        <ul>
          <li>📄 "Try Real News"</li>
          <li>📄 "Try Fake News"</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="section">
    <h2>🧠 Model Training</h2>
    <ul>
      <li>TF-IDF vectorization + Logistic Regression classifier</li>
      <li>Datasets from Kaggle, BoomLive, and Alt News</li>
      <li>Saved as <code>model.pkl</code> and <code>vectorizer.pkl</code></li>
    </ul>
  </div>

  <div class="section">
    <h2>📌 Future Improvements</h2>
    <ul>
      <li>Use BERT or multilingual transformer models</li>
      <li>Integrate auto-scheduled scrapers</li>
      <li>Store article metadata with database support</li>
      <li>Deploy to Render, Vercel, or Railway</li>
    </ul>
  </div>

  <!--
  <div class="section">
    <h2>📄 License</h2>
    <p>This project is licensed under the MIT License – see the <code>LICENSE</code> file for details.</p>
  </div>
  -->

  <div class="section">
    <h2>🤝 Acknowledgments</h2>
    <ul>
      <li><a href="https://www.altnews.in/">Alt News</a></li>
      <li><a href="https://www.boomlive.in/">BoomLive</a></li>
      <li><a href="https://scikit-learn.org/">Scikit-learn</a></li>
      <li><a href="https://www.kaggle.com/">Kaggle</a></li>
    </ul>
  </div>

  <div class="section">
    <h2>📬 Contact</h2>
    <p>Made by <a href="https://github.com/Atraxi-0" target="_blank">Krishna Kant Pathak</a></p>
  </div>
</body>
</html>
