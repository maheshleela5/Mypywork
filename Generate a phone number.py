import random

def generate_phone_number():
    x = random.randint(7,9)
    y = "+91-"
    num = str(x)

    for i in range(0,9):
        num = num + str(random.randint(0,9))
        k = y + num
    return  k


print(generate_phone_number())
print(generate_phone_number())
print(generate_phone_number())
