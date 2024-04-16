def create_counter():
    count=0
    def counter():
        nonlocal count
        count +=1
        return count
    return counter

my_counter=create_counter()


print(my_counter())
print(my_counter())
print(my_counter())
