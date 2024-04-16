def function_call_counter(func):
    count=0

    def wrapper_func(*args,**kwargs):
        nonlocal count
        count+=1
        result=func(*args,**kwargs)
        return count, result
    
    return wrapper_func

def my_function(x):
    return x*2

counter_my_function=function_call_counter(my_function)

print(counter_my_function(5))
print(counter_my_function(7))
print(counter_my_function(11))
