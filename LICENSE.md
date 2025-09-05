from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features_from_url

# Load the model
with open('model/phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features_from_url(url)
        result = model.predict([features])[0]
        if result==1:
            result= "  Does Not Look Secure  "
        else:
            result= " Looks Secure! "
        print("Extracted Features:", features)
        print("Prediction:", result)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
