from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open ('patient.json','r') as f :
        data = json.load(f)
    return data

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/xbout')
def aaaabout():
    return {"bout": "about"}


@app.get('/cbout')
def vt():
    return {"viduu": "Vidya"}

@app.get('/view')
def views ():
    data  = load_data ()
    return data


@app.get('/patient/{patient_id}')
def patient_id(patient_id:int):
    #load all data 
    data = load_data()

    if patient_id in data :
        return data[patient_id]
    else:
        return {'message':'Patinent not found'}




