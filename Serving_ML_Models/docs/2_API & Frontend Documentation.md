# API & Frontend Documentation

This section explains how the FastAPI backend and Streamlit frontend communicate to generate insurance premium predictions.

---

# Backend API Documentation

## API Endpoint

```http
POST /predict
```

---

## Purpose

The endpoint accepts user information, performs feature engineering, sends processed data to the Random Forest model, and returns the predicted insurance premium tier.

---

# Endpoint URL

Local Development:

```text
http://127.0.0.1:8001/predict
```

---

# Request Flow

```text
User Input
     │
     ▼
Streamlit Frontend
     │
     ▼
POST Request
     │
     ▼
FastAPI Endpoint
     │
     ▼
Pydantic Validation
     │
     ▼
Feature Engineering
     │
     ▼
Random Forest Prediction
     │
     ▼
JSON Response
     │
     ▼
Frontend Display
```

---

# Request Body Schema

## UserInput Model

The API expects data in the following structure:

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

# Input Fields

## age

Type:

```python
int
```

Validation:

```python
gt=0
lt=120
```

Purpose:

* User age

Example:

```json
{
    "age": 30
}
```

---

## weight

Type:

```python
float
```

Validation:

```python
gt=0
```

Purpose:

* Weight in kilograms

Example:

```json
{
    "weight": 70
}
```

---

## height

Type:

```python
float
```

Validation:

```python
gt=0
lt=2.5
```

Purpose:

* Height in meters

Example:

```json
{
    "height": 1.75
}
```

---

## income_lpa

Type:

```python
float
```

Validation:

```python
gt=0
```

Purpose:

* Annual income in Lakhs Per Annum

Example:

```json
{
    "income_lpa": 12
}
```

---

## smoker

Type:

```python
bool
```

Purpose:

* Smoking status

Values:

```python
True
False
```

---

## city

Type:

```python
str
```

Purpose:

* User city

Example:

```json
{
    "city":"Mumbai"
}
```

---

## occupation

Type:

```python
Literal
```

Allowed Values:

```python
retired
freelancer
student
government_job
business_owner
unemployed
private_job
```

---

# Feature Engineering Layer

Before prediction, the system automatically creates additional features.

---

## Generated Feature 1

### BMI

Formula:

```text
BMI = Weight / Height²
```

Example:

```text
Weight = 70

Height = 1.75

BMI = 22.86
```

---

## Generated Feature 2

### Lifestyle Risk

Generated using:

* Smoking Status
* BMI

Possible Values:

```text
low
medium
high
```

---

## Generated Feature 3

### Age Group

Possible Values:

```text
young
adult
middle_aged
senior
```

---

## Generated Feature 4

### City Tier

Possible Values:

```text
1
2
3
```

Logic:

```text
Tier 1 Cities
      │
      ▼
      1
```

```text
Tier 2 Cities
      │
      ▼
      2
```

```text
Other Cities
      │
      ▼
      3
```

---

# Model Input Structure

After feature engineering:

```python
{
    'bmi': 22.86,
    'age_group': 'adult',
    'lifestyle_risk': 'low',
    'city_tier': 1,
    'income_lpa': 12,
    'occupation': 'private_job'
}
```

---

# Pandas Transformation

The dictionary is converted into a DataFrame.

Structure:

```text
Rows = 1
Columns = 6
```

Purpose:

* Match model training format
* Prepare data for prediction

---

# Prediction Stage

The processed DataFrame is sent to:

```python
model.predict()
```

Random Forest returns:

```text
Low
```

or

```text
Medium
```

or

```text
High
```

---

# Success Response

Status Code:

```text
200 OK
```

Response:

```json
{
    "predicted_category":"Medium"
}
```

---

# Validation Errors

FastAPI automatically returns:

```text
422 Unprocessable Entity
```

Example:

```json
{
    "detail":[]
}
```

---

# Example Invalid Request

```json
{
    "age": -5
}
```

Reason:

```text
Age must be greater than zero
```

---

# Backend Workflow

```text
Request
   │
   ▼
Validation
   │
   ▼
Computed Fields
   │
   ▼
City Tier Mapping
   │
   ▼
DataFrame Creation
   │
   ▼
Random Forest
   │
   ▼
Prediction
   │
   ▼
JSON Response
```

---

# Streamlit Frontend Documentation

## Purpose

Provides a graphical interface for interacting with the prediction API.

---

# Frontend URL

```text
http://localhost:8000
```

---

# User Interface Components

## Age Input

Widget:

```python
st.number_input()
```

Purpose:

* Capture age

---

## Weight Input

Widget:

```python
st.number_input()
```

Purpose:

* Capture weight

---

## Height Input

Widget:

```python
st.number_input()
```

Purpose:

* Capture height

---

## Income Input

Widget:

```python
st.number_input()
```

Purpose:

* Capture annual income

---

## Smoker Selection

Widget:

```python
st.selectbox()
```

Options:

```python
True
False
```

---

## City Input

Widget:

```python
st.text_input()
```

Purpose:

* Enter city name

---

## Occupation Selection

Widget:

```python
st.selectbox()
```

Options:

```text
retired
freelancer
student
government_job
business_owner
unemployed
private_job
```

---

## Prediction Button

Widget:

```python
st.button()
```

Purpose:

* Trigger prediction request

---

# Frontend Workflow

```text
User Input
     │
     ▼
Collect Values
     │
     ▼
Create JSON
     │
     ▼
requests.post()
     │
     ▼
FastAPI
     │
     ▼
Prediction
     │
     ▼
Receive Response
     │
     ▼
Display Result
```

---

# API Communication

Request Method:

```python
requests.post()
```

Purpose:

* Send user data to FastAPI

---

# Result Display

Success:

```python
st.success()
```

Example:

```text
Predicted Insurance Premium Category: Medium
```

---

# Error Handling

## API Error

Displays:

```python
st.error()
```

Example:

```text
API Error: 422
```

---

## Connection Error

Occurs when FastAPI server is not running.

Message:

```text
Could not connect to the FastAPI server.
Make sure it's running.
```

---

# Footer Section

Displays:

```text
Developed by Ritesh Kumar
```

and

```text
© 2026 Ritesh Kumar | Insurance Premium Prediction App
```

---

# Complete Application Lifecycle

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Input Collection
 │
 ▼
POST Request
 │
 ▼
FastAPI
 │
 ▼
Validation
 │
 ▼
Feature Engineering
 │
 ▼
Random Forest
 │
 ▼
Prediction
 │
 ▼
JSON Response
 │
 ▼
Frontend Display
 │
 ▼
User Result
```
