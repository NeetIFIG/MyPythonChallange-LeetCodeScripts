#Day 2: 30 Days of python programming
###### Ejercicio 1
def returnType(variable):
    print (type(variable))
def returnLen(variable):
    print (len(variable))
def  AskAndReturn(Question ,VarToAssing):
    VarToAssing = input(Question +": ")
FirstName = "ESL"
LastName ="MLS"
FullName = FirstName + LastName
Country = "My Country"
CityVariable = "MyCity"
age,year = 123,2012
is_married,is_True,is_light = True, False, False
LotsVar =  [FirstName,LastName,FullName,Country,CityVariable,age,year,is_married,is_True,is_light]
###### Ejercicio 2
for var in LotsVar:
    returnType(var)
returnLen(FirstName)
print("Len  first Name : " +FirstName + "\n Len last Name : "+ LastName)
numOne,numTwo=5,4
Total=numOne+numTwo
diff=numOne-numTwo
product = numOne*numTwo
Division = numOne/numTwo
remainder = numTwo%numOne
exp=numOne**numTwo
floorDivision = numOne//numTwo
###
radio_user = int(input("Insert Radius "))
area_of_circle = 3.1416*(radio_user**2)
circum_of_circle = 2*3.1416*radio_user
print("Area of circle: " + str(area_of_circle)+" Circunference: "+ str(circum_of_circle))
AskAndReturn("First Name",FirstName)
AskAndReturn("Last Name",{LastName})
AskAndReturn("Country ",Country)
AskAndReturn("Age ",age)
print(help("keywords"))