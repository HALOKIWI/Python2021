import time
list=[0,1,2,3,4,5,9,7,8,9]
def linear_search(list, n):
    start_time = time.time()
    arr=[]
    for i in range (len(list)):
        if list[i]==n:
            arr.append(i)
    print("--- %s seconds ---" % (time.time() - start_time))
    return arr

print(linear_search(list,9))
