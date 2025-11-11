arr=[]
value=int(input("enter the number of elements in array"))
for i in range(value):
      num=int(input("enter number "))
      arr.append(num)
x=len(arr)
def bubble():
   for i in range(x-1):
      for j in range(x-i-1):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
def selection():
   for i in range(x-1):
      min=i
      for j in range(i+1,x):
         if arr[min]>arr[j]:
            min=j
         arr[i],arr[min]=arr[min],arr[i]
def show():
   for i in range(x):
      if i!=x-1:
        print(arr[i],"",end="")
      else:
         print(arr[i])
      
if __name__=="__main__":
  
   bubble()
   show()
   print("after bubles sort")
   selection()
   show()
   print(" after selection")
