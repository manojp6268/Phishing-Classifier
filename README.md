# 🔐 Phishing Website Classifier
 
> *A machine learning system that looks at a URL the way a security analyst would — and decides in milliseconds whether to trust it.*
 
[![Python](https://img.shields.io/badge/Python-3.7-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Deployed](https://img.shields.io/badge/Deployed-Heroku-430098?style=flat-square&logo=heroku&logoColor=white)](https://heroku.com)
 
---
 
## What this does
 
Phishing attacks rely on URLs that *look* legitimate but aren't. This project builds a classifier that extracts structural and lexical features directly from a URL — no page loading, no external API calls — and predicts whether it's a phishing attempt or legitimate.
 
The result: a live web application where you paste any URL and get an instant prediction.
 
---
 
## The approach
 
```
Raw URL
   │
   ▼
Feature Extraction (30+ signals)
   │  ├── URL length, depth, special character counts
   │  ├── Presence of IP address, @ symbol, redirects
   │  ├── HTTPS usage, domain age indicators
   │  └── Subdomain count, path structure
   │
   ▼
ML Classification
   │  ├── Support Vector Machine (SVM)
   │  └── Multi-Layer Perceptron (MLP Neural Network)
   │
   ▼
Flask Web App → Live Prediction
```
 
---
 
## Models trained
 
| Model | Type | Notes |
|-------|------|-------|
| `SVM.pickle` | Support Vector Machine | Strong on high-dimensional feature spaces |
| `MLP1.pickle` | Neural Network (MLP) | Non-linear decision boundaries |
 
Both models trained on a combined dataset of benign URLs (`Benign_list_big_final.csv`) and known phishing URLs (`online-valid.csv`).
 
---
 
## Project structure
 
```
Phishing-Classifier/
│
├── Feature Extraction.ipynb          ← Feature engineering exploration
├── Phishing Website Detection-       ← Model training & evaluation
│   Models & Training.ipynb
│
├── feature.py                        ← Feature extraction logic
├── app.py                            ← Flask application entry point
├── main.py                           ← Core prediction pipeline
│
├── SVM.pickle                        ← Trained SVM model
├── MLP1.pickle                       ← Trained MLP model
│
├── templates/                        ← HTML frontend
├── static/                           ← CSS/JS assets
│
├── legitimate_FE.csv                 ← Feature-engineered legitimate URLs
├── phishing_FE.csv                   ← Feature-engineered phishing URLs
├── urldata_FE.csv                    ← Combined dataset
│
└── requirements.txt
```
 
---
 
## Run it locally
 
**Step 1 — Clone the repo**
```bash
git clone https://github.com/manojp6268/Phishing-Classifier.git
cd Phishing-Classifier
```
 
**Step 2 — Create and activate environment**
```bash
# Create environment
conda create -n phishing-classifier python==3.7
 
# Activate
conda activate phishing-classifier          # Windows
source activate phishing-classifier         # Mac/Linux
```
 
**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```
 
**Step 4 — Run the app**
```bash
python app.py
```
 
Open your browser at `http://localhost:5000` and paste any URL to classify it.
 
> **Tip:** Copy URLs directly from your browser's address bar rather than typing them manually for best accuracy.
 
---
 
## Tech stack
 
- **Python 3.7** — core language
- **Scikit-learn** — SVM and MLP model training
- **Pandas / NumPy** — data processing and feature engineering
- **Flask** — web application framework
- **Heroku** — deployment platform
- **Jupyter Notebooks** — exploration and model training
---
 
## Background
 
This project originated from published research:
 
> *"Detection and Classification of Phishing Websites"* — Manoj P. et al. (2021)
> Applied ML classifiers with feature engineering to identify fraudulent web patterns at high accuracy.
 
The classifier in this repo is the working implementation of that research, taken from paper to production.
 
---
 
## Author
 
**Manoj Prakash** — Data Scientist & AI/ML Engineer
Currently pursuing M.Sc. Data Science @ Universität Trier, Germany.
Previously Software Developer II @ Oracle Cerner Healthcare.
 
(https://linkedin.com/in/manoj-p-a95b7b1a2)
 
---
 
*Contributions, suggestions, and forks are welcome. Happy learning.*
