size=int(input("enter the size of hash table"))
hashtable=[]
for i in range(size):
   hashtable.append([])
def hashfunction(key):
  return key%size
def insert(key,value):
  index=hashfunction(key)
  hashtable[index].append((key,value))
def search(key):
  index=hashfunction(key)
  chain=hashtable[index]
  for i ,(k,v) in enumerate (chain):
    if k==key:
      print(f"found at index {index} and has value{v}")
    else:
      print("not found")
def display():
  for i ,chain in enumerate(hashtable):
     if chain:
       
      print(f"{i}.{chain}")
     else:
       print(f"Null.null")

def delete(key):
   index=hashfunction(key)
   chain=hashtable[index]
   for i ,(k,v) in enumerate (chain):
    if k==key:
      chain.pop(i)
    
if __name__=="__main__":
   ##size=int(input("enter the size of hash table"))
   while True:
    print("1.insert")
    print("2.search")
    print("3.display")
    print("4.delete")
    print("5.exit")
    option=int(input("enter th option"))
    if option==1:
      key=int(input("enter the key"))
      value=input("enter the value")
      insert(key,value)
    elif option==2:
      key=int(input("enter the key"))
      search(key)
    elif option==3:
      display()
    elif option==4:
      key=int(input("enter the key"))
      delete(key)
    elif option==5:
      print("exiting the program")
      break
    else:
      print("Enter a valid option")
