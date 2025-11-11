def linear(arr,cid):
  n=len(arr)
  for i in range(n):
     if arr[i]==cid:
       return i
  return -1

def binary(arr,cid):
   low=0
   high=len(arr)-1
   while low<high:
      mid=low+high-low//2
      if arr[mid]==cid:
       return mid
      elif arr[mid]<cid:
        low=mid+1
      else:
        high=mid-1
   return -1

 
if __name__=="__main__":
    arr=[]
    size =int(input("enter the total number of customers :"))
    print(" enter elements in array")
    for i in range(size):
      e=int(input(f"enter customer id at index {i} :"))
      arr.append(e)
    cid=int(input("enter the customer id  to search :"))
    index=linear(arr,cid)
    if index ==-1:
      print("not found")
    else:
      print(f"found at index {index}")
      print("found by linear search")
    index=binary(arr,cid)
    if index ==-1:
      print("not found")
    else:
      print(f"found at index {index}")
      print("found by binary search")
