from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):
    
    name : str
    email: EmailStr
    age : int
    weight : float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validation(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domina')
        
        return value
    
    @field_validator('name')
    @classmethod
    def trasform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else: 
            raise ValueError('Age should be in between 0 and 100')
    
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('insert')
    
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('update')
    
patient_info = {'name': 'Vishal', 'email' : 'vishal@hdfc.com', 'age': '30', 'weight': 75.2, 'married' : True, 'allergies' : ['pollen', 'dust'], 'contact_details' : {'phone' : '2233445566'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)