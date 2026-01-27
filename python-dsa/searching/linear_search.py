def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return "found at index->",i
    return -1
