"""
Alright, Voyager, here's your next mission. Your objective is to identify all the elements in a list of integers that are repeating their ugly mugs more than once. They could be negative and in no particular order, just to keep you on your toes!

Your final output should be a list of these duplicate numbers. The order? Doesn't matter! Maybe they were just in the wrong place at the wrong time.

All clear? Time's a-wasting, let's crack on, space cowboy!
"""


# returning duplicates
def repeating_elements(nums):
    values=set()
    for i in nums:
        count=0
        for j in nums:
            if abs(i)==abs(j):
                count+=1
                if count>=2:
                    values.add(i)
    return list(values)


# returning duplicates using set
# 
def repeating_elements_using_set(nums):
    seen=set()
    duplicates = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            duplicates.add(i)
    
    return sorted(list(duplicates))

# print(repeating_elements_using_set([9, 8, 7, 8, 7, 6, 5])) 
# print(repeating_elements_using_set([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
# print(repeating_elements_using_set([1, 2, 3, 4, 5]))        # expected output : []

# print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
# print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
# print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []


# returning unique items


# def exclusive_products(inventory1, inventory2):
    
#     for a,b in enumerate(inventory1):

#         for j,k in enumerate(inventory2):

#             # print(i.upper(), j.upper())
#             if b.capitalize() == k.capitalize():
#                 inventory1[a]=""
#                 inventory2[j]=""
#                 # break

#     first_store=[b.upper()  for b in inventory1 if len(b)>0]
#     second_store=[k.upper() for k in inventory2 if len(k)>0] 
#     return sorted(first_store),sorted(second_store)

# # inventory1 = ["Shirt", "Jeans", "Hat"]
# # inventory2 = ["jeans", "Belt", "Boots"]
# # print(exclusive_products(inventory1, inventory2))
# # # Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

# # inventory1 = ["T-Shirt", "hoodie", "Backpack"]
# # inventory2 = ["Backpack", "Hoodie", "t-shirt"]
# # print(exclusive_products(inventory1, inventory2))
# # # Expected output: ([], [])

# # inventory1 = []
# # inventory2 = ["Dress", "Skirt", "Coat"]
# # print(exclusive_products(inventory1, inventory2))
# # Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])



# # finding unique items

# def find_unique_string(words):
#     seen=set()
#     duplicates=set()
#     for word in words:
#         if word not in seen:
#             seen.add(word)
#         else:
#             duplicates.add(word)

#     # print(seen,duplicates)
#     unique=seen.difference(duplicates)

#     for words in seen:
#         print(word,unique)
#         if words in sorted(unique,reverse=True):
#             return words
#     return ""

# print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
# print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
# print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
# print(find_unique_string([]))  # It should print: ''


# finding anagrams

# def find_anagram_words(list_1, list_2):
#     value1=list_1[0]
#     sep_value="".join([i for i in value1])
#     container=set()
#     value2=[i for i in list_2]
#     for i in sep_value:
#         for j in value2:
#             print(j)
#             if i in list(j):
#                 # print(i)
#                 container.add(j)
#     # return container

# def find_anagram_words(list_1, list_2):
#     value1=list_1
#     # sep_value="".join([i for i in value1])
#     # print(sep_value)
#     value2=[i for i in list_2]
#     values=[]
#     for i in value2:
#         counter=0
#         for j in list_1:
#             if j in i:
#                 counter+=1            
#         if counter==len(j) and len(i)==counter:
#             values.append(i)
#             continue
#     return values
def find_anagram_words(list_1, list_2):
    # Initialize result list
    anagrams = set()
    
    # Process each word in list_1
    for word in list_1:
        # Convert to sorted string for comparison
        sorted_word = ''.join(sorted(word))
        
        # Check each word in list_2
        for candidate in list_2:
            # Sort the candidate word
            sorted_candidate = ''.join(sorted(candidate))
            
            # Compare the sorted strings
            if sorted_word == sorted_candidate:
                anagrams.add(word)
    
    return list(anagrams)
print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []