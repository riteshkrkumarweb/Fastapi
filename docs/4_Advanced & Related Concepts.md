# Advanced FastAPI & Pydantic Concepts

These concepts are not directly used in the Patient Management System project but are commonly used in real-world FastAPI applications.

---

# Body()

## What is Body()?

`Body()` is used to configure and validate request body data.

It provides metadata and validation rules similar to `Field()`, but for endpoint parameters.

---

## Syntax

```python
from fastapi import Body

@app.post('/create')
def create_user(
    name: str = Body(
        ...,
        min_length=3,
        description='Enter user name'
    )
):
    return {'name': name}
```

---

## Common Parameters

| Parameter   | Purpose                       |
| ----------- | ----------------------------- |
| default     | Default value                 |
| embed       | Wrap value inside JSON object |
| description | Swagger description           |
| example     | Example value                 |
| gt          | Greater than                  |
| lt          | Less than                     |

---

## Example

Without embed:

```json
"Ritesh"
```

With embed:

```python
name: str = Body(..., embed=True)
```

Request:

```json
{
    "name":"Ritesh"
}
```

---

# response_model

## What is response_model?

Defines the structure of data returned by an endpoint.

FastAPI validates the response before sending it to the client.

---

## Syntax

```python
@app.get(
    '/user',
    response_model=User
)
```

---

## Example

```python
class User(BaseModel):
    name:str
    age:int

@app.get(
    '/user',
    response_model=User
)
def get_user():
    return {
        'name':'Ritesh',
        'age':22
    }
```

---

## Benefits

* Response validation
* Data filtering
* Better Swagger documentation
* Prevents accidental data exposure

---

# field_validator()

## What is field_validator()?

Used to validate a single field.

Runs custom validation logic.

---

## Syntax

```python
from pydantic import field_validator
```

```python
@field_validator('age')
```

---

## Example

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age:int

    @field_validator('age')
    @classmethod
    def validate_age(cls,value):

        if value < 18:
            raise ValueError(
                'Age must be at least 18'
            )

        return value
```

---

## Workflow

```text
Input
  │
  ▼
Field Validation
  │
  ▼
Pass / Fail
```

---

## Use Cases

* Username validation
* Email validation
* Password rules
* Custom business rules

---

# model_validator()

## What is model_validator()?

Validates multiple fields together.

Useful when one field depends on another.

---

## Syntax

```python
from pydantic import model_validator
```

---

# mode='before'

Runs before Pydantic type conversion.

---

## Example

```python
@model_validator(mode='before')
```

Input:

```python
{
    'age':'22'
}
```

Value is still:

```python
'22'
```

String.

---

# mode='after'

Runs after model creation.

---

## Example

```python
@model_validator(mode='after')
```

Input:

```python
{
    'age':'22'
}
```

Pydantic converts:

```python
22
```

Integer.

Validation happens after conversion.

---

## Example

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):

    password:str
    confirm_password:str

    @model_validator(
        mode='after'
    )
    def passwords_match(self):

        if (
            self.password
            !=
            self.confirm_password
        ):
            raise ValueError(
                'Passwords do not match'
            )

        return self
```

---

# computed_field()

## Advanced Use Case

Instead of storing calculated values, generate them dynamically.

---

## Example

```python
@computed_field
@property
def full_name(self):

    return (
        self.first_name
        +
        ' '
        +
        self.last_name
    )
```

Output:

```python
full_name
```

Generated automatically.

---

# Serialization

## What is Serialization?

Converting Python objects into a transferable format.

Usually JSON.

---

## Example

Python Dictionary:

```python
{
    'name':'Ritesh'
}
```

JSON:

```json
{
    "name":"Ritesh"
}
```

---

## In FastAPI

```python
return {'name':'Ritesh'}
```

FastAPI serializes it automatically.

---

# Deserialization

## What is Deserialization?

Converting JSON into Python objects.

---

## Example

JSON:

```json
{
    "name":"Ritesh"
}
```

Converted Into:

```python
{
    'name':'Ritesh'
}
```

