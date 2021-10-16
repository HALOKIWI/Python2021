def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        t = i
        for j in range(i+1, n):
            if arr[t] > arr[j]:
                t = j
                arr[i], arr[t] = arr[t], arr[i]



arr = [5,3,2]
selectionSort(arr)


print(arr)