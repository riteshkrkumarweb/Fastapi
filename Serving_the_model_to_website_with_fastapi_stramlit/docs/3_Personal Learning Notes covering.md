# Personal Learning Notes

This section explains all concepts used in the Insurance Premium Tier Prediction System project.

---

# FastAPI

## What is FastAPI?

FastAPI is a modern Python web framework used for building APIs.

It is designed for:

* High Performance
* Automatic Validation
* Automatic Documentation
* Easy Model Deployment

---

## Used In Project

```python
from fastapi import FastAPI

app = FastAPI()
```

---

## Purpose In This Project

* Create API Server
* Receive User Data
* Validate Requests
* Perform Predictions
* Return Results

---

# FastAPI Route Decorator

## What is a Route?

A route connects a URL to a Python function.

---

## Used In Project

```python
@app.post('/predict')
```

---

## Meaning

When a user sends a POST request to:

```text
/predict
```

FastAPI executes:

```python
def predict_user():
```

---

# POST Method

## What is POST?

POST is used to send data from the client to the server.

---

## Used In Project

Frontend sends:

```json
{
  "age":30,
  "weight":70
}
```

to the backend.

---

## Why POST?

Because the user is sending data for prediction.

---

# Pydantic

## What is Pydantic?

Pydantic validates incoming data automatically.

---

## Used In Project

```python
class UserInput(BaseModel):
```

---

## Benefits

* Data Validation
* Type Conversion
* Error Handling
* Automatic Documentation

---

# BaseModel

## What is BaseModel?

BaseModel is the foundation of every Pydantic model.

---

## Used In Project

```python
class UserInput(BaseModel):
```

---

## Purpose

Defines the structure of API input data.

---

# Annotated

## What is Annotated?

Annotated combines:

* Data Type
* Validation Rules

into a single declaration.

---

## Used In Project

```python
age: Annotated[
    int,
    Field(...)
]
```

---

## Benefits

* Better Validation
* Better Documentation
* Cleaner Code

---

# Field()

## What is Field()?

Field adds validation and metadata.

---

## Syntax

```python
Field(
    ...,
    gt=0,
    lt=120
)
```

---

## Used In Project

```python
age: Annotated[
    int,
    Field(
        ...,
        gt=0,
        lt=120
    )
]
```

---

## Validation Rules

### gt

Greater Than

```python
gt=0
```

Meaning:

```text
Age > 0
```

---

### lt

Less Than

```python
lt=120
```

Meaning:

```text
Age < 120
```

---

# Literal

## What is Literal?

Restricts values to predefined options.

---

## Used In Project

```python
Literal[
    'retired',
    'freelancer',
    'student',
    'government_job',
    'business_owner',
    'unemployed',
    'private_job'
]
```

---

## Purpose

Prevent invalid occupations.

---

## Valid Values

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

## Invalid Value

```text
doctor
```

Validation fails.

---

# computed_field()

## What is computed_field()?

Creates fields automatically.

The client does not send them.

Pydantic generates them.

---

## Used In Project

```python
@computed_field
@property
def bmi(self):
```

---

## Generated Fields

* bmi
* lifestyle_risk
* age_group

---

# BMI Calculation

## Formula

```text
BMI = Weight / Height²
```

---

## Example

```text
Weight = 70

Height = 1.75
```

Calculation:

```text
70 / (1.75 × 1.75)

BMI = 22.86
```

---

## Purpose

Represents health condition.

---

# Lifestyle Risk

## Purpose

Determine risk level.

---

## Logic

```python
if smoker and bmi > 30:
```

Result:

```text
high
```

---

## Categories

* low
* medium
* high

---

# Age Group

## Purpose

Convert numeric age into categories.

---

## Categories

### Young

```text
Age < 25
```

---

### Adult

```text
25 - 44
```

---

### Middle Aged

```text
45 - 59
```

---

### Senior

```text
60+
```

---

# Property Decorator

## What is @property?

Allows a method to behave like an attribute.

---

## Example

Without Property:

```python
obj.bmi()
```

With Property:

```python
obj.bmi
```

---

## Used In Project

```python
@property
```

for:

