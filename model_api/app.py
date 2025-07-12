from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ import this

import joblib
import os

app = Flask(__name__)
CORS(app)  # ✅ enable CORS here

# Load model and vectorizer
model = joblib.load('model/model.pkl')
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No input text provided'}), 400

    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]

    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
