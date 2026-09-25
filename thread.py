import time
import threading

# concept the thread and multithread 

def welcome(skills):
    for index,val in enumerate(skills):
        time.sleep(2)
        print(f"the skills index {index} the values are is {val}")

def welcome(skills):
    for index,val in enumerate(skills):
            time.sleep(2)
            print(f"the skills index {index} the values are is {val}")
    

def welcome(skills):
    for index,val in enumerate(skills):
            time.sleep(2)
            print(f"the skills index {index} the values are is {val}")
    

starting=time.time()

firstlist=["html","css","javascript"]
welcome(firstlist)
secondslist=["Agentic AI","gen AI","AI/ML"]
welcome(secondslist)
thirdlist=["fullstack","marnstack","devops"]
welcome(thirdlist)

endingtime=time.time()


print("program excution time is ",endingtime-starting)

























