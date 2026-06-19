# FastAPI & Pydantic Personal Notes

These notes explain the concepts used in the Patient Management System project along with their purpose, syntax, parameters, and practical usage.

---

# FastAPI()

## What is FastAPI()?

`FastAPI()` is the main class used to create a FastAPI application instance.

Without it, routes cannot be registered and the API cannot run.

---

## Syntax

```python
from fastapi import FastAPI

app = FastAPI()
```

---

## Purpose

* Creates the API application
* Registers endpoints
* Generates Swagger UI automatically
* Handles requests and responses
* Manages routing

---

## Used In Project

```python
app = FastAPI()
```

---

## Important Notes

* Every FastAPI project starts with `FastAPI()`.
* Routes are attached to this object using decorators.

Example:

```python
@app.get('/')
def home():
    return {'message':'Hello'}
```

---

# Route Decorators

## What are Route Decorators?

Decorators connect a Python function to a URL endpoint.

---

## Syntax

```python
@app.get('/path')
```

```python
@app.post('/path')
```

```python
@app.put('/path')
```

```python
@app.delete('/path')
```

---

## Used In Project

```python
@app.get('/view')
```

```python
@app.post('/create')
```

```python
@app.put('/edit/{patient_id}')
```

```python
@app.delete('/delete/{patient_id}')
```

---

## HTTP Methods

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve Data |
| POST   | Create Data   |
| PUT    | Update Data   |
| DELETE | Delete Data   |

---

# BaseModel

## What is BaseModel?

`BaseModel` is the foundation of Pydantic.

It creates a schema for incoming data and validates it automatically.

---

## Syntax

```python
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
```

---

## Purpose

* Data validation
* Type conversion
* Serialization
* API request validation

---

## Used In Project

```python
class Patient(BaseModel):
```

```python
class PatientUpdate(BaseModel):
```

---

## Example

Input:

```json
{
    "name":"Ritesh",
    "age":"22"
}
```

Pydantic converts:

```python
age = 22
```

Automatically.

This process is called:

```text
Type Conversion
```

---

# Annotated

## What is Annotated?

`Annotated` attaches metadata to a type.

FastAPI and Pydantic use this metadata for validation and documentation.

---

## Syntax

```python
Annotated[
    str,
    Field(...)
]
```

---

## Used In Project

```python
name: Annotated[
    str,
    Field(...)
]
```

---

## Why Use Annotated?

Without Annotated:

```python
name:str
```

With Annotated:

```python
name: Annotated[
    str,
    Field(
        description='Patient Name'
    )
]
```

Additional validation and documentation become available.

---

# Field()

## What is Field()?

`Field()` provides validation rules and metadata for model attributes.

---

## Syntax

```python
Field(
    default,
    description='',
    gt=,
    lt=
)
```

---

## Common Parameters

| Parameter   | Purpose               |
| ----------- | --------------------- |
| default     | Default value         |
| description | Swagger description   |
| gt          | Greater Than          |
| ge          | Greater Than Equal    |
| lt          | Less Than             |
| le          | Less Than Equal       |
| min_length  | Minimum string length |
| max_length  | Maximum string length |
| example     | Example value         |

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

## Validation

Valid:

```python
age = 25
```

Invalid:

```python
age = -10
```

```python
age = 150
```

---

# Required Field (...)

## What is ... ?

Three dots represent a required field.

---

## Syntax

```python
Field(...)
```

Meaning:

```text
This field must be provided.
```

---

## Example

```python
name: Annotated[
    str,
    Field(...)
]
```

Valid:

```json
{
    "name":"Ritesh"
}
```

Invalid:

```json
{}
```

---

# Literal

## What is Literal?

`Literal` restricts values to predefined choices.

---

## Syntax

```python
Literal[
    'Male',
    'Female',
    'Others'
]
```

---

## Used In Project

```python
gender: Annotated[
    Literal[
        'Male',
        'Female',
        'Others'
    ],
    Field(...)
]
```

---

## Benefits

* Prevents invalid values
* Creates dropdown-like restrictions
* Improves data consistency

---

## Valid

```python
Male
Female
Others
```

---

## Invalid

```python
Unknown
ABC
```

---

# Optional

## What is Optional?

`Optional` allows a field to be either:

* Specific Type
* None

---

## Syntax

```python
Optional[str]
```

Equivalent:

```python
str | None
```

---

## Used In Project

```python
city: Optional[str]
```

---

## Why Used?

The update model allows partial updates.

User can update only one field.

Example:

```json
{
    "city":"Lucknow"
}
```

Without Optional, all fields would become mandatory.

---

# Path()

## What is Path()?

`Path()` validates and documents URL path parameters.

---

## Syntax

