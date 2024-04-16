def memorize(func):
    cache={}

    def memrized_func(*args):
        if args in cache:
            return cache[args]
        result=func(*args)
        cache[args]=result
        return result
    
    return memrized_func

def expensdive_function(n):
    print("Calculating...")
    return n*n

memrized_expesive_function=memorize(expensdive_function)

print(memrized_expesive_function(5))
print(memrized_expesive_function(7))
