# FastAPI Patient Management System

## Project Overview

The FastAPI Patient Management System is a REST API application built using FastAPI and Pydantic. The project performs complete CRUD (Create, Read, Update, Delete) operations on patient records stored in a JSON file.

The application demonstrates:

* FastAPI route creation
* Request validation using Pydantic
* Path and Query parameter validation
* JSON file handling
* Custom error handling
* Computed fields
* Partial updates
* Structured API responses

The project follows a simple file-based database approach where patient information is stored inside `patients.json`.

---

# Project Features

* Create new patient records
* Retrieve all patients
* Retrieve a patient using Patient ID
* Sort patients based on different fields
* Update existing patient information
* Delete patient records
* Automatic BMI calculation
* Automatic health verdict generation
* Input validation using Pydantic
* Error handling using HTTPException
* JSON-based persistence

---

# Technology Stack

| Technology | Purpose          |
| ---------- | ---------------- |
| FastAPI    | API Framework    |
| Pydantic   | Data Validation  |
| JSON       | Data Storage     |
| Python     | Backend Language |
| Uvicorn    | ASGI Server      |

---

# Project Structure

```text
project/
│
├── main.py
├── patients.json
│
└── requirements.txt
```

### main.py

Contains:

* API routes
* Validation models
* CRUD operations
* Utility functions

### patients.json

Stores all patient records.

Example:

```json
{
    "P001": {
        "name": "Ritesh",
        "age": 22,
        "city": "Varanasi"
    }
}
```

---

# Application Flow

```text
Client
   │
   ▼
FastAPI Endpoint
   │
   ▼
Pydantic Validation
   │
   ▼
Business Logic
   │
   ▼
JSON File Operations
   │
   ▼
Response Returned
```

### Explanation

* Client sends request.
* FastAPI receives request.
* Pydantic validates incoming data.
* CRUD logic executes.
* Data is loaded from or saved to JSON file.
* Response is returned to client.

---

# Data Storage Strategy

The application uses a JSON file instead of a database.

### Read Operation

```python
data = load_data()
```

Loads all records from:

```text
patients.json
```

### Write Operation

```python
save_data(data)
```

Saves modified records back into:

```text
patients.json
```

---

# Utility Functions

## load_data()

### Purpose

Reads all patient records from JSON storage.

### Syntax

```python
def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data
```

### Workflow

```text
patients.json
      │
      ▼
 json.load()
      │
      ▼
 Python Dictionary
```

### Return Type

```python
dict
```

---

## save_data()

### Purpose

Writes updated records into JSON storage.

### Syntax

```python
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)
```

### Workflow

```text
Python Dictionary
       │
       ▼
 json.dump()
       │
       ▼
 patients.json
```

---

# CRUD Architecture

## Create

```text
POST /create
```

Adds a new patient.

---

## Read

```text
GET /view
GET /patient/{patient_id}
```

Retrieves patient data.

---

## Update

```text
PUT /edit/{patient_id}
```

Updates existing patient information.

---

## Delete

```text
DELETE /delete/{patient_id}
```

Removes a patient record.

---

# Patient Data Model

The application uses a Pydantic model called:

```python
class Patient(BaseModel)
```

This model validates incoming request data before processing.

---

## Patient Schema

```python
Patient
│
├── id
├── name
├── age
├── height_m
├── weight_kg
├── gender
├── city
├── blood_group
├── bmi
└── verdict
```

---

# Patient Fields

## id

```python
id: str
```

Purpose:

* Unique patient identifier

Example:

```text
P001
```

---

## name

```python
name: str
```

Purpose:

* Stores patient name

Example:

```text
Ritesh
```

---

## age

```python
age: int
```

Validation:

```python
gt=0
lt=120
```

Rules:

* Greater than 0
* Less than 120

Valid:

```python
25
```

Invalid:

```python
-5
150
```

---

## height_m

```python
height_m: float
```

Stores patient height in meters.

Example:

```python
1.75
```

---

## weight_kg

```python
weight_kg: float
```

Stores patient weight in kilograms.

Example:

```python
70
```

---

## gender

```python
Literal[
    "Male",
    "Female",
    "Others"
]
```

Allowed values:

* Male
* Female
* Others

Invalid values automatically fail validation.

---

## city

```python
city: str
```

Stores city name.

---

## blood_group

```python
blood_group: str
```

Stores blood group.

Example:

```text
A+
B+
AB+
O+
```

---

# Computed Fields

The project automatically calculates additional information.

---

## BMI Calculation

```python
@computed_field
@property
def bmi(self):
```

Formula:

```text
BMI = Weight / Height²
```

Example:

```text
Weight = 70kg
Height = 1.75m

BMI = 70 / (1.75 × 1.75)

BMI = 22.86
```

Generated automatically.

Client does not send BMI.

---

## Health Verdict

```python
@computed_field
@property
def verdict(self):
```

Generated automatically from BMI.

### Rules

| BMI Range | Verdict       |
| --------- | ------------- |
| <18.5     | Underweight   |
| 18.5–24.9 | Normal Weight |
| 25–29.9   | Overweight    |
| >=30      | Obese         |

Example:

```text
BMI = 22.86

Verdict:
Normal Weight
```

---

# Update Model Architecture

The project uses a separate model:

```python
class PatientUpdate(BaseModel)
```

Purpose:

* Supports partial updates
* Makes every field optional
* Prevents unnecessary data submission

---

## Example

Existing Patient:

```json
{
    "name":"Ritesh",
    "age":22,
    "city":"Varanasi"
}
```

Request:

```json
{
    "city":"Lucknow"
}
```

Result:

```json
{
    "name":"Ritesh",
    "age":22,
    "city":"Lucknow"
}
```

Only modified fields are updated.

---

# Error Handling Strategy

The application uses:

```python
HTTPException
```

Benefits:

* Proper HTTP status codes
* Clear error messages
* API-friendly responses

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Patient Not Found"
)
```

Response:

```json
{
    "detail":"Patient Not Found"
}
```

---

# Response Architecture

The application returns responses in two forms.

## Normal Python Dictionary

```python
return data
```

FastAPI automatically converts it into JSON.

---

## JSONResponse

```python
return JSONResponse(
    status_code=201,
    content={
        "message":"patient created successfully"
    }
)
```

Used when custom status codes are required.

---

# Validation Layer

Validation occurs before route execution.

```text
Client Request
      │
      ▼
Pydantic Validation
      │
      ▼
Valid Data
      │
      ▼
Route Execution
```

If validation fails:

```text
422 Unprocessable Entity
```

is returned automatically.

---

# Key Learning Outcomes

* REST API development
* CRUD implementation
* JSON file handling
* FastAPI routing
* Request validation
* Query parameters
* Path parameters
* Computed fields
* Partial updates
* Error handling
* Structured API responses
* Data persistence without a database

