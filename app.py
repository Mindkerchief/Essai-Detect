import joblib
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)
CORS(app)

bert_model = None
bert_tokenizer = None
logreg_model = None
logreg_vectorizer = None
model_mode = -1 # 1 = BERT, 0 = Logistic Regression
id2label = {0: "Human-Written", 1: "LLM-Generated"}

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

def load_bert_model():
    global bert_model, bert_tokenizer, model_mode
    if not os.path.exists('model/bert'):
        raise FileNotFoundError("BERT model files not found.")
    bert_tokenizer = AutoTokenizer.from_pretrained('model/bert')
    bert_model = AutoModelForSequenceClassification.from_pretrained('model/bert', trust_remote_code=True)
    bert_model.eval()
    model_mode = 1

def load_logreg_model():
    if not os.path.exists('model/tfidf.pkl') or not os.path.exists('model/logreg.pkl'):
        raise FileNotFoundError("Logistic Regression model files not found.")
    global logreg_model, logreg_vectorizer, model_mode
    logreg_vectorizer = joblib.load('model/tfidf.pkl')
    logreg_model = joblib.load('model/logreg.pkl')
    model_mode = 0

def predict_logreg(text):
    text_vectorized = logreg_vectorizer.transform([text])
    pred = logreg_model.predict(text_vectorized)
    conf = logreg_model.predict_proba(text_vectorized)
    confidence = conf[0][pred[0]]

    # Adjust prediction output to compesate for the model's bias
    if pred[0] == 1 and confidence < 0.81:
        confidence = 1 - confidence
        pred[0] = 0
    return pred[0], confidence

def predict_bert(text):
    inputs = bert_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=-1)
        pred = torch.argmax(probs, dim=-1).item()
        confidence = torch.max(probs).item()
    return pred, confidence

def load_model(model_num):
    if model_num == 0:
        load_logreg_model()
    elif model_num == 1:
        load_bert_model()

def predict(text):
    if model_mode == 0:
        return predict_logreg(text)
    elif model_mode == 1:
        return predict_bert(text)
    else:
        raise ValueError("Model is missing.")

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get("text", "")

    pred, confidence = predict(text)
    label = id2label[pred]
    
    return jsonify({
        "prediction": label,
        'confidence': f'{confidence:.2f}'
    })

if __name__ == '__main__':
    load_model(1) # Change the number to switch models
    app.run()
