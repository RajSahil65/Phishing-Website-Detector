from flask import Flask, render_template, request, jsonify
import pickle
from feature_extraction import extract_features_from_url

app = Flask(__name__)

# Load the trained model
with open('model/phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    features = extract_features_from_url(url)
    prediction = model.predict([features])[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
