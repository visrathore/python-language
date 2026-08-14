def decorate(fun):
    def wrapper(*args, **kargs): # instead of wrapper(a,b) use args and kargs to accept any kind of data
        print('First')
        fun(*args, **kargs)
        print('Last')
    return wrapper

@decorate
def addition(a,b):
    print(f"Total: {a+b}")

addition(1,2)