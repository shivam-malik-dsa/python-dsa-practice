def binary_recursive(arr,left,right,target):
    if left>right:
        return-1
    
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_recursive(arr,mid+1,right,target)
    else:
        return binary_recursive(arr,left,mid-1,target)
