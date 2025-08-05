# 🌍 Life Expectancy Prediction with Decision Tree

This project is a **Flask-based web application** that predicts **Life Expectancy** using a **Decision Tree Regressor** trained on the `Life Expectancy Data.csv` dataset. Users can input various health, demographic, and economic factors to estimate life expectancy for better policy-making and health planning.

## 🚀 Features
- 🌳 Decision Tree Regressor for accurate life expectancy prediction
- 🧹 Data preprocessing and feature engineering
- 🌐 Flask web interface for easy user input
- 📊 Visualization of predictions and feature importance
- ☁️ Deployment-ready for platforms like Render, Heroku, or AWS

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS (Responsive UI)
- **Backend:** Flask (Python)
- **Machine Learning:** Decision Tree Regressor (Scikit-learn)
- **Visualization:** Matplotlib / Seaborn
- **Deployment:** Gunicorn, Render/Heroku

## 📂 Project Structure
```
life-expectancy-predictor/
│── app.py                 # Flask backend
│── model.ipynb             # Model training notebook
│── decision_tree_model.pkl # Saved Decision Tree model
│── scaler.pkl              # Data scaler
│── templates/
│     └── index.html        # Frontend HTML
│── static/
│     └── style.css         # Styling
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## ⚡ Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/life-expectancy-predictor.git
   cd life-expectancy-predictor
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask app**
   ```bash
   python app.py
   ```
4. **Access the app**
   Open your browser → `http://127.0.0.1:5000`

## 🧑‍⚕️ Usage
- Input health, demographic, and economic data
- Click **Predict** to get estimated life expectancy
- View model insights and important contributing features

## 🖼️ App Preview

<img width="1364" height="626" alt="Screenshot 2025-08-05 144000" src="https://github.com/user-attachments/assets/0eb5a75d-551a-411f-8866-df7db358bdab" />