* bmi
* lifestyle_risk
* age_group
* city_tier

---

# City Tier Mapping

## Purpose

Convert city names into numerical categories.

---

## Tier 1

Examples:

```text
Mumbai
Delhi
Bangalore
Chennai
```

Returns:

```text
1
```

---

## Tier 2

Examples:

```text
Lucknow
Patna
Ranchi
Jaipur
```

Returns:

```text
2
```

---

## Tier 3

Any city not present in the lists.

Returns:

```text
3
```

---

# Pickle

## What is Pickle?

Pickle is Python's serialization library.

Used for saving and loading machine learning models.

---

# Serialization

## Meaning

Convert Python object into a file.

Example:

```python
model
```

becomes:

```text
model.pkl
```

---

# Deserialization

## Meaning

Load saved file back into memory.

---

## Used In Project

```python
with open(
    'model.pkl',
    'rb'
) as f:

    model = pickle.load(f)
```

---

## Workflow

```text
model.pkl
      │
      ▼
pickle.load()
      │
      ▼
Random Forest Model
```

---

# Random Forest

## What is Random Forest?

Random Forest is an ensemble learning algorithm.

It combines multiple decision trees.

---

## Benefits

* High Accuracy
* Handles Nonlinear Data
* Less Overfitting
* Works Well With Mixed Features

---

## Used For

Predicting:

```text
Insurance Premium Tier
```

---

# Pandas

## What is Pandas?

Pandas is a data manipulation library.

---

## Used In Project

```python
import pandas as pd
```

---

# DataFrame

## What is DataFrame?

A tabular data structure.

Rows and Columns.

---

## Used In Project

```python
input_df = pd.DataFrame(...)
```

---

## Why Needed?

Model was trained on tabular data.

Prediction input must have the same structure.

---

# Model Serving

## What is Model Serving?

Making a trained machine learning model available through an API.

---

## Workflow

```text
Trained Model
      │
      ▼
FastAPI
      │
      ▼
API Endpoint
      │
      ▼
Prediction
```

---

# JSONResponse

## What is JSONResponse?

Returns custom JSON responses.

---

## Used In Project

```python
return JSONResponse(
    status_code=200,
    content={}
)
```

---

## Purpose

Return prediction results.

---

# Streamlit

## What is Streamlit?

Streamlit is a Python framework for creating web applications.

---

## Purpose In Project

* User Interface
* Input Forms
* Result Display

---

# st.number_input()

## Purpose

Accept numeric values.

---

## Used For

* Age
* Weight
* Height
* Income

---

# st.text_input()

## Purpose

Accept text values.

---

## Used For

* City

---

# st.selectbox()

## Purpose

Create dropdown selections.

---

## Used For

* Smoker Status
* Occupation

---

# st.button()

## Purpose

Trigger prediction request.

---

## Used In Project

```python
if st.button(
    "Predict Premium Category"
)
```

---

# requests Module

## Purpose

Communicate with APIs.

---

## Used In Project

```python
requests.post()
```

---

## Workflow

```text
Frontend
    │
    ▼
POST Request
    │
    ▼
FastAPI
    │
    ▼
Response
```

---

# API Communication

## Request

Frontend sends:

```json
{
  "age":30,
  "weight":70,
  "height":1.75,
  "income_lpa":10,
  "smoker":false,
  "city":"Mumbai",
  "occupation":"private_job"
}
```

---

## Response

```json
{
  "predicted_category":"Medium"
}
```

---

# End-to-End Project Flow

```text
User
 │
 ▼
Streamlit
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
Pydantic Validation
 │
 ▼
Feature Engineering
 │
 ▼
Pandas DataFrame
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
```

---

# Key Concepts Learned

* FastAPI
* Route Decorators
* POST Requests
* Pydantic
* BaseModel
* Annotated
* Field
* Literal
* computed_field
* Property Decorator
* Feature Engineering
* City Tier Mapping
* Pickle
* Serialization
* Deserialization
* Random Forest
* Pandas DataFrame
* Model Serving
* JSONResponse
* Streamlit
* API Communication
* requests.post()
* End-to-End ML Deployment
