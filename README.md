# 🛡️ Credit Card Fraud Detection using Machine Learning

A Machine Learning project that detects potentially fraudulent credit card transactions using classification algorithms and provides an interactive **Streamlit web application** for real-time fraud prediction.

The project uses anonymized transaction features, performs data preprocessing and exploratory analysis, compares multiple classification models, and deploys the selected **Random Forest Classifier** for fraud prediction.

## 🚀 Live Demo

👉 **[Try FraudGuard AI](https://credit-card-fraud-detection-ml-ibvaas8srypq7kyleecexn.streamlit.app/)**

---

## 📌 Overview

Credit card fraud detection is a **binary classification problem** where the goal is to distinguish between:

* **0 → Legitimate Transaction**
* **1 → Fraudulent Transaction**

This project analyzes transaction data containing anonymized features (`V1`–`V28`), transaction time, and transaction amount.

After evaluating multiple machine learning models, **Random Forest** was selected as the final model based on its overall classification performance.

The trained model is serialized using **Joblib** and integrated into a **Streamlit application** where users can enter transaction details and receive a fraud prediction.

---

## 🎯 Project Objectives

* Understand and analyze credit card transaction data
* Perform data cleaning and preprocessing
* Conduct Exploratory Data Analysis (EDA)
* Perform feature engineering
* Train multiple classification models
* Compare model performance
* Select the best-performing model
* Serialize the trained model using Joblib
* Build an interactive Streamlit application
* Generate fraud predictions and probability scores

---

## 📊 Dataset

The project uses a credit card fraud detection dataset containing anonymized transaction information.

### Features

| Feature      | Description                                    |
| ------------ | ---------------------------------------------- |
| `Time`       | Number of seconds elapsed between transactions |
| `V1` – `V28` | Anonymized transaction features                |
| `Amount`     | Transaction amount                             |
| `Class`      | Target variable                                |

### Target Variable

```text
0 → Legitimate Transaction
1 → Fraudulent Transaction
```

> **Note:** The `V1`–`V28` features are anonymized numerical variables from the original dataset.

---

## 🔄 Machine Learning Workflow

```text
                 Credit Card Dataset
                         │
                         ▼
                Data Understanding
                         │
                         ▼
                  Data Cleaning
                         │
                         ▼
               Exploratory Data Analysis
                         │
                         ▼
                 Feature Engineering
                         │
                         ▼
                  Train-Test Split
                         │
                         ▼
                  Model Training
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
        Logistic      Random      Gradient
        Regression    Forest      Boosting
             │           │           │
             └───────────┼───────────┘
                         ▼
                  Model Evaluation
                         │
                         ▼
                  Model Comparison
                         │
                         ▼
                 Random Forest
                    Selection
                         │
                         ▼
                  Model Serialization
                         │
                         ▼
                Streamlit Application
                         │
                         ▼
                 Fraud Prediction
```

---

## 🤖 Machine Learning Models

### 1. Logistic Regression

Used as a baseline classification model to establish a reference point for model performance.

### 2. Random Forest

An ensemble learning algorithm that combines multiple decision trees to improve classification performance and robustness.

**Selected as the final model for deployment.**

### 3. Gradient Boosting

A boosting-based ensemble algorithm used to compare performance against Logistic Regression and Random Forest.

---

## 📈 Model Performance

The final **Random Forest Classifier** achieved the following results:

| Metric        |      Score |
| ------------- | ---------: |
| **Precision** | **90.59%** |
| **Recall**    | **78.57%** |
| **F1 Score**  | **84.15%** |

### Precision

Precision indicates how many transactions predicted as fraudulent were actually fraudulent.

### Recall

Recall indicates how many actual fraudulent transactions were successfully detected by the model.

### F1 Score

F1 Score provides a balance between precision and recall and is particularly useful when evaluating classification problems with imbalanced classes.

---

## 🖥️ Streamlit Application

The trained Random Forest model is integrated into a Streamlit application.

Users can provide transaction information such as:

* Transaction time
* Transaction amount
* `V1` – `V28` transaction features

The application then returns:

* **Fraud / Legitimate prediction**
* **Fraud probability**
* Prediction result
* Transaction analysis

### Example Output

```text
Prediction: FRAUD

Fraud Probability: 97%
```

or

```text
Prediction: LEGITIMATE

Fraud Probability: Low
```

---

## 🧪 Model Validation

The trained model was additionally tested using an actual fraudulent transaction from the dataset.

Example prediction:

```text
Prediction: 1
Fraud Probability: ~0.97
```

Where:

```text
1 → Fraudulent Transaction
0 → Legitimate Transaction
```

This validation demonstrates that the trained model can identify transaction patterns associated with fraudulent activity.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Logistic Regression
* Random Forest
* Gradient Boosting

### Model Deployment

* Streamlit

### Model Serialization

* Joblib

### Development Environment

* Jupyter Notebook

---

## 📁 Project Structure

```text
credit-card-fraud-detection-ml/
│
├── app/
│   └── app.py
│
├── data/
│   └── dataset.csv
│
├── models/
│   ├── random_forest_fraud_model.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

> If the dataset is not included in the repository because of file size or privacy considerations, the `data/` folder can be left empty or documented separately.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/madhava-raju/credit-card-fraud-detection-ml.git
```

### 2. Navigate to the Project

```bash
cd credit-card-fraud-detection-ml
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

From the project root directory, run:

```bash
streamlit run app/app.py
```

The Streamlit application will open automatically in your default browser.

---

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

* Binary Classification
* Data Preprocessing
* Exploratory Data Analysis
* Feature Engineering
* Train-Test Splitting
* Model Training
* Model Comparison
* Random Forest
* Logistic Regression
* Gradient Boosting
* Precision, Recall & F1 Score
* Model Serialization using Joblib
* Streamlit Application Development
* Machine Learning Model Deployment

---

## 🔮 Future Improvements

Potential improvements for the project include:

* Handling class imbalance using techniques such as SMOTE
* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
* Adding ROC-AUC and Precision-Recall curves
* Adding a confusion matrix to the Streamlit dashboard
* Improving the Streamlit UI
* Adding batch prediction through CSV upload
* Deploying the application using Streamlit Community Cloud
* Adding model explainability using SHAP
* Implementing real-time transaction monitoring

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes only**.

The predictions generated by this application should not be used as the sole basis for real-world financial, security, or fraud-related decisions.

---

## 👨‍💻 Author

### Madhava Raju Maddimani

**B.Tech – Electronics and Communication Engineering**

**Areas of Interest**

* Data Analytics
* Machine Learning
* Python
* SQL
* Generative AI

---
