from fastapi import FastAPI, HTTPException , Path , Query
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
def patient_id(patient_id:str=Path(...,
    description='Enter the patient id to retrive from the DB',
    example='P001')): # Path Sets rules and information for values taken from the URL path
    #load all data 
    data = load_data()

    if patient_id in data :
        return data[patient_id]
    else:
       # return{'error':'Patient not found '}
        raise HTTPException(status_code=404,detail='Patient Not Found') # HTTPException: Sends a clear error message when a request fails 
    
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the Basis of name , age , city , gender'),
                  order:str=Query('asc',description='sort in acending or desending order ')):
    
    valid_fields = ['name','age','city','gender','blood_group']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail=f'Invalid field selected from the {valid_fields}')

    if order not in ['asc','des']:
        raise HTTPException(status_code=404,detail='Invalid order is selected between asc and dsc') 
    
    data = load_data()
    sort_order = True if order == 'des' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data



    

        
        







