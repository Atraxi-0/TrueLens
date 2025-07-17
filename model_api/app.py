from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sample_news import get_random_sample

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

    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    prob = model.predict_proba(text_vector)[0].max()

    result = {
        'prediction': 'FAKE' if prediction == 1 else 'REAL',
        'confidence': round(float(prob), 4)
    }

    return jsonify(result)

@app.route('/sample/<label>', methods=['GET'])
def sample_news(label):
    try:
        if label == 'fake':
            sample = get_random_sample(1)
        elif label == 'real':
            sample = get_random_sample(0)
        else:
            return jsonify({'error': 'Invalid label'}), 400

        return jsonify({'text': sample})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
