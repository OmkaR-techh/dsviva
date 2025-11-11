size=int(input("enter the size of hash table"))
hashT=[]
deleted = "<del>"
for i in range(size):
   hashT.append(None)
def hashfunction(key):
   return key%size
def insert(key):
    idx=hashfunction(key)
    start=idx
    while hashT[idx] not in (None,deleted):
       if hashT[idx]==key:
          print("already existed")

       idx=(idx+1)%size
       if idx==start:
          print("table fulll")
    hashT[idx]=key
def search(key):
    idx=hashfunction(key)
    start=idx
    while hashT[idx] not in (None,deleted):
       if hashT[idx]==key:
          
          return idx
       else :
          idx=(idx+1)%size
    print("not found")
def delete(key):
   idx=search(key)
   hashT[idx]="<del>"
def display():
   for i ,v in enumerate(hashT):
      print(f"{i}.{v}")
if __name__=="__main__":

  while(True):
    print("1.insert  2. delete 3.search 4.display 5.exit")
    option=int(input("enter an valid option"))
    if option==1:
      insert(int(input("enter key")))
    elif option==2:
      delete(int(input("enter  option to delete")))
    elif option==3:
      print("found at index", search(int(input("enter option to search"))))
    elif option==4:
      display()
    elif option==5:
      print("exiting")
      break
    else:
      print("enter an valid option")
