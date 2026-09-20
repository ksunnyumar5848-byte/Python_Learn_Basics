"""print("Practice the python concept ")


#some python how to workd ans input and output and type casting 

name="sunny kumar "
age=20
location="jharkhand"
teacher="Vikash sir "
profession="bca "

print("=============all the information about the user ==============\nclea")
print(f" hello {teacher} my name is  {name}\n i form {location} i persuring {profession} \n  i learn the python this language are very ")
print(f"i have one team member and his also working profession he work on Accenture company and and many company \n ")


#types casting 
print("------------input information form  person ---------------------")

myname=input("Enter the name of user ")
myprofession=input("Enter the work profession of user ")
company=input("Enter the company name ")


print("print the user input information and this data type \n ")

print(f"my name {myname} and data type--->{type(myname)} \n \n working profession {myprofession}\n  and i currenty woring in {company}")


#operator 

#  logic operator





isID=False
Token_number=int(input("Enter the token number "))

if isID==True:
    print("Enter the Holl ")
    if isID ==True and Token_number==10:
        print("welcome bro you are join the new company  ")
    else:
        print(f"pleae this token NO {Token_number} are the worng ")
else:
    print("bro you have no id  you are not allowed ")            



# some collection and data structure in the python 

#list is collection is store the data and value allow the duplicate value and imp list are the modify the original list 
#multiple data type and some inbuilt methods like splice reverse sort sroted index access ->lastindexof firstindex 
# append pop push as so an 
#synatx of list listnmae=[]--> here some values 

number=[10,20,30,40,50,60]

print(f"my list data is : {number} and type {type(number)}")

#some methods in the list 

number.append(10)
number.append("sunny kumar ")
print(number)
mycount=number.count("sunny kumar ")
datacount=number.count(30)
print(mycount)
print(mycount)

number.append("rahul kumar ")
print(number)

# print("----------------")
# number.pop()
# number.pop("rahul kumar ")
# print(number)
# number.sort()
# print(number)
number.pop(8)
print(number)
number.pop(5)
number.pop(6)
print(number)
number.pop(3)
print(number)
number.reverse()
print(number)
number.pop(0)
print(number)




#tuples are the store data multiple data type but afer creating the tuples not modify the tuples and it has only 
#two methods first are the            tupes are not allow the assigment opreator 



mytuples=(10,20,30,40,50,60)

print(mytuples)

print(mytuples[0])
print(mytuples[4])
print(mytuples.count(10))
print(mytuples.index(60))




# dictniory dictory are the store the data into the key and value pairs 
#key are always in the "" quats and the values are me or me not be and seconds most important are the key allways are the unique and 
#values are the diffenent 

person={
    "name":"Atul Yadav ",
    "age":20,
    "FirstJob":"Tcs",
    "profession":"Full stack dev and GEN AI ",
    "location":{
        "first locaton":"jharkhand ",
        "my location ":"ranchi ",
        "Hobbies":" "
    }
      
}

print(person["location"])

# print(person["age"])
# print(person.get("age"))
print(f"\n")
# print(person.keys())
print()
# print(person.items())
# print(person)
# person["name"]="Deepak kumar "
# print(person)

convert=list(person)

print(f"{convert} and datatype {type(convert)} ")
print(f"{person} and datatype {type(person)}")


"""


# set data strusture in the python are not store the duplicate value 
# some imp operation in set 

myset={10,20,30,40,50,"sunny "}


for i in myset:
    print(f" the list items {i}")
myset2={10,20,80,60,90,40}
print(myset)
print(myset.add(60))
print(myset)
myintersetion=myset.intersection(myset2)  #---it provide the comman values 
myunion=myset.union(myset2)

print(myintersetion)
print(myunion)
print(myset.difference(myset2))


