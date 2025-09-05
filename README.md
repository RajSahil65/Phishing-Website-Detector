# 🛡️ Phishing URL Detection using Flask & Machine Learning

This project is a simple web-based application that detects whether a given URL is **legitimate** or **phishing** using a trained machine learning model.

## 📂 Project Structure
├── app.py # Flask app to serve the prediction API
├── feature_extraction.py # Functions to extract features from URLs
├── model.py # Script to train & save the phishing detection model
├── model/
│ └── phishing_model.pkl # Pre-trained ML model
├── templates/
│ └── index.html # Frontend (web UI)


## 🚀 Features
- Extracts basic URL-based features:
  - URL length
  - Count of '@'
  - Count of '-'
  - HTTPS check
- Uses **Random Forest Classifier** (dummy model for demo).
- Provides a **Flask API endpoint** (`/predict`) for predictions.
- Simple **web interface** (`index.html`).
