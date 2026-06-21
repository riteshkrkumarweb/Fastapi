# Insurance Premium Tier Prediction System

A Machine Learning deployment project that predicts an individual's insurance premium tier based on health, lifestyle, demographic, and financial information. The application uses a trained Random Forest model served through FastAPI and accessed through a Streamlit web interface.

## Author

**Ritesh Kumar**

---

## Features

* Predicts Insurance Premium Tier
* FastAPI Backend API
* Streamlit Frontend Application
* Pydantic Data Validation
* Automatic BMI Calculation
* Automatic Lifestyle Risk Assessment
* Automatic Age Group Classification
* City Tier Mapping
* Real-Time Predictions
* Random Forest Machine Learning Model

---

## Technology Stack

* Python
* FastAPI
* Streamlit
* Pandas
* Pydantic
* Scikit-Learn
* Pickle

---

## Project Structure

```text
Serving_ML_Models/
│
├── main.py
├── frontend.py
├── model.pkl
├── requirement.txt
└── myvenv/
```

---

## Application Workflow

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
Data Validation
 │
 ▼
Feature Engineering
 │
 ▼
Random Forest Model
 │
 ▼
Prediction
 │
 ▼
Result Display
```

---

## Input Features

* Age
* Weight
* Height
* Income (LPA)
* Smoking Status
* City
* Occupation

---

## Generated Features

The application automatically generates:

* BMI
* Lifestyle Risk
* Age Group
* City Tier

---

## Prediction Classes

The model predicts one of the following categories:

* Low
* Medium
* High

---

## Installation

### Create Virtual Environment

```bash
python -m venv myvenv
```

### Activate Virtual Environment

```bash
myvenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirement.txt
```

---

## Run FastAPI Backend

```bash
fastapi dev main.py --port 8001
```

Backend URL:

```text
http://127.0.0.1:8001
```

Swagger Documentation:

```text
http://127.0.0.1:8001/docs
```

---

## Run Streamlit Frontend

```bash
streamlit run frontend.py --server.port 8000
```

Frontend URL:

```text
http://localhost:8000
```

---

## Example Request

```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 12,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

---

## Example Response

```json
{
  "predicted_category": "Medium"
}
```

---

## Learning Outcomes

* Machine Learning Model Deployment
* FastAPI API Development
* Streamlit Frontend Development
* Pydantic Validation
* Feature Engineering
* Model Serialization using Pickle
* API Integration
* Real-Time Prediction Systems

---

## Future Improvements

* Docker Deployment
* Cloud Hosting
* User Authentication
* Batch Predictions
* Prediction History
* Monitoring Dashboard

---

### Developed by Ritesh Kumar
