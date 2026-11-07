## to day are the revision of the what are the list and what are the tupes ans and dictonary and how can the perform all 
## this data  sturcture 




#   firs are the list 

# number=[1,2,3,4,5]

# print(type(number))

# # my question are the traverse the list and all item are the print seprataly 
# #  my logic are the age keval index chahiye to range use karo ager index or value chahiye to enumerate use karo 



# for num in range(len(number)):
#     print(num, number[num])



#list and tuples and dictniory how to the print 





    











# # first word print the element 

# for i in range(len(information)):
#     print(f"index number {i } and value this index numebr : {information[i]}")




# getdata=information[3]

# print(f" it show the value of this : ->   {information.index("prakash")} index {getdata}")


# for index , item  in enumerate(information):
#     print(f" index number are : {index} and value : {item}")

# information=["sunny","rahul","ratan","prakash","sushila devi","puja"]

# result=[]

# for index, item  in enumerate(information):
#     result.append({
#         "index":index,
#         "data":item
#     })



# # for i in result:
# #     print(result)

# print(result)
# print(f" here o index value are the {result[0]} " )



name=["sunny","age","pradeep","mukesh","ronak"]


print(name)

## Access in the list through the index number 

print(name[0],name[3])




name[0]="Rahul Bhai"

name.append("new member ")
name.extend("Ranjana kumari ")
name.extend("AND")
items=name.count("sunny")
newlist=name.copy()

print(f" this are new list it copy list items ......{newlist}")

print(f" this element are how many times {items} ")

print(f" this methods are show the list items {name}")


for i in range(len(name)):
    data=name[i]
    print(f"this is your the data {data}")





mytuppes=("hello" ,"hi","hey")

print(mytuppes)

countdata=mytuppes.count("hello")

print(countdata)

whichele=mytuppes.index("hello")

print(whichele)










Cricketer={
    "name":"surya kumar yadav",
    "age":35,
    "RUNS":3000,
    "match":{
     "ODI":"20 MORE ",
     "T20":"BEST PERFORMANCE",
     "TEST":"DEBAUT"
    }
}


 # aceess in the dictionry

print(Cricketer["age"])
print(Cricketer["match"])

#updating in the list dic

Cricketer["name"]="MSD"

print(Cricketer["name"])



# some importent methods in the dic


keyitem=Cricketer.keys()

valitems=Cricketer.values()

print(keyitem)

print(valitems)


print(Cricketer.get("name"))  # this methods are the find which elemnet are the persent in the dic 




