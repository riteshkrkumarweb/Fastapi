# Insurance Premium Tier Prediction System

## Author

* Name: Ritesh Kumar
* Project Type: Machine Learning Model Serving
* Documentation Version: 1.0

---

# Project Overview

The Insurance Premium Tier Prediction System is an end-to-end Machine Learning deployment project that predicts the insurance premium tier of a user based on personal, health, lifestyle, demographic, and financial information.

The project combines:

* FastAPI for Backend API Development
* Streamlit for Frontend User Interface
* Random Forest Machine Learning Model
* Pydantic for Data Validation
* Pandas for Data Transformation
* Pickle for Model Serialization

The system accepts user information, performs feature engineering, sends the processed data to a trained Random Forest model, and predicts an insurance premium category.

---

# Prediction Objective

The goal of the system is to predict:

```text
Insurance Premium Tier
```

Possible Categories:

* Low
* Medium
* High

---

# Business Problem

Insurance companies often determine premium categories based on several risk factors.

Important factors include:

* Age
* Income
* Smoking Habit
* Occupation
* BMI
* Lifestyle Risk
* City Tier

The model automates this classification process.

---

# Project Features

* Machine Learning Model Deployment
* FastAPI REST API
* Streamlit Frontend
* Input Validation using Pydantic
* Automatic BMI Calculation
* Automatic Lifestyle Risk Assessment
* Automatic Age Group Classification
* Automatic City Tier Mapping
* Random Forest Prediction Engine
* Real-Time Predictions
* Interactive User Interface
* API Integration between FastAPI and Streamlit

---

# Technology Stack

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming Language |
| FastAPI       | Backend API          |
| Streamlit     | Frontend UI          |
| Pydantic      | Data Validation      |
| Pandas        | Data Processing      |
| Pickle        | Model Loading        |
| Random Forest | Prediction Model     |

---

# Project Structure

```text
Serving_ML_Models/
│
├── main.py
├── frontend.py
├── model.pkl
├── requirement.txt
├── myvenv/
├── docs/
└── __pycache__/
```

---

# File Description

## main.py

Contains:

* FastAPI Application
* Model Loading Logic
* Pydantic Validation
* Feature Engineering
* Prediction Endpoint

---

## frontend.py

Contains:

* Streamlit User Interface
* User Input Forms
* API Communication
* Result Display

---

## model.pkl

Contains:

* Trained Random Forest Model

Loaded using:

```python
pickle.load()
```

---

## requirement.txt

Contains:

* Project Dependencies

Examples:

* FastAPI
* Streamlit
* Pandas
* Pydantic
* Uvicorn
* Scikit-Learn

---

# System Architecture

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
Pydantic Validation
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
JSON Response
 │
 ▼
Frontend Display
```

---

# Complete Workflow

## Step 1

User opens Streamlit Application.

---

## Step 2

User enters:

* Age
* Weight
* Height
* Income
* Smoking Status
* City
* Occupation

---

## Step 3

Frontend collects user information.

---

## Step 4

Frontend sends POST request to:

```text
http://127.0.0.1:8001/predict
```

---

## Step 5

FastAPI receives request.

---

## Step 6

Pydantic validates incoming data.

Validation Examples:

* Age must be greater than 0
* Height must be less than 2.5 meters
* Income must be positive
* Occupation must match allowed values

---

## Step 7

Computed fields are generated automatically.

Generated Features:

* BMI
* Lifestyle Risk
* Age Group

---

## Step 8

City is converted into City Tier.

Tier Mapping:

```text
Tier 1
Tier 2
Tier 3
```

---

## Step 9

Processed features are converted into a Pandas DataFrame.

---

## Step 10

DataFrame is passed into the Random Forest Model.

---

## Step 11

Model predicts:

```text
Low
Medium
High
```

---

## Step 12

Prediction is returned as JSON.

---

## Step 13

Frontend displays prediction to user.

---

# Feature Engineering Pipeline

The project performs feature engineering at prediction time.

---

## BMI Generation

Formula:

```text
BMI = Weight / Height²
```

Example:

```text
Weight = 70 kg
Height = 1.75 m
```

Calculation:

```text
BMI = 70 / (1.75 × 1.75)

BMI = 22.86
```

Generated Automatically.

---

## Lifestyle Risk Generation

Logic:

```text
Smoker + High BMI
          │
          ▼
        High Risk
```

Categories:

* Low
* Medium
* High

---

## Age Group Generation

Categories:

* Young
* Adult
* Middle Aged
* Senior

Classification:

```text
Age < 25
      ▼
Young
```

```text
25 - 44
      ▼
Adult
```

```text
45 - 59
      ▼
Middle Aged
```

```text
60+
      ▼
Senior
```

---

## City Tier Generation

Categories:

* Tier 1
* Tier 2
* Tier 3

Purpose:

Convert city names into numerical representation.

Example:

```text
Mumbai
Delhi
Bangalore
```

Converted To:

```text
1
```

---

# Why Feature Engineering is Important

Machine Learning models understand numerical and structured information better than raw user inputs.

Feature engineering improves:

* Prediction Accuracy
* Data Consistency
* Model Performance
* Business Interpretation

---

# Model Loading Process

The trained model is loaded during application startup.

Workflow:

```text
Application Starts
        │
        ▼
Open model.pkl
        │
        ▼
pickle.load()
        │
        ▼
Random Forest Model
        │
        ▼
Ready For Prediction
```

---

# Backend Responsibilities

FastAPI handles:

* Request Processing
* Validation
* Feature Engineering
* Prediction
* Response Generation

---

# Frontend Responsibilities

Streamlit handles:

* User Interface
* Input Collection
* API Communication
* Displaying Results

---

# Project Setup

## Create Virtual Environment

```bash
python -m venv myvenv
```

---

## Activate Environment

Windows:

```bash
myvenv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirement.txt
```

---

# Running FastAPI Backend

Command:

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

# Running Streamlit Frontend

Command:

```bash
streamlit run frontend.py --server.port 8000
```

Frontend URL:

```text
http://localhost:8000
```

---

# Project Advantages

* Easy Deployment
* Clean Architecture
* Strong Validation Layer
* User-Friendly Interface
* Real-Time Predictions
* Modular Design
* Scalable Structure

---

# Known Limitations

* Single Prediction at a Time
* No User Authentication
* Model Retraining Not Included
* Local Deployment Only
* No Database Storage

---

# Future Improvements

* Batch Predictions
* Cloud Deployment
* Docker Integration
* Database Support
* Authentication System
* Model Monitoring
* CI/CD Pipeline
* Prediction History Storage

---

# Key Learning Outcomes

* Machine Learning Model Serving
* FastAPI Development
* Streamlit Development
* API Integration
* Pydantic Validation
* Feature Engineering
* Random Forest Deployment
* Pickle Serialization
* Request Handling
* Real-Time Prediction Systems
