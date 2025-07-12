<h1>📰 TrueLens: Fake News Detection Web App (India-focused)</h1>
<p><img src="https://img.shields.io/badge/AI-Fake_News_Detector-blue?style=for-the-badge" alt="Badge" /></p>
<p>A machine learning-based web application to detect whether a news article is <strong>fake</strong> or <strong>real</strong>, using NLP and logistic regression.</p>

<h2>🔍 Overview</h2>
<p>TrueLens is an AI-powered tool designed to detect fake news content. The model is trained on a dataset of 9,999 Indian news articles and classifies input news as either <strong>real (0)</strong> or <strong>fake (1)</strong>.</p>

<h2>✅ Features</h2>
<ul>
  <li>🧠 ML model trained on Indian fake news dataset (<code>fri_dataset.csv</code>)</li>
  <li>📊 Logistic Regression + TF-IDF for feature extraction</li>
  <li>🖥️ Web app with Flask API backend + MERN frontend (in development)</li>
  <li>🔁 Cross-validation and evaluation metrics (accuracy: <strong>~99%</strong>)</li>
  <li>🌐 Real-time news classification using typed input or future APIs</li>
</ul>

<h2>🧪 Technologies Used</h2>
<ul>
  <li>Python, Flask</li>
  <li>Scikit-learn, Pandas, Numpy</li>
  <li>TF-IDF Vectorization</li>
  <li>React (frontend), Node.js (planned)</li>
  <li>Joblib for model serialization</li>
  <li>Google Colab for training</li>
</ul>

<h2>📂 Project Structure</h2>
<pre><code>TrueLens/
│
├── model_api/
│   ├── app.py                  # Flask API
│   └── model/
│       ├── model.pkl           # Trained model
│       └── tfidf_vectorizer.pkl
│
├── notebooks/
│   ├── 01_eda_and_cleaning.ipynb
│   └── 02_model_training.ipynb
│
├── dataset/
│   ├── fri_dataset.csv
│   ├── fri_dataset_cleaned.csv
│   ├── train_data.csv
│   └── test_data.csv
│
├── data/
│   ├── real/                   # Optional real news articles
│   └── fake/                   # Optional fake news articles
│
└── requirements.txt
</code></pre>

<h2>📈 Performance</h2>
<ul>
  <li>✅ <strong>Accuracy</strong>: 99.18%</li>
  <li>✅ <strong>Precision/Recall</strong>: Balanced</li>
  <li>✅ <strong>Cross-validation</strong>: ~98.9% mean accuracy</li>
</ul>

<h2>🧪 How to Use</h2>
<ol>
  <li>Clone the repo:
    <pre><code>git clone https://github.com/your-username/TrueLens.git
cd TrueLens</code></pre>
  </li>
  <li>Install requirements:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the Flask backend:
    <pre><code>cd model_api
python app.py</code></pre>
  </li>
  <li>Use <a href="https://hoppscotch.io" target="_blank">Hoppscotch</a> or Postman to send:
    <pre><code>POST http://localhost:5000/predict
{
  "text": "Your news headline or content here"
}
</code></pre>
  </li>
</ol>

<h2>⚠️ Lim
