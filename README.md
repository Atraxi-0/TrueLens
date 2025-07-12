
---

### ✅ HTML VERSION (for GitHub README rendering)

```html
<h1>📰 TrueLens: Fake News Detection for Indian Media</h1>

<p>TrueLens is an AI-powered web application that detects fake news from real news using a machine learning model trained on Indian datasets. It provides a REST API and a user-friendly React frontend for live predictions.</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>🧠 Machine Learning model trained on Indian news (<code>fri_dataset.csv</code>)</li>
  <li>🔍 Real-time news classification (Fake / Real)</li>
  <li>🧪 REST API built with Flask</li>
  <li>🌐 React frontend for end-user interaction</li>
  <li>📦 TF-IDF vectorization for text processing</li>
  <li>✅ High accuracy (>98%) using Logistic Regression</li>
</ul>

<hr>

<h2>🗂️ Project Structure</h2>

<pre><code>TrueLens/
├── data/                     # Raw real/fake scraped data
├── dataset/                  # Cleaned, processed, and split data
├── model_api/                # Flask API with model & vectorizer
│   ├── model/                # Saved model.pkl and vectorizer.pkl
│   └── app.py                # Flask app
├── client/                   # React frontend
│   └── src/
│       └── App.js            # Frontend logic
├── notebooks/                # Jupyter notebooks (EDA, training)
│   ├── 01_eda_and_cleaning.ipynb
│   └── 02_model_training.ipynb
├── venv/                     # Virtual environment
├── requirements.txt          # Python dependencies
└── README.md
</code></pre>

<hr>

<h2>🧪 How to Use</h2>

<h3>✅ Backend (Flask)</h3>

<ol>
  <li>Clone the repo:</li>
</ol>
<pre><code>git clone https://github.com/your-username/TrueLens.git
cd TrueLens
</code></pre>

<ol start="2">
  <li>Create and activate a virtual environment:</li>
</ol>
<pre><code>python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
</code></pre>

<ol start="3">
  <li>Install Python dependencies:</li>
</ol>
<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="4">
  <li>Run the Flask API:</li>
</ol>
<pre><code>cd model_api
python app.py
</code></pre>

<h3>✅ Frontend (React)</h3>

<ol>
  <li>Install frontend dependencies:</li>
</ol>
<pre><code>cd ../client
npm install
</code></pre>

<ol start="2">
  <li>Start the React app:</li>
</ol>
<pre><code>npm start
</code></pre>

<ol start="3">
  <li>Open in your browser:</li>
</ol>
<pre><code>http://localhost:3000</code></pre>

<hr>

<h2>📡 API Endpoint</h2>

<p><strong>POST</strong> <code>/predict</code></p>

<p><strong>Example:</strong></p>
<pre><code>POST http://localhost:5000/predict
Content-Type: application/json

{
  "text": "This is the news article text to classify."
}
</code></pre>

<p><strong>Response:</strong></p>
<pre><code>{
  "prediction": 0  // 0 = Real, 1 = Fake
}
</code></pre>

<hr>

<h2>⚠️ Limitations</h2>

<ul>
  <li>❌ Cannot detect fake news in real-time from the internet</li>
  <li>🧠 Model is limited to the data it was trained on (<code>fri_dataset.csv</code>)</li>
</ul>

<hr>

<h2>🏁 Future Improvements</h2>

<ul>
  <li>Integrate real-time scraping and classification</li>
  <li>Use transformer-based models (e.g., BERT)</li>
  <li>Add more Indian datasets (regional + national)</li>
  <li>Deploy to cloud (Render/Netlify/Vercel)</li>
</ul>

<hr>

