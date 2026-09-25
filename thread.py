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



# creating the multithread 

start=time.time()

mythread_1=threading.Thread(
     target=welcome,
     args=(firstlist,)
)
mythread_2=threading.Thread(
     target=welcome,
     args=(secondslist,)
)

mythread_3=threading.Thread(
     target=welcome,
     args=(thirdlist,)
)

mythread_1.start()
mythread_2.start()
mythread_3.start()

mythread_1.join()
mythread_2.join()
mythread_3.join()
end=time.time()

print(f"apply the  multithreading and program exuction time see the time   {end-start}  ")































