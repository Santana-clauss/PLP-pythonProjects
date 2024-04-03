def mod(x,y,n):
    result=1
    x=x%n
    while y>0:
        if y%2==1:
            result=(result*x)%n
        x=(x*x)%n
        y=y//2
    return result

print(mod(11,345,23))