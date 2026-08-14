a = [2,3,4,5,6]

def multiply(x):
    return x*2

newResult = map(multiply, a)
result = map(lambda x : x*2, a) #it will return an object so convert it to list to print

print(list(result))
print(list(newResult))

b = [1,2,3,4,5,6,7,8,9]
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

filterResult = filter(even, b)
print(list(filterResult))