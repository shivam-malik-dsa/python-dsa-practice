def first_occurrances(arr,target):
    left = 0
    right = len(arr)-1
    result = -1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            result = mid
            right = mid-1
        
        elif arr[mid] < target:
            left = mid+1

        else:
            right = mid-1

    return result            
                
def last_occurrances(arr,target):
    left = 0
    right = len(arr)-1
    result = -1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            result = mid
            left = mid+1
        
        elif arr[mid] < target:
            left = mid+1

        else:
            right = mid-1

    return result

def count_occurrances(arr,target):
    first = first_occurrances(arr,target)

    if first == -1:
        return 0
    
    last = last_occurrances(arr,target)
    return (last - first) + 1
