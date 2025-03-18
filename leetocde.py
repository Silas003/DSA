# maximum product subarray

def product_subarry(arr):
    values={}
    for i in range(len(arr)-1):
        mul=arr[i]*arr[i+1]
        values[mul]=[]
        values[mul].append(arr[i])
        values[mul].append(arr[i+1])

    maxi=max(values.keys())
    
    for k,v in values.items():
        if k == maxi and maxi >0:
            return v
        return 0



array=[2,3,-2,4]
array=[-2,0,1]
# print(product_subarry(array))

# product of array except self
array=[1,2,3,4]

