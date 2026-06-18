# FastAPI CRUD Project Documentation

# FastAPI()

FastAPI is the main class used to create a FastAPI application.

Syntax

```python
from fastapi import FastAPI

app = FastAPI()
```

Purpose

* Creates an API application.
* Registers routes/endpoints.
* Generates automatic Swagger documentation.
* Handles requests and responses.

Example

```python
app = FastAPI()
```

One-Line Summary

FastAPI() is the starting point of every FastAPI application.

# Path()

The Path() function in FastAPI is used to provide metadata, validation rules, and documentation hints for path parameters in API endpoints.

Syntax

```python
Path(
    default,
    title="",
    description="",
    example=""
)
```

Important Parameters

* title → Title shown in API documentation.
* description → Description shown in Swagger UI.
* example → Example value for users.
* ge → Greater than or equal to.
* gt → Greater than.
* le → Less than or equal to.
* lt → Less than.
* min_length → Minimum string length.
* max_length → Maximum string length.
* pattern → Validate text using regex.
* alias → Alternative parameter name.
* deprecated → Marks parameter as deprecated.
* include_in_schema → Show or hide in docs.

Three Dots (...)

```python
Path(...)
```

The three dots (...) mean the field is required and cannot be omitted.

Example

```python
@app.get("/patient/{patient_id}")
def get_patient(
    patient_id: str = Path(
        ...,
        description="Enter Patient ID",
        example="P001"
    )
):
    return patient_id
```

One-Line Summary

Path() validates and documents values taken from the URL path.

# Query()

Query() is used in FastAPI to define and validate query parameters.

It helps add validation, default values, and documentation to query parameters.

Syntax

```python
Query(default, description="", min_length=1)
```

Important Parameters

* default → Sets the default value.
* description → Adds a description in API docs.
* example → Shows an example value.
* min_length → Minimum allowed string length.
* max_length → Maximum allowed string length.
* ge → Value must be greater than or equal to a number.
* gt → Value must be greater than a number.
* le → Value must be less than or equal to a number.
* lt → Value must be less than a number.
* pattern → Validates text using a regex pattern.
* alias → Uses a different name in the URL.
* deprecated → Marks the parameter as deprecated.
* include_in_schema → Shows or hides the parameter in API docs.

Real-Life Example

Imagine searching on Amazon:

```text
/products?category=laptop&price=50000
```

Here, category and price are query parameters because they come after ?.

Code Example

```python
from fastapi import Query

@app.get("/search")
def search(
    q: str = Query(
        min_length=3,
        description="Enter search keyword"
    )
):
    return {"query": q}
```

Memory Trick

Query = Questions in the URL

Anything after ? in a URL is usually a query parameter.

Common Mistake

Using Query() for path parameters.

```text
/users/{id}
```

id is a path parameter, so use Path(), not Query().

One-Line Summary

Query() is used to validate and document values passed after ? in a URL.

# HTTPException

HTTPException is a special built-in exception in FastAPI used to return custom HTTP error responses when something goes wrong in your API.

Instead of returning a normal JSON response or crashing the server, you can gracefully raise an error with:

* HTTP status code
* Custom error message
* Optional headers

Syntax

```python
raise HTTPException(
    status_code=404,
    detail="Patient Not Found"
)
```

Example

```python
if patient_id not in data:
    raise HTTPException(
        status_code=404,
        detail="Patient Not Found"
    )
```

One-Line Summary

HTTPException allows you to send meaningful error responses to clients.

# Most Common HTTP Status Codes

* 200 → OK (Request successful)
* 201 → Created (Resource created successfully)
* 400 → Bad Request (Invalid input from client)
* 401 → Unauthorized (Authentication required)
* 403 → Forbidden (Access denied)
* 404 → Not Found (Resource does not exist)
* 405 → Method Not Allowed (Wrong HTTP method used)
* 409 → Conflict (Resource already exists)
* 422 → Unprocessable Entity (Validation error)
* 500 → Internal Server Error (Server-side error)

# Request Body

A request body is the portion of an HTTP request that contains data sent by the client to the server.

