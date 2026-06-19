# =========================
# Import Required Libraries
# =========================

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field  # see on the github i have how to use the pydantic for validation of data
from typing import Annotated, Literal, Optional  # This is also the part of the pydanctic
import json


# =========================
# Create FastAPI Application
# =========================

app = FastAPI()


# =========================
# Notes
# =========================

# https://mockaroo.com/ This is Website where u can generate json, csv and many more file automatically for testing purpose
# Or you can say chatgpt to create the sample of 1000 patient record in json file or u want to.


# =========================
# Utility Functions
# =========================

def load_data():
    """
    Load all patient data from patients.json file.
    """
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    """
    Save updated patient data into patients.json file.
    """
    with open('patients.json', 'w') as f:
        json.dump(data, f)


# =========================
# Basic Routes
# =========================

@app.get('/')
def read_root():
    """
    Root endpoint.
    """
    return {"Hello": "World"}


@app.get('/About')
def aaaabout():
    """
    About endpoint.
    """
    return {"About": "about"}


# =========================
# Retrieve All Patients
# =========================

# From the CRUD part this is Retrive part , view all data

@app.get('/view')
def views():
    """
    View all patient records.
    """
    data = load_data()
    return data


# =========================
# Retrieve Patient By ID
# =========================

# view data with the patient id

@app.get('/patient/{patient_id}')
def patient_id(
    patient_id: str = Path(
        ...,
        description='Enter the patient id to retrive from the DB',
        example='P001'
    )
):
    # Path Sets rules and information for values taken from the URL path

    # load all data
    data = load_data()

    # check if patient exists
    if patient_id in data:
        return data[patient_id]

    # return proper error if patient is not found
    else:
        # return{'error':'Patient not found '}
        raise HTTPException(
            status_code=404,
            detail='Patient Not Found'
        )  # HTTPException: Sends a clear error message when a request fails


# =========================
# Sort Patient Records
# =========================

# sort the data on the basis of name , age and gender

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(
        ...,
        description='Sort on the Basis of name , age , city , gender'
    ),
    order: str = Query(
        'asc',
        description='sort in acending or desending order '
    )
):

    # fields allowed for sorting
    valid_fields = ['name', 'age', 'city', 'gender', 'blood_group']

    # validate selected field
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=404,
            detail=f'Invalid field selected from the {valid_fields}'
        )

    # validate sorting order
    if order not in ['asc', 'des']:
        raise HTTPException(
            status_code=404,
            detail='Invalid order is selected between asc and dsc'
        )

    # load data from json file
    data = load_data()

    # determine sorting direction
    sort_order = True if order == 'des' else False

    # sort patient records
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data


# =========================
# Patient Model
# =========================

# Now here with read the Create Part from the CRUD .
# and this is Post type something u send data to the server

class Patient(BaseModel):
    # with the pydantic we have created this . for more see on the github

    id: Annotated[
        str,
        Field(..., description='Id of the Patient ')
    ]  # ...,(means required field )

    name: Annotated[
        str,
        Field(..., description='Enter the name of the patient ')
    ]

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=120,
            description='Enter the Age of the Patient'
        )
    ]  # gt = greather than and lt = less than

    height_m: Annotated[
        float,
        Field(..., description='Enter the heights in the meters ')
    ]

    weight_kg: Annotated[
        float,
        Field(..., description='Enter the weight in the kg ')
    ]

    gender: Annotated[
        Literal['Male', 'Female', 'Others'],
        Field(..., description='Enter the Gender of Patient')
    ]  # Literal means giving opition

    city: Annotated[
        str,
        Field(..., description="Enter the city of Patient ")
    ]

    blood_group: Annotated[
        str,
        Field(..., description='Enter the Blodd group of the patient ')
    ]

    # Automatically calculate BMI
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight_kg / (self.height_m ** 2), 2)
        return bmi

    # Automatically generate health verdict based on BMI
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal Weight"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


# =========================
# Create Patient
# =========================

# Now we had created the model above class Patient
# and now lets write the Endpoint

@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail='Patient already Exist'
        )

    # if not add the patient to the database ,
    # data is the dictionary and the patient is the pydentic model
    # so first we make the pydentic into the dictionary by using this code

    data[patient.id] = patient.model_dump(exclude=['id'])  # type: ignore

    # this is the dictory so we make reverse in the json file
    save_data(data)

    return JSONResponse(
        status_code=201,
        content={'message': 'patient created successfully'}
    )


# =========================
# Update Patient Model
# =========================

# Now the Update here , from the CRUD we donot id here beacuse it is the request module

class PatientUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(default=None)
    ]

    city: Annotated[
        Optional[str],
        Field(default=None)
    ]

    age: Annotated[
        Optional[int],
        Field(default=None, gt=0)
    ]

    gender: Annotated[
        Optional[Literal['Male', 'Female', 'Others']],
        Field(default=None)
    ]

    height_m: Annotated[
        Optional[float],
        Field(default=None, gt=0)
    ]

    weight_kg: Annotated[
        Optional[float],
        Field(default=None, gt=0)
    ]


# =========================
# Update Patient
# =========================

@app.put('/edit/{patient_id}')
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):

    # load existing patient data
    data = load_data()

    # check patient existence
    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail='Patient Not Found'
        )

    # get existing patient information
    existing_patient_info = data[patient_id]

    # only get fields provided by user
    updated_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    # update existing fields
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    data[patient_id] = existing_patient_info

    # existing_patient_info -> pydantic object -> updated bmi + verdict

    existing_patient_info['id'] = patient_id

    patient_pydandic_obj = Patient(**existing_patient_info)

    # -> pydantic object -> dict

    existing_patient_info = patient_pydandic_obj.model_dump(
        exclude='id' # type: ignore
    )  

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={'message': 'patient updated'}
    )


# =========================
# Delete Patient
# =========================

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    # check patient existence
    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail='Patient not found'
        )

    # delete patient record
    del data[patient_id]

    # save updated data
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={'message': 'patient deleted'}
    )