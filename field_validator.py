from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name: str 
    age:int  
    weight: float  
    married: bool 
    allergies:  List[str]
    contact_details:Dict[str,str]
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")
        return value
    @field_validator
    @classmethod
    def transform_name(cls,value):
        return value.upper()

def patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("inserted")
def updated_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("updated")
patient_info={'name':'raju','age':20,'weight':61.5,'married':False,'contact_details':{'email':'raju@gmail.com','phone_no':'389492839'}}
patient1=Patient(**patient_info)
updated_patient_data=patient1