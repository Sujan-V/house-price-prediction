# 🏠 AI House Price Prediction Web App

An advanced Machine Learning-powered web application that predicts real estate property prices using XGBoost Regression and Flask. The application provides real-time predictions, interactive analytics, AI-driven property insights, and a modern responsive dashboard UI.

---

## 🚀 Live Demo

🌐 Live Website:  https://house-price-prediction-0fq6.onrender.com/

---

# 📌 Features

✅ Real-time House Price Prediction  
✅ XGBoost Machine Learning Model  
✅ Interactive Analytics Dashboard  
✅ Responsive Modern UI  
✅ AI-generated Property Insights  
✅ Data Preprocessing & Feature Scaling  
✅ Flask Backend Integration  
✅ Chart Visualization using Chart.js  
✅ Deployment Ready Architecture  

---

# 🧠 Machine Learning Model

The project uses:

- **XGBoost Regressor**
- Feature Scaling using **StandardScaler**
- Optimized feature selection
- Train-Test split validation

### 📊 Model Performance

- Achieved high R² score on the India House Price Dataset.
- Improved prediction accuracy using feature engineering and preprocessing techniques.

---

# 🛠 Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend & ML |
| Flask | Web Framework |
| XGBoost | Machine Learning |
| Scikit-Learn | Preprocessing |
| Pandas & NumPy | Data Handling |
| HTML/CSS/JavaScript | Frontend |
| Chart.js | Data Visualization |
| Gunicorn | Production Server |

---

# 📂 Project Structure

```bash
house-price-prediction/
│
├── dataset/
│   └── House Price India.csv
│
├── model/
│   ├── house_price_model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       └── house-bg.jpg
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── runtime.txt
└── Procfile
````

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd house-price-prediction
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Train Machine Learning Model

Run:

```bash
python train_model.py
```

This generates:

```bash
model/
├── house_price_model.pkl
├── scaler.pkl
└── columns.pkl
```

---

# ▶️ Run Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# ☁️ Deployment

The application can be deployed using:

* Render
* Railway
* Vercel
* Heroku

### Production Start Command

```bash
gunicorn app:app
```

---

# 📊 Dataset

Dataset used:

**House Prices India Dataset**

Source:
[https://www.kaggle.com/datasets/sukhmandeepsinghbrar/house-prices-india](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/house-prices-india)

---

# 🔥 Future Improvements

* Google Maps Integration
* Property Recommendation System
* User Authentication
* MongoDB Database Integration
* Prediction History
* AI Chatbot Assistant
* PDF Report Generation
* Dark/Light Theme Toggle
* Real Estate Market Analytics

---

# 📸 Screenshots

## Home Page

<img width="1365" height="645" alt="image" src="https://github.com/user-attachments/assets/33193a05-19d8-4069-9ce0-5b5c5d4887c8" />


## Prediction Dashboard

<img width="1253" height="556" alt="image" src="https://github.com/user-attachments/assets/37510bd6-8fe5-4d86-8a9b-df8ce8ed7d1d" />

---
# 👨‍💻 Author

**Sujan V**

* LinkedIn: https://www.linkedin.com/in/sujan-v/
* GitHub: https://github.com/Sujan-V

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

