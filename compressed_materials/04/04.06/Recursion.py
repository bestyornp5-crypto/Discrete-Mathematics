# 5! = 1*2*3*4*5

def fac1(n):
    result = 1
    if n == 1 or n == 0:
        return 1
    for i in range(1, n+1):
        result *= i
    return result


# 5! = 1*2*3*4*5
# 5! = 5*(4!) = 5*(4*(3!)) = 5*(4*(3*(2!))) = 5*(4*(3*(2*(1!)))) = 5*(4*(3*(2*1))) = 5*(4*(3*2)) = 5*(4*6) = 5*24 = 120
def fac2(n):
    if n == 1 or n == 0:
        return 1
    return n*fac2(n-1)


print(fac2(5))
print(fac2(990))