def limit_call_function(func,limit):
    count=0

    def wrapped_func(*args,**kwargs):
        nonlocal count
        if count<limit:
            count+=1
            return func(*args,**kwargs)
        else:
            return "Limit reached.Further calls not allowed."
        
    return wrapped_func

def my_function(x):
    return x*2

limited_function=limit_call_function(my_function,2)

print(limited_function(5))
print(limited_function(7))
print(limited_function(11))
