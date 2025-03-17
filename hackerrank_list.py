


# Complete the 'plusMinus' function below.

# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    negatives=[]
    positives=[]
    zeroes=[]
    dict1={}
    dict1["sum_p"]=0
    dict1["sum_n"]=0
    dict1["sum_z"]=0
    for i in arr:
        if i<0:
            negatives.append(i)
        
        elif i==0:
            zeroes.append(i)
            
        else:
            positives.append(i)
            
    dict1["sum_n"]=len(negatives)/len(arr)
    dict1["sum_z"]=len(zeroes)/len(arr)
    dict1['sum_p']=len(positives)/len(arr)

    for key,val in dict1.items():
        formatted = format(val, ".6f")  # Use format() for formatting
        print(formatted)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(arr)
    plusMinus(arr)


# minmax sum

def miniMaxSum(arr):
    sumit=[]
    results=sum(arr)
    print(results)
    for i in arr:
        new_v=results-i
        print(new_v)
        sumit.append(new_v)
    print(sumit)
    print(min(sumit),"",max(sumit))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# timeconversion


def timeConverion(s):
    hour=s[0:2]
    day=s[-2:]
    if day=="PM":
        hour=int(hour)+12
    elif day=="AM" and hour=="12":
        hour="00"
    print(f"{hour}{s[2:-2]}")

timeConverion("11:00:00AM")


# buying and selling
def buySell(arr:list[int]):
    profit=0
    buy=arr[0]
    for i in range(0,len(arr)-1):
        if  arr[i] > arr[i+1]:
            buy=arr[i+1]

        profit+=arr[i+1]-buy

        buy=arr[i+1]
    
    return profit


prices = [7, 1, 5, 3, 6, 4]
prices1 =[1,2,3,4,5]
prices2=[7,6,4,3,1]

print(buySell(prices))
print(buySell(prices1))
print(buySell(prices2))

# rotating numbers
def rotateNums(nums:list[int],k:int)->None:
    # mod=k%len(nums)
    # if k > len(nums):
    #     nums=[nums[-1]]+nums[:-1]

    # else:
    #     lastv=nums[-k:]
    #     first=nums[:-k]
    #     final=lastv+first
    n = len(nums)
    k = k % n  # Normalize k to handle cases where k > n

    # Split the array into two parts
    lastv = nums[-k:]  # Last k elements
    first = nums[:-k]  # All elements except the last k

    # Clear the original array
    nums.clear()

    # Rebuild the array in-place
    nums.extend(lastv)  # Add the last k elements
    nums.extend(first)  # Add the remaining elements

    print(nums)




nums = [1,2,]
rotateNums(nums,3)


# duplicates

def verify_duplicates(nums):
    seen=set()
    duplicates=set()
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            duplicates.add(i)
    
    return True if duplicates&seen else False



nums = [1,2,3,4]

print(verify_duplicates(nums))


# appearing onces

def appearonces(nums):
    seen=set()
    duplicates=set()

    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            duplicates.add(i)
    
    k=seen.difference(duplicates).pop()

    
    return k


nums1 = [2,2,1]

nums2 = [4,1,2,1,2]

appearonces(nums1)
appearonces(nums2)


# intersection of arrays

def intersection(nums1,nums2):

    # if len(nums1) > len(nums2):
    #     final=[i for i in nums2 if i in nums1]
    # else:
    #     final=[i for i in nums1 if i in nums2]
    
    # return final
    final=[]
    seen=set()
    if len(nums1) > len(nums2):
        for i in nums2:
            seen.add(i)
            if i in nums1 and i in seen:
                final.append(i)
        
        return final[:1] if len(final)==len(nums2) else final
    else:
        for i in nums1:
            seen.add(i)
            if i in nums2 and i  in seen:
                final.append(i)

        return final[:1] if len(final)== len(nums1) else final


nums1 = [2,2,1]

nums2 = [4,1,2,1,2]

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# nums1=[1,2,2,1]
# nums2=[2]
# nums1=[3,1,2]
# nums2=[1,1]
print(intersection(nums1,nums2))


# minimal index

def minimal_index(arr):
    seen = []
    for i,j in enumerate(arr):
        if j  not in seen:
            seen.append((j,i))

    for i in sorted(seen):
        print(i)

a=[2,3,5,3,2]

minimal_index(a)


def minimal(arr):
    va={}
    minimum:int
    for a,b in enumerate(arr):
        if b>=va:
            return b
        va[b]=a
    return -1

            

def firstDuplicate(a):
    """
    Returns the first duplicate number in the array `a` with the smallest second occurrence index.
    If no duplicates exist, returns -1.
    """
    seen = {}  # Dictionary to store elements and their indices

    for index, value in enumerate(a):
        if value in seen:
              # If the element is already in the dictionary
            return value   # Return the first duplicate
        seen[value] = index  # Store the element and its index

    # print(seen)
    return -1  # If no duplicates are found
a=[2,3,4,5,6,2,8,1,4,5,2,4,31,53,64,2,3,6,8,0,5]

print(minimal(a))
print(firstDuplicate(a))


# replace values

a=input(int())
b=input(int())

a=b,b=a


# significant figures

def significant(nums:list[int]):
    new_nums=int("".join([str(i) for i in nums]))
    new_nums+=1

    value=[]
    for i in str(new_nums):
        value.append(int(i))
    print(value)
significant([9])


# replacing non zero values

def replacement(nums:list[int]):

    for i in range(len(nums)-1):
        j=i+1    
        for j in range(len(nums)):
            temp:int
            if nums[j] == 0:
                temp=nums[j]
                nums[i],nums[j]=temp,nums[i]

    print(nums)
replacement([1,0,2,3,0,4,5,0])


# two sums

def twoSum(nums: list[int], target: int) -> list[int]:

    all=[]
    for a,b in enumerate(nums):
        for j,k  in enumerate(nums):
            if b+k == target:
                all.append([a,j])

    return all[1]


[-1,-2,-3,-4,-5]
print(twoSum([3,2,4],6))
print(twoSum([-1,-2,-3,-4,-5],-8))

# rotate a 2d array

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def rotate(matrix):
    total=[]
    for i in range(0,len(matrix)):
        first=[]
        for j in range(0,len(matrix)):
            first.append(matrix[j][i])

        total.append(first[::-1])
    
    print(total)
rotate(matrix=matrix)

# reverse integer

def reverseInt(x:int)->int:
    if x > 0:
        stri=str(x)
        rev=stri[::-1]
        return int(rev)
    else:
        stri=str(x)
        rev=stri[len(stri):0:-1]
        return int("-"+rev)


reverseInt(-123)

# first non repeating character

def firstNonRepeatingCharacter(s: str) -> int:
    seen={}
    for char in s: 
        seen[char]=seen.get(char,0)+1
    
    print(seen)
    for i,char in enumerate(s):
        if seen[char]==1:
            return i
    return -1
print(firstNonRepeatingCharacter("aabb"))
