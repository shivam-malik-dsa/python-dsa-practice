def next_smaller_element(arr):
    n=len(arr)
    stack=[]
    result= [-1] * n

    for i in range(n):
        
        while stack and arr[i] < arr[stack[-1]]:
            index= stack.pop()
            result[index]= arr[i]
        
        stack.append(i)
    
    return result
