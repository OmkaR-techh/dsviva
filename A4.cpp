queue=[]
def add(event):
    queue.append(event)
    print("event is added succesfully")


def process():
    a=queue.pop(0)
    print(f"{a} event is being processed")

def display():
    v=1
    for i in queue:
        print (f"{v}  {i}")
        v+=1
        
def cancel(event):
   queue.remove(event)

if __name__=="__main__":
   print("Welcome in student management system")
   while True:
       print("1.add event")
       print("2.process event") 
       print("3.cancel event")
       print("4.display") 
       print("5.exit") 
       value=int(input("enter the option"))
       if value==1:
           a1=input("enter element to add")
           add(a1)
       elif value==2:
           process()
       elif value==3:
           a2=input("enter element to cancel")
           cancel(a2)
       elif value==4:
           display()
       elif value==5:
           print("exiting")
           break
       else :
          print("enter a valid option")
       
           
            
