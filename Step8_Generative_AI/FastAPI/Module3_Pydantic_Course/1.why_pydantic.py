# From the below code we will understand the need of pydantic library

def insert_patient_data(name:str,age:int):
    print(name)
    print(age)
    print("Successfully inserted into database")

insert_patient_data("Azaan",24)

# NOTE : the typehunting of the python is not so strong because of that we will use pydantic

# Custom type validation
def insert_patient_data2(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("Successfully inserted into database")
    else :
        raise TypeError('Incorrect data type')

insert_patient_data2("Azaan",24)

# The above method works fine but there is hope of improvement

# Problem 1 : Type Validation 
# Problem 2 : Data Validation 

#* The both problem solved by pydantic 