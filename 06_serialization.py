from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump() # it converts pydantic model to python dictonary
print(temp)
print(type(temp)) # it returns dict type.

temp1=patient1.model_dump_json() # it converts pydantic model to JSON.
print(temp1)
print(type(temp1)) # it returns str type. 

temp2 = patient1.model_dump(include=['name' ,'gender']) # it  import specific part. which we write here 
print(temp2)
print(type(temp2)) # it returns dict type.

temp3 = patient1.model_dump(exclude='name') # it import everthing exclude which we written here.
print(temp3)
print(type(temp3)) # it returns dict type.

temp4 = patient1.model_dump(exclude={'address':['state']}) # now its only exclude particular data
print(temp4)         
print(type(temp4)) # it returns dict type.    



temp = patient1.model_dump(exclude_unset=True) # here we can see via use this we stop export partcular data which not available is pataient1 dict , in our case its stop printing gender which we already set male but for this its not print.
print(temp)
print(type(temp)) # it returns dict type.

