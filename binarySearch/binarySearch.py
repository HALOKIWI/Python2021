def binary_search(arr, low, high, target):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == target:
            return mid
 
 
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
 
        else:
            return binary_search(arr, mid + 1, high, target)
 
    else:
        return -1
 
# Test array
arr = [ 3, 10, 40, 80, 90,91,92,100,110,150 ]
target = 150
 
# Function call
result = binary_search(arr, 0, len(arr)-1, target)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")