
def Sum(n):
    if n > 0:
        return n + Sum(n-1)
    else:
        return 0



print(Sum(10))