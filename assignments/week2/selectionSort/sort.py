arr = [3, 7, 25, 10, 5]

def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for k in range(i+1, len(arr)):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]
    return arr

print(bubbleSort(arr))

def insertionSort(arr):
    for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while key < arr[j] and j >= 0:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key 
    return arr

print(insertionSort(arr))


    

        

        
    
