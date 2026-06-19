# Advanced & Related Concepts

This section covers important concepts related to FastAPI, Machine Learning Deployment, and Streamlit that were not directly implemented but are important for production-grade applications and interviews.

---

# Uvicorn

## What is Uvicorn?

Uvicorn is an ASGI server used to run FastAPI applications.

FastAPI itself does not run the application.

Uvicorn serves the application to clients.

---

## Example

```bash id="9v7n1x"
uvicorn main:app --reload
```

---

## Purpose

* Runs FastAPI application
* Handles incoming requests
* Sends responses back to clients

---

## Workflow

```text id="tckm3d"
Client
  │
  ▼
Uvicorn
  │
  ▼
FastAPI
  │
  ▼
Response
```

---

# ASGI

## What is ASGI?

ASGI stands for:

```text id="xy8c1v"
Asynchronous Server Gateway Interface
```

---

## Purpose

Provides communication between:

* Web Server
* Python Application

---

## Why FastAPI Uses ASGI

Benefits:

* Faster Performance
* Async Support
* Better Scalability

---

# Swagger Documentation

## What is Swagger?

FastAPI automatically generates API documentation.

---

## URL

```text id="m4ha3j"
http://127.0.0.1:8001/docs
```

---

## Benefits

* API Testing
* Request Validation
* Endpoint Documentation
* Interactive Interface

---

# ReDoc Documentation

## URL

```text id="zgixw4"
http://127.0.0.1:8001/redoc
```

---

## Purpose

Alternative API documentation interface.

---

# response_model

## What is response_model?

Defines the structure of data returned by an endpoint.

---

## Example

```python id="e6yzv7"
@app.post(
    '/predict',
    response_model=PredictionResponse
)
```

---

## Benefits

* Response Validation
* Better Documentation
* Type Safety

---

# Body()

## What is Body()?

Used to configure request body parameters.

---

## Example

```python id="gn3uw4"
from fastapi import Body
```

```python id="hrv4j7"
age:int = Body(
    ...,
    gt=0
)
```

---

## Benefits

* Additional Validation
* Better Swagger Documentation

---

# field_validator()

## What is field_validator()?

Validates a single field.

---

## Example

```python id="6f2jyb"
from pydantic import field_validator
```

```python id="pv2p1k"
@field_validator('city')
```

---

## Example Use Case

```python id="vl2z8r"
@field_validator('city')
@classmethod
def city_validation(
    cls,
    value
):
    return value.title()
```

---

## Purpose

* Data Cleaning
* Custom Validation
* Input Standardization

---

# model_validator()

## What is model_validator()?

Validates multiple fields together.

---

## Example

```python id="m0s1fw"
@model_validator(
    mode='after'
)
```

---

## Example Use Case

```python id="6xj3sz"
if self.age < 18 and self.income > 20:
```

Custom business validation.

---

# mode='before'

Runs before Pydantic converts data types.

---

## Example

Input:

```python id="vgqg8i"
{
    "age":"30"
}
```

Value is still:

```python id="2aj0pb"
"30"
```

String.

---

# mode='after'

Runs after conversion.

---

Input:

```python id="k3ljw7"
{
    "age":"30"
}
```

Converted to:

```python id="7m0yra"
30
```

Integer.

---

# Dependency Injection

## What is Dependency Injection?

FastAPI's system for sharing reusable logic.

---

## Using Depends()

```python id="jtpzdc"
from fastapi import Depends
```

---

## Example

```python id="m6htcz"
def verify_user():
    pass

@app.get('/')
def home(
    user=Depends(
        verify_user
    )
):
    pass
```

---

## Common Uses

* Authentication
* Database Connections
* Logging
* Configuration

---

# Production Deployment

## Current Deployment

Your project currently runs locally.

---

## Local Architecture

```text id="b7k6fn"
Streamlit
    │
    ▼
FastAPI
    │
    ▼
Random Forest
```

---

# Production Architecture

```text id="1l0wrx"
Users
   │
   ▼
Nginx
   │
   ▼
FastAPI
   │
   ▼
Random Forest
```

---

# Docker

## What is Docker?

Docker packages the application into containers.

---

## Benefits

* Easy Deployment
* Environment Consistency
* Cloud Ready

---

# Environment Variables

## Purpose

Store configuration securely.

---

## Example

Instead of:

```python id="ytu2mx"
API_URL = "http://127.0.0.1"
```

Use:

```python id="d3gk0v"
os.getenv()
```

---

## Benefits

* Security
* Flexibility
* Better Deployment

---

# Logging

## What is Logging?

Recording application activity.

---

## Example

```python id="c9qvlr"
import logging
```

---

## Use Cases

* Debugging
* Monitoring
* Error Tracking

---

# Exception Handling

## Current State

Frontend handles:

* API Errors
* Connection Errors

---

## Advanced Error Handling

Backend can also handle:

* Invalid Model Inputs
* Server Failures
* Missing Files
* Model Loading Errors

---

# Model Loading Best Practice

## Current Approach

```python id="l1g4qf"
model.pkl
```

loads once at startup.

---

## Why Good?

Model is not loaded for every request.

Benefits:

* Faster Predictions
* Better Performance

---

# Batch Prediction

## Current State

One user prediction at a time.

---

## Future Version

Accept multiple records.

Example:

```json id="7s8i1n"
[
    {...},
    {...},
    {...}
]
```

---

## Benefits

* Faster Processing
* Enterprise Usage

---

# Model Monitoring

## What is Model Monitoring?

Tracking model performance after deployment.

---

## Checks

* Prediction Accuracy
* Response Time
* Data Drift
* Model Drift

---

# Security Improvements

## Future Enhancements

* API Key Authentication
* JWT Authentication
* Rate Limiting
* Input Sanitization

---

# Deployment Options

## Render

Good for beginners.

---

## Railway

Simple deployment.

---

## AWS

Enterprise-level deployment.

---

## Azure

Microsoft Cloud Platform.

---

## Google Cloud

Production ML deployments.

---

# Interview Questions

## FastAPI

* What is FastAPI?
* Why is FastAPI faster than Flask?
* What is ASGI?
* What is Uvicorn?
* What is Dependency Injection?
* What is response_model?
* Difference between Path and Query?

---

## Pydantic

* What is BaseModel?
* What is Field()?
* What is Annotated?
* What is Literal?
* What is computed_field()?
* What is field_validator()?
* What is model_validator()?
* Difference between before and after mode?

---

## Machine Learning Deployment

* What is model serving?
* Why use Pickle?
* What is serialization?
* What is deserialization?
* Why use FastAPI for ML deployment?
* Why convert data into a DataFrame?
* Why perform feature engineering before prediction?

---

## Streamlit

* What is Streamlit?
* Difference between Streamlit and FastAPI?
* How does Streamlit communicate with APIs?
* Why use requests.post()?

---

# Project Improvements You Can Add Next

* Model Training Pipeline
* Docker Support
* Authentication
* Batch Prediction
* Database Storage
* Prediction History
* Cloud Deployment
* Logging System
* CI/CD Pipeline
* Monitoring Dashboard

---

# Final Learning Outcomes

* FastAPI API Development
* Streamlit Frontend Development
* Machine Learning Model Serving
* Random Forest Deployment
* Pickle Serialization
* Pydantic Validation
* Feature Engineering
* REST APIs
* API Communication
* Swagger Documentation
* ASGI Architecture
* Production Deployment Concepts
* End-to-End ML Application Development
