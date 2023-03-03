import math
"""print(math.pi)
print(math.e)
print(math.sqrt(256))
print(math.factorial(10))
"""
def rec_dact(num):
    if type(num) != int:
        raise TypeError("number is not integer")
    if num<=0:
        raise ValueError("number is smallest null")
    if num==1:
        return 1
    return rec_dact(num-1)*(num)

print(rec_dact(10))