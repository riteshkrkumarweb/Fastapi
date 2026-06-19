# API Endpoint Documentation

This section explains every endpoint available in the Patient Management System, including request parameters, validation rules, responses, status codes, and internal workflow.

---

# Base URL

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 1. Root Endpoint

## Endpoint

```http
GET /
```

## Purpose

Used to verify that the API server is running successfully.

## Request

No request body required.

## Response

```json
{
    "Hello": "World"
}
```

## Status Code

```text
200 OK
```

## Workflow

```text
Client Request
      │
      ▼
GET /
      │
      ▼
Return Dictionary
      │
      ▼
JSON Response
```

---

# 2. About Endpoint

## Endpoint

```http
GET /About
```

## Purpose

Returns basic information from the About route.

## Request

No request body required.

## Response

```json
{
    "About": "about"
}
```

## Status Code

```text
200 OK
```

---

# 3. View All Patients

## Endpoint

```http
GET /view
```

## Purpose

Returns all patient records stored inside the JSON database.

## Request

No parameters required.

## Internal Workflow

```text
Request
   │
   ▼
load_data()
   │
   ▼
patients.json
   │
   ▼
Dictionary
   │
   ▼
Return Data
```

## Example Response

```json
{
    "P001": {
        "name": "Ritesh",
        "age": 22,
        "height_m": 1.75,
        "weight_kg": 70,
        "gender": "Male",
        "city": "Varanasi",
        "blood_group": "B+",
        "bmi": 22.86,
        "verdict": "Normal Weight"
    }
}
```

## Status Code

```text
200 OK
```

---

# 4. Retrieve Patient by ID

## Endpoint

```http
GET /patient/{patient_id}
```

## Purpose

Returns a specific patient's information using Patient ID.

---

## Path Parameter

### patient_id

```python
patient_id: str = Path(...)
```

Validation:

* Required parameter
* Must be passed in URL

Example:

```http
GET /patient/P001
```

---

## Success Response

```json
{
    "name": "Ritesh",
    "age": 22,
    "height_m": 1.75,
    "weight_kg": 70,
    "gender": "Male",
    "city": "Varanasi",
    "blood_group": "B+",
    "bmi": 22.86,
    "verdict": "Normal Weight"
}
```

---

## Error Response

When patient does not exist:

```json
{
    "detail": "Patient Not Found"
}
```

---

## Status Codes

```text
200 OK
404 Not Found
```

---

## Workflow

```text
Patient ID
     │
     ▼
load_data()
     │
     ▼
Patient Exists?
     │
 ┌───┴────┐
 │        │
Yes       No
 │         │
 ▼         ▼
Return    HTTPException
Data      404
```

---

# 5. Sort Patients

## Endpoint

```http
GET /sort
```

## Purpose

Sorts patient records according to a selected field.

---

## Query Parameters

### sort_by

```python
sort_by: str
```

Allowed Values:

* name
* age
* city
* gender
* blood_group

Example:

```http
GET /sort?sort_by=age
```

---

### order

```python
order: str = "asc"
```

Allowed Values:

* asc
* des

Example:

```http
GET /sort?sort_by=age&order=des
```

---

## Ascending Example

```http
GET /sort?sort_by=age&order=asc
```

Result:

```text
18
22
30
40
```

---

## Descending Example

```http
GET /sort?sort_by=age&order=des
```

Result:

```text
40
30
22
18
```

---

## Invalid Field Response

```json
{
    "detail": "Invalid field selected from the ['name', 'age', 'city', 'gender', 'blood_group']"
}
```

---

## Invalid Order Response

```json
{
    "detail": "Invalid order is selected between asc and dsc"
}
```

---

## Status Codes

```text
200 OK
404 Not Found
```

---

## Workflow

```text
Query Parameters
       │
       ▼
Validate Field
       │
       ▼
Validate Order
       │
       ▼
Load Data
       │
       ▼
sorted()
       │
       ▼
Return Result
```

---

# 6. Create Patient

## Endpoint

```http
POST /create
```

## Purpose

Creates a new patient record.

---

## Request Body

```json
{
    "id": "P001",
    "name": "Ritesh",
    "age": 22,
    "height_m": 1.75,
    "weight_kg": 70,
    "gender": "Male",
    "city": "Varanasi",
    "blood_group": "B+"
}
```

