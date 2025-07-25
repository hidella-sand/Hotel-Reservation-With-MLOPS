# 🏨 Hotel Reservation Cancellation Prediction (MLOps Project)

[![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue)](https://mlflow.org/)
[![Dockerized](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/Jenkins-CI--Ready-green)](https://www.jenkins.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

> An end-to-end MLOps pipeline that predicts hotel reservation cancellations using LightGBM, MLflow, Docker, and Jenkins. Deployed via a Flask web app and integrated with Google Cloud Storage.

---

## 📊 Project Overview

This project builds a robust machine learning pipeline to predict whether a hotel reservation will be canceled or not. The pipeline covers:

- **Cloud-based data ingestion**
- **Feature engineering & preprocessing**
- **Class balancing with SMOTE**
- **Model training with hyperparameter tuning**
- **MLflow tracking**
- **Web deployment via Flask**
- **Containerized deployment & CI/CD automation**

---

## ⚙️ Pipeline Architecture

```mermaid
graph TD;
    A[Google Cloud CSV] --> B[Data Ingestion]
    B --> C[Train/Test Split]
    C --> D[Preprocessing]
    D --> E[SMOTE Balancing]
    E --> F[Feature Selection]
    F --> G[LightGBM Training]
    G --> H[MLflow Logging]
    H --> I[Flask Web App]
    I --> J[Docker + Jenkins]

## 🧠 What's Happening Inside Each Stage

### 1️⃣ Data Ingestion
- Connects to a **Google Cloud Storage (GCS)** bucket.
- Downloads a CSV file (`raw.csv`) containing hotel reservation data.
- Splits it into **train** and **test** sets (based on `train_ratio` in `config.yaml`).

---

### 2️⃣ Data Preprocessing
- Drops irrelevant columns like `Booking_ID`.
- Applies **Label Encoding** for categorical columns.
- Corrects **skewness** in numerical features using `log1p()`.
- Removes **duplicates** and handles any **missing data**.

---

### 3️⃣ Class Balancing (SMOTE)
- The dataset is imbalanced (more non-cancellations than cancellations).
- Uses **SMOTE** to oversample the minority class and balance the training data.

---

### 4️⃣ Feature Selection
- Trains a **RandomForestClassifier** to compute feature importances.
- Selects the top **N features** (as defined in `config.yaml`) for training.
- Helps reduce **noise**, **dimensionality**, and **overfitting**.

---

### 5️⃣ Model Training
- Trains a **LightGBM** classifier for fast, efficient gradient boosting.
- Applies **RandomizedSearchCV** to tune:
  - `n_estimators`, `max_depth`, `learning_rate`, `num_leaves`, etc.
- Uses the balanced and feature-selected dataset.

---

### 6️⃣ MLflow Logging
- Automatically logs:
  - Model parameters
  - Metrics (accuracy, precision, recall, F1)
  - Train/test data artifacts
- Enables **experiment tracking**, **comparison**, and **model versioning**.

---

### 7️⃣ Web App Deployment
- A responsive **Flask app** allows users to input reservation data and receive predictions (cancellation or not).
- Styled using a custom **modern CSS design** (`style.css`).
- Loads the model using `joblib` and performs **real-time inference**.

---

### 8️⃣ Docker + Jenkins
- A **Dockerfile** packages the entire app for consistent environment deployment.
- `Jenkinsfile` supports **Continuous Integration and Delivery (CI/CD)**:
  - **Build → Test → Train → Deploy**

---

## 👨‍💻 Author

**Sandeep Hidellarachchi**  
🎓 Machine Learning Engineer | 🇩🇪 Based in Germany  
📧 s.hidellarachchi.de@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sandeephidella/) | [GitHub](https://github.com/hidella-sand)
