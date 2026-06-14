from fastapi import FastAPI, HTTPException
import json

app = FastAPI()
#https://mockaroo.com/ This is Website where u can generate json, csv and many more file automatically for testing purpose
#Or you can say chatgpt to create the sample of 1000 patient record in json file or u want to . 
def load_data():
    with open ('patients.json','r') as f :
        data = json.load(f)
    return data

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/About')
def aaaabout():
    return {"About": "about"}

@app.get('/view')
def views ():
    data  = load_data ()
    return data


@app.get('/patient/{patient_id}')
def patient_id(patient_id:str):
    #load all data 
    data = load_data()

    if patient_id in data :
        return data[patient_id]
    else:
       # return{'error':'Patient not found '}
        raise HTTPException(status_code=404,detail='Patient Not Found') 
        # HTTPException is a special built-in exception in FastAPI used to return custom HTTP error responses
        # when something goes wrong in your API.
        #Instead of returning a normal JSON or crashing the server, you can gracefully raise an error with:
        # a proper HTTP status code (like 404, 400, 403, etc.)
        #  a custom error message
        # (optional) extra headers
        







