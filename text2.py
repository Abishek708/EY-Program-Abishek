count = 100
kilometer = 1000.0
name = 'rahul'

print(count, kilometer, name)

def fact(n):
    if n==0 or n==1:
        return n
    else:
        return fact(n)*fact(n-1)

fact(5)