It is commonly used with:

* POST
* PUT
* PATCH

The data is usually sent as:

* JSON
* XML
* Form Data
* Multipart Form Data

Example

```python
@app.post("/create")
def create_patient(patient: Patient):
    return patient
```

Here, Patient data is sent inside the request body.

Example JSON

```json
{
    "name": "Ritesh",
    "age": 20
}
```

One-Line Summary

A request body contains the data that a client sends to the server.

# Response

A response is the data returned by the server after processing a request.

Example

```python
return {
    "message": "Patient created successfully"
}
```

Response

```json
{
    "message": "Patient created successfully"
}
```

One-Line Summary

A response is the server's answer to a client's request.

# JSONResponse

JSONResponse is used to return a custom JSON response with a specific status code.

Syntax

```python
from fastapi.responses import JSONResponse

return JSONResponse(
    status_code=201,
    content={"message": "Created"}
)
```

Example

```python
return JSONResponse(
    status_code=201,
    content={"message": "Patient created successfully"}
)
```

One-Line Summary

JSONResponse allows full control over JSON output and status codes.

# Pydantic

Pydantic is a data validation library used by FastAPI.

It validates incoming data automatically and converts data types when possible.

Example

```python
class Patient(BaseModel):
    name: str
    age: int
```

Benefits

* Data validation
* Type conversion
* Automatic documentation
* Cleaner code

One-Line Summary

Pydantic validates and structures API data.

# BaseModel

BaseModel is the parent class used to create Pydantic models.

Example

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

One-Line Summary

BaseModel defines the structure and validation rules of data.

# Field()

Field() is used to add validation rules and documentation to model fields.

Syntax

```python
Field(
    default,
    description="",
    gt=0
)
```

Important Parameters

* default → Default value.
* description → Documentation text.
* example → Example value.
* gt → Greater than.
* ge → Greater than or equal to.
* lt → Less than.
* le → Less than or equal to.
* min_length → Minimum text length.
* max_length → Maximum text length.
* pattern → Regex validation.

Example

```python
age: int = Field(
    gt=0,
    lt=120,
    description="Enter age"
)
```

One-Line Summary

Field() adds validation and documentation to model attributes.

# Annotated

Annotated is used to combine a type with additional metadata.

Syntax

```python
Annotated[type, metadata]
```

Example

```python
age: Annotated[
    int,
    Field(gt=0, lt=120)
]
```

Benefits

* Keeps type and validation together.
* Recommended in FastAPI and Pydantic v2.

One-Line Summary

Annotated attaches validation metadata to a type.

# Literal

Literal means a value must be exactly what you specify.

Instead of allowing any text or number, you lock it down to a few exact choices.

You can think of it as giving predefined options.

Example

```python
gender: Literal[
    "Male",
    "Female",
    "Others"
]
```

Valid Values

```text
Male
Female
Others
```

Invalid Value

```text
Robot
```

One-Line Summary

Literal restricts a field to specific allowed values.

# computed_field

computed_field is used to create calculated fields that are automatically included in model output.

Example

```python
@computed_field
@property
def bmi(self) -> float:
    return round(
        self.weight_kg /
        (self.height_m ** 2),
        2
    )
```

Benefits

* Automatically calculated.
* Included in model_dump().
* No need to store in database.

One-Line Summary

computed_field creates dynamic fields calculated from other fields.

# model_dump()

model_dump() converts a Pydantic model into a Python dictionary.

Example

```python
patient.model_dump()
```

Output

```python
{
    "name": "Ritesh",
    "age": 20
}
```

Exclude Fields

```python
patient.model_dump(
    exclude=["id"]
)
```

One-Line Summary

model_dump() converts a Pydantic object into a dictionary.

# CRUD Operations

CRUD stands for:

* Create → Add data
* Read → Retrieve data
* Update → Modify data
* Delete → Remove data

HTTP Methods

* POST → Create
* GET → Read
* PUT/PATCH → Update
* DELETE → Delete

One-Line Summary

CRUD represents the four basic operations performed on data.
