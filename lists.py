strList = ['Apple', 'Banana', 'Kiwi', 'Apple']
numList = [1,2,3,4,52,3]
boolList = [True, False, False, True]
mixList=[1,'Apple', True, False, 3]

# Length
print(len(strList)) 

# Create list using list() constructor
listConst = list(('Apple', 1,3,True))
print(listConst)

"""Accessing List Items"""

# Access the list items using index
print(strList[1]) 
print(strList[-3]) 

# Slicing - return new list
print(strList[1:4]) 
print(strList[:2])
print(strList[1:]) 

# Check if item exists
if 'Apple' in strList:
    print('Yes, Apple is present')

"""Changing List Items"""

# Change one item
strList[1] = 'Gems'
print(strList)

# Change range
strList[1:3] = ["blackcurrant", "watermelon"]
numList[1:3] = ["blackcurrant"]
print(strList)
print(numList)

# Insert item without changing existing values
numList.insert(1, 'Vishal')
print(numList)

# Append item
numList.append('Singh')
print(numList)

# Extend - to merge two lists - The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# remove() - remove the element from list
thislist.remove('banana')
print(thislist)

# pop() - remove the specified index
# pop() - if no index given remove the last element
thislist.pop(1)
print(thislist)

# del - also remove from specified index
# del - also delete list completely
# del thislist
del thislist[1]
print(thislist)

# clear() - clear the list but keep it
thislist.clear()
print(thislist)

"""Loop List"""

for x in numList:
    print(x)

for x in range(len(numList)):
    print(numList[x])