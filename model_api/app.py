from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load('model/model.pkl')
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({'error': 'No input text provided'}), 400

    # Transform text using vectorizer
    text_vector = vectorizer.transform([text])

    # Make prediction
    prediction = model.predict(text_vector)[0]  # 0 or 1
    prob = model.predict_proba(text_vector)[0].max()  # max confidence

    result = {
        'prediction': 'FAKE' if prediction == 1 else 'REAL',
        'confidence': round(float(prob), 4)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
