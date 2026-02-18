from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    
    name : str
    email: EmailStr
    age : int
    weight : float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model) : 
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must haver an emergency contact')
        return model
    
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('insert')
    
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('update')
    
patient_info = {'name': 'Vishal', 'email' : 'vishal@hdfc.com', 'age': '65', 'weight': 75.2, 'married' : True, 'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '2233445566', 'emergency': '5566778899'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)