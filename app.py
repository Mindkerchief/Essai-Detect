import joblib
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logreg_model = None
tfidf_model = None
id2label = {0: "Human-Written", 1: "LLM-Generated"}

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

def load_model():
    global logreg_model, tfidf_model
    tfidf_model = joblib.load('model/tfidf.pkl')
    logreg_model = joblib.load('model/logreg.pkl')

def predict(text):
    text_vectorized = tfidf_model.transform([text])
    pred = logreg_model.predict(text_vectorized)
    conf = logreg_model.predict_proba(text_vectorized)
    confidence = conf[0][pred[0]]

    # Adjust prediction output to compesate for the model's bias
    if pred[0] == 1 and confidence < 0.81:
        confidence = 1 - confidence
        pred[0] = 0
    return pred[0], confidence

@app.route('/analyze', methods=['POST'])
def analyze_logreg():
    data = request.get_json()
    text = data.get("text", "")

    pred, confidence = predict(text)
    label = id2label[pred]
    
    return jsonify({
        "prediction": label,
        'confidence': f'{confidence:.2f}'
    })

if __name__ == '__main__':
    load_model()
    app.run()
