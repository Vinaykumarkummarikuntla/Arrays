// 
def largest( arr, n):
    largest = arr[0]
    for i in range(1,n):
        if arr[i] > largest:
            largest = arr[i]
    return largest
    


