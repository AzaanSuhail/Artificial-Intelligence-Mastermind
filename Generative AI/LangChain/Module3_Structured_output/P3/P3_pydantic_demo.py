from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None # it means agr age hogi toh interger hogi wrna nhi hogi(none)
    email: EmailStr  #& It is  a different data type built in pydantic library only
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')  #~ gt means greater than, lt means less than


new_student = {'age':'32', 'email':'abc@gmail.com'}  #^ if you send wrong mail this will give error  

student = Student(**new_student) # ** represents dictionary

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()  #dump_json is a inbuilt function of pydantic