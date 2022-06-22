def bubble_sort(arr):
    for i in range(len(arr)-1):
        l = 0
        r = l+1
        while(r!=len(arr)-i):
            if arr[l]>arr[r]:
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
            l+=1
            r+=1

arr = [10,2,8,7]
bubble_sort(arr)
print(arr)