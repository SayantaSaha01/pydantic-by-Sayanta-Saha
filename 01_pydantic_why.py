from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional , Annotated


class Patient(BaseModel): # it is a pydantic class  , bydefault the all fields are required it means  when you create a data of user all fields are required if not its throw error.
    
    # name:str=Field (max_length=50)# max_length it is custom constraint,you limit max word by 50 in string.
    name: Annotated[str, Field(max_length=50,title='name of the patient', description='give name in less than 50 characters', examples=['nitish','amit'])] # we can set meta data via using Annotated and Field combine

    email:EmailStr #it is a pure example of data validation , by using EmailStr from pydantic ,  you dont have to worry about email validation in your code, its a built in data validator type.
    linkedin_url:AnyUrl

    age:int=Field(gt=0,lt=120) # we can use Field for custom data validation via using custom constraints like gt,ge,lt,le.

    # weight:float=Field(gt=0) # we can use Field for custom data validation via using custom constraints like gt,ge,lt,le.
    weight:Annotated[float,Field(gt=0,lt=120,strict=True)] # here we can see via using Annotated and field we can set (strict=True), its overrite auto type conversation.
    # married:Optional[bool]=None

    married:Annotated[Optional[bool],Field(default=None)]

    allergies:List[str]=Field(max_length=5) #two level data type validation by use list[str],also use custom constraints by using Field(max_length=5).

    contact_details:Dict[str,str]  #two level data type validation by use this dict[str,str] 


def insert_patient_data(p:Patient): #function_name(parameter_name: type_hint/pydantic model)

    print(p.name) #this is atribite access not dictionary access , dictioay me Patient["name"]
    print(p.age)
    print(p.married)  # here it prints None until user send their data its optional field and we set default value = None
    print('insert into databases')
    print(p.email)

def uodate_patient_data(p:Patient):
    print(p.name)
    print(p.age)
    print(p.weight) #here it prints 70.2 until user send their data its not optional field and we set default value = 70.2
    print('updated')

patient_info={"name":"sayanta",'email':"iamsayantasaha01@gmail.com", "linkedin_url":"https://www.linkedin.com/in/sayanta-saha-a72b1832a/","age":"21" ,'weight':76.9,'allergies': ['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'767865444467'}} #creating a dictinary  ,you have to create all fields here which you add in pydantic basemodel.                                          

patient1=Patient(**patient_info) # it is now a pydantic object,not a dictionary, ** is unpacking dictionary

insert_patient_data(patient1)
uodate_patient_data(patient1)        


