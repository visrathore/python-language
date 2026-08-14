def addition(*args): # here args is a tuple
    sum = 0
    for i in args:
        sum+=i

    print(sum)

addition(1,2,3,4,5)


def kAddition(**kargs): # here kargs is a dictionaries
    for i in kargs:
        print(f"{i}: {kargs[i]}")

kAddition(a=1, b=2, c=3)