---

## In FastAPI

Request Body:

```json
{
    "name":"Ritesh"
}
```

Converted Into:

```python
Patient(
    name='Ritesh'
)
```

Automatically.

---

# Depends()

## What is Depends()?

FastAPI's Dependency Injection System.

Used for reusable logic.

---

## Syntax

```python
from fastapi import Depends
```

---

## Example

```python
def get_user():

    return {
        'name':'Ritesh'
    }

@app.get('/profile')
def profile(
    user=Depends(get_user)
):
    return user
```

---

## Workflow

```text
Request
   │
   ▼
Dependency
   │
   ▼
Route Function
   │
   ▼
Response
```

---

## Common Uses

* Authentication
* Authorization
* Database Sessions
* Logging
* Configuration

---

# Response Class

## Purpose

Customize API responses.

---

## Common Response Types

| Response          | Purpose       |
| ----------------- | ------------- |
| JSONResponse      | JSON Output   |
| HTMLResponse      | HTML Output   |
| PlainTextResponse | Text Output   |
| FileResponse      | File Download |
| RedirectResponse  | Redirect User |
| StreamingResponse | Stream Data   |

---

# Status Codes

## Informational

| Code | Meaning  |
| ---- | -------- |
| 100  | Continue |

---

## Success

| Code | Meaning    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 204  | No Content |

---

## Client Errors

| Code | Meaning            |
| ---- | ------------------ |
| 400  | Bad Request        |
| 401  | Unauthorized       |
| 403  | Forbidden          |
| 404  | Not Found          |
| 405  | Method Not Allowed |
| 422  | Validation Error   |

---

## Server Errors

| Code | Meaning               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |

---

# Request Lifecycle in FastAPI

```text
Client Request
      │
      ▼
Route Matching
      │
      ▼
Path Validation
      │
      ▼
Query Validation
      │
      ▼
Body Validation
      │
      ▼
Dependency Execution
      │
      ▼
Route Function
      │
      ▼
Response Serialization
      │
      ▼
Client Response
```

---

# Pydantic Type Conversion

## Example

Input:

```json
{
    "age":"22"
}
```

Schema:

```python
age:int
```

Output:

```python
age = 22
```

Pydantic automatically converts compatible values.

---

# Common Validation Types

## String

```python
name:str
```

---

## Integer

```python
age:int
```

---

## Float

```python
salary:float
```

---

## Boolean

```python
is_active:bool
```

---

## List

```python
skills:list[str]
```

---

## Dictionary

```python
metadata:dict
```

---

## Optional

```python
city:Optional[str]
```

---

## Literal

```python
status:Literal[
    'active',
    'inactive'
]
```

---

# Nested Models

## Purpose

Represent complex structured data.

---

## Example

```python
class Address(BaseModel):

    city:str
    state:str
    pin:str
```

```python
class Patient(BaseModel):

    name:str
    address:Address
```

---

## Request

```json
{
    "name":"Ritesh",
    "address":{
        "city":"Varanasi",
        "state":"UP",
        "pin":"221011"
    }
}
```

---

# Important Interview Questions

## FastAPI

* What is FastAPI?
* Why is FastAPI faster than Flask?
* Difference between Path and Query?
* What is Dependency Injection?
* What is response_model?
* What is JSONResponse?

---

## Pydantic

* What is BaseModel?
* What is Field()?
* What is Annotated?
* What is Literal?
* What is Optional?
* What is model_dump()?
* Difference between field_validator() and model_validator()?
* Difference between before and after mode?
* What is computed_field()?
* What is Serialization and Deserialization?

---

# Final Concepts Covered

* FastAPI()
* Route Decorators
* BaseModel
* Field()
* Annotated
* Literal
* Optional
* Query()
* Path()
* Body()
* response_model
* computed_field()
* field_validator()
* model_validator()
* Depends()
* JSONResponse
* HTTPException
* model_dump()
* Serialization
* Deserialization
* Status Codes
* Nested Models
* Dependency Injection
* Request Lifecycle
* Type Conversion