---

## Automatic Fields

These fields are generated automatically:

```json
{
    "bmi": 22.86,
    "verdict": "Normal Weight"
}
```

Client does not send them.

---

## Validation Rules

### age

```python
gt=0
lt=120
```

Valid:

```json
{
    "age": 25
}
```

Invalid:

```json
{
    "age": -10
}
```

---

### gender

```python
Literal[
    "Male",
    "Female",
    "Others"
]
```

Valid:

```json
{
    "gender":"Male"
}
```

Invalid:

```json
{
    "gender":"Unknown"
}
```

---

## Success Response

```json
{
    "message": "patient created successfully"
}
```

---

## Duplicate Patient Response

```json
{
    "detail": "Patient already Exist"
}
```

---

## Status Codes

```text
201 Created
400 Bad Request
422 Validation Error
```

---

## Workflow

```text
Client Request
      │
      ▼
Pydantic Validation
      │
      ▼
Patient Exists?
      │
 ┌────┴────┐
 │         │
No        Yes
 │          │
 ▼          ▼
Save      400 Error
Data
 │
 ▼
201 Created
```

---

# 7. Update Patient

## Endpoint

```http
PUT /edit/{patient_id}
```

## Purpose

Updates existing patient information.

Supports partial updates.

---

## Path Parameter

```http
/edit/P001
```

Patient ID:

```text
P001
```

---

## Request Body Example

### Update City Only

```json
{
    "city": "Lucknow"
}
```

---

### Update Age Only

```json
{
    "age": 25
}
```

---

### Update Multiple Fields

```json
{
    "city": "Lucknow",
    "weight_kg": 75
}
```

---

## Internal Logic

The route uses:

```python
model_dump(exclude_unset=True)
```

Meaning:

Only fields provided by the user are updated.

---

## BMI Recalculation

After updating:

```python
Patient(**existing_patient_info)
```

creates a new Pydantic object.

This automatically recalculates:

* bmi
* verdict

---

## Success Response

```json
{
    "message": "patient updated"
}
```

---

## Error Response

```json
{
    "detail": "Patient Not Found"
}
```

---

## Status Codes

```text
200 OK
404 Not Found
422 Validation Error
```

---

## Workflow

```text
Request
   │
   ▼
Patient Exists?
   │
 ┌─┴──┐
 │    │
Yes   No
 │     │
 ▼     ▼
Update 404
Fields
 │
 ▼
Recalculate BMI
 │
 ▼
Save Data
 │
 ▼
200 OK
```

---

# 8. Delete Patient

## Endpoint

```http
DELETE /delete/{patient_id}
```

## Purpose

Removes a patient record from storage.

---

## Path Parameter

Example:

```http
DELETE /delete/P001
```

---

## Success Response

```json
{
    "message": "patient deleted"
}
```

---

## Error Response

```json
{
    "detail": "Patient not found"
}
```

---

## Status Codes

```text
200 OK
404 Not Found
```

---

## Workflow

```text
Patient ID
     │
     ▼
Load Data
     │
     ▼
Patient Exists?
     │
 ┌───┴────┐
 │        │
Yes       No
 │         │
 ▼         ▼
Delete    404
Record
 │
 ▼
Save Data
 │
 ▼
200 OK
```

---

# CRUD Endpoint Summary

| Operation | Method | Endpoint              |
| --------- | ------ | --------------------- |
| Create    | POST   | /create               |
| Read All  | GET    | /view                 |
| Read One  | GET    | /patient/{patient_id} |
| Update    | PUT    | /edit/{patient_id}    |
| Delete    | DELETE | /delete/{patient_id}  |
| Sort      | GET    | /sort                 |

---

# HTTP Status Codes Used

| Code | Meaning            |
| ---- | ------------------ |
| 200  | Request Successful |
| 201  | Resource Created   |
| 400  | Bad Request        |
| 404  | Resource Not Found |
| 422  | Validation Error   |

---

# API Lifecycle

```text
Client
   │
   ▼
FastAPI Route
   │
   ▼
Path/Query Validation
   │
   ▼
Pydantic Validation
   │
   ▼
Business Logic
   │
   ▼
JSON Storage
   │
   ▼
Response
```
