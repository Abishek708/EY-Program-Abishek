''' print all the fibbonacci series that are divisible by 3 or 4 or 5'''
x = 0
n1 = 0
n2 = 1
nxt_num = n2
while x<10:
    if nxt_num%3==0 or nxt_num%4==0 or nxt_num%6==0:
        print(nxt_num, end=" ")
    x = x+1
    n1, n2 = n2, nxt_num
    nxt_num = n1 + n2
   
print()


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n)*fact(n-1)

fact(2)