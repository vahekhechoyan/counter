def  create_accumuliator(initial):
    total=initial
    def accumuliator(number):
        nonlocal total
        total+=number
        return total
    return accumuliator

my_accumuliator=create_accumuliator(0)

print(create_accumuliator(5))
print(create_accumuliator(7))
print(create_accumuliator(11))

