arr = [5, 4, 2, 3 ,1]

for i in range(len(arr)):
	min = i
	for j in range(i+1, len(arr)):
		if arr[min] > arr[j]:
			min = j
			
	arr[i], arr[min] = arr[min], arr[i]

for i in range(len(arr)):
	print("%d" %arr[i]),