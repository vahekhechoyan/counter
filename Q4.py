def power_of(exp):
    def power(x):
        return x** exp
    return power
square=power_of(2)
cube=power_of(3)

print(square(5))
print(cube(5))
