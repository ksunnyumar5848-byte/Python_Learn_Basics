   # student record manager 

# add , update ,remove , list , quit 


students={

}
def infoAdd(students,name,age,marks,id):
    if id in students:
        return False
    students[id]={"name":name, "age":age, "marks":marks}
    return True
def updatemarks(students,id,marks):
    if id in students:
        students[marks]=marks
    return False  
def idremove(students,id):
    if id in students:
        del students[id]
        return True
    return False


while True:
    print(f"1. Add student \t  ")
    print(f"2. update ")
    print(f"3. remove student \t ")
    print(f"4. show student\t ")
    print(f"5. find student \t")
    print(f"exit. ......\n")


    choise=input("Enter the choise number ")

    if choise=='1':
        name=input("student name bro ")
        age=int(input("Student age bro "))
        marks=float(input("student marks bro "))
        id=int(input("Enter the id of student "))

        if infoAdd(students,name,age,marks,id):
            print("student information is added.... ")
        else:
            print("student are all ready added here ......")    
    elif choise=='2':
        id=int(input("Enter the id of students "))
        marks=float(input("Enter the new marks of student "))

        if updatemarks(students,id,marks):
            print("marks are the update of student ")
        else:
            print("marks are the all ready exits ")    
    elif choise=='3':
        id=int(input("Enter the id of student "))

        if idremove(students,id):
            print("exits students are romve here......! ")
        else:
            print("in this dic not student for this id ....")    
    elif choise=='4':

        

        for id ,info in students.items():
            print(f"===all list student ===\n  id :{id} \n name :{info["name"]} age : {info["age"]} \n marks:{info["marks"]}")
    elif choise=='exit':
        print("program are finised... ")
        break
    else:
        print("Invalid information you type hare ")


