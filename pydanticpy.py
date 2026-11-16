from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the Patient',description="give the name of patient in less than 50 character",examples=['kaju','raju'])]
    age:int = Field(gt=0,lt=120)
    email:EmailStr
    linkdin_url:AnyUrl
    weight:Annotated[float ,Field(gt=0,strict=True)]
    married:Annotated[ bool,Field(default=None,description='is the patient is marrid or not')]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details:Dict[str,str]


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