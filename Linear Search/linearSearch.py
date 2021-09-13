import time
numbers=[1,3,5,123,6,7,34,7,45,8]

def search(numbers,n):
    for i in range(len(numbers)):
        if numbers[i]==n:
            print(i)
            return True
    
    return False

n=123
place=0
start_time = time.time()
if search(numbers,n):
    print("found")
else:
    print("not found")
print("--- %s seconds ---" % (time.time() - start_time))
