
# Selection Sort

def selection_sort(arr):
    for i in range(len(arr)):
        sort=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[sort]:
                sort=j
            
        arr[i],arr[sort]=arr[sort],arr[i]


arr=[64,25,12,22,11]

print(f'Original Array : {arr}')

selection_sort(arr)
print(f'Sorted Array : {arr}')