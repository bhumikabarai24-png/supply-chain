# 📦 Supply Chain Delay Prediction

### AI-Powered Order Fulfillment Risk Prediction

An end-to-end Machine Learning project that predicts whether a supply chain order is likely to be **delayed or delivered on time**.

## 🚀 Live Demo

👉 https://supply-chain-8tacxbloycixrhu5pdtikg.streamlit.app/

## 💻 GitHub

👉 https://github.com/bhumikabarai24-png/supply-chain

## ✨ Features

- 🧹 Data Cleaning
- ⚙️ Data Preprocessing
- 📊 Exploratory Data Analysis
- 📈 Data Visualization
- 🤖 Machine Learning Model Training
- 🔍 Model Comparison & Evaluation
- 🎯 Delay Risk Prediction
- 🌐 Streamlit Deployment

## 🧠 Input Features

- Supplier Reliability Score
- Warehouse Inventory Level
- Order Quantity
- Shipping Distance
- Shipping Method
- Weather Condition
- Processing Time
- Order Priority
- Order Hour
- Order Day
- Order Month
- Day of Week

## 🤖 Machine Learning

The project uses a Scikit-learn pipeline with:

- StandardScaler
- OneHotEncoder
- Logistic Regression

The trained model is saved as:

```text
delay_model.pkl
🎯 Prediction
Result	Meaning
🟢 Low Risk	Order likely to be on time
🔴 High Risk	Order likely to be delayed

The application also displays the delay probability.

🛠️ Technologies
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit

📁 Project Structure
supply-chain/
│
├── app.py
├── delay_model.pkl
├── requirements.txt
├── README.md
└── .gitignor

👩‍💻 Author
Bhumika Barai

GitHub:
https://github.com/bhumikabarai24-png

⭐ If you like this project, consider giving it a star!
