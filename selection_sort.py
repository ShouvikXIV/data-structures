def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i,len(arr)):
            if(arr[j]<arr[min_idx]):
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

arr = [10,5,8,20,2,18]
selection_sort(arr)
print(arr)
