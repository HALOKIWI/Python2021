def bubbleSort(lst):
    n = len(lst)
  
    for i in range(n):
  
        for j in range(0, n-i-1):
  

            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
lst = []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele)
  
bubbleSort(lst)
  
print ("Sorted array is:")
for i in range(len(lst)):
    print ("%d" %lst[i]), 