```python
Path(
    ...,
    description='',
    example=''
)
```

---

## Used In Project

```python
patient_id:str = Path(
    ...,
    description='Enter Patient ID',
    example='P001'
)
```

---

## Example

URL:

```http
/patient/P001
```

Here:

```text
P001
```

is a Path Parameter.

---

## Benefits

* Validation
* Swagger Documentation
* Better API readability

---

# Query()

## What is Query()?

`Query()` validates query parameters.

---

## Syntax

```python
Query(
    default,
    description=''
)
```

---

## Used In Project

```python
sort_by:str = Query(...)
```

```python
order:str = Query(
    'asc'
)
```

---

## Example

```http
/sort?sort_by=age&order=des
```

---

## Query Parameters

```text
sort_by = age
order = des
```

---

# computed_field()

## What is computed_field()?

A computed field creates values automatically from existing fields.

Client does not provide these values.

Pydantic generates them.

---

## Syntax

```python
@computed_field
@property
def bmi(self):
```

---

## Used In Project

```python
@computed_field
@property
def bmi(self):
```

```python
@computed_field
@property
def verdict(self):
```

---

## BMI Example

```python
weight = 70
height = 1.75
```

Formula:

```python
70/(1.75**2)
```

Output:

```python
22.86
```

Automatically generated.

---

# @property

## What is @property?

Converts a method into an attribute.

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

## Used With

```python
@computed_field
@property
```

---

# HTTPException

## What is HTTPException?

Used to send structured API errors.

---

## Syntax

```python
raise HTTPException(
    status_code=404,
    detail='Patient Not Found'
)
```

---

## Used In Project

```python
raise HTTPException(
    status_code=404,
    detail='Patient Not Found'
)
```

```python
raise HTTPException(
    status_code=400,
    detail='Patient already Exist'
)
```

---

## Common Status Codes

| Code | Meaning          |
| ---- | ---------------- |
| 400  | Bad Request      |
| 401  | Unauthorized     |
| 403  | Forbidden        |
| 404  | Not Found        |
| 422  | Validation Error |
| 500  | Server Error     |

---

# JSONResponse

## What is JSONResponse?

Returns a custom JSON response with a specific status code.

---

## Syntax

```python
JSONResponse(
    status_code=201,
    content={}
)
```

---

## Used In Project

```python
return JSONResponse(
    status_code=201,
    content={
        'message':'patient created successfully'
    }
)
```

---

## Why Use JSONResponse?

Normal return:

```python
return {'message':'created'}
```

Custom response:

```python
return JSONResponse(
    status_code=201,
    content={'message':'created'}
)
```

Allows custom status codes.

---

# model_dump()

## What is model_dump()?

Converts a Pydantic model into a Python dictionary.

---

## Syntax

```python
model.model_dump()
```

---

## Used In Project

```python
patient.model_dump()
```

---

## Example

Pydantic Object:

```python
patient = Patient(...)
```

Convert:

```python
patient.model_dump()
```

Result:

```python
{
    'name':'Ritesh',
    'age':22
}
```

---

# exclude

## Purpose

Exclude fields while converting to dictionary.

---

## Used In Project

```python
patient.model_dump(
    exclude=['id']
)
```

---

## Result

Before:

```python
{
    'id':'P001',
    'name':'Ritesh'
}
```

After:

```python
{
    'name':'Ritesh'
}
```

---

# exclude_unset

## Purpose

Returns only fields supplied by the user.

---

## Used In Project

```python
patient_update.model_dump(
    exclude_unset=True
)
```

---

## Example

Request:

```json
{
    "city":"Lucknow"
}
```

Output:

```python
{
    'city':'Lucknow'
}
```

Only modified fields are returned.

---

# JSON Module

## json.load()

Purpose:

* Read JSON file

Syntax:

```python
json.load(file)
```

---

## json.dump()

Purpose:

* Write data to JSON file

Syntax:

```python
json.dump(data,file)
```

---

# CRUD Summary

## Create

```http
POST /create
```

Insert new patient.

---

## Read

```http
GET /view
GET /patient/{patient_id}
```

Retrieve data.

---

## Update

```http
PUT /edit/{patient_id}
```

Modify existing record.

---

## Delete

```http
DELETE /delete/{patient_id}
```

Remove record.

---

# Key Concepts Learned From This Project

* FastAPI Application Creation
* Route Decorators
* CRUD Operations
* Pydantic Models
* Field Validation
* Annotated Types
* Literal Validation
* Optional Fields
* Path Parameters
* Query Parameters
* Computed Fields
* Property Decorator
* JSON Responses
* HTTP Exceptions
* model_dump()
* Partial Updates
* JSON File Storage
* Request Validation
* Automatic API Documentation
