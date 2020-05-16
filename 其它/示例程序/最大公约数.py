def yue(x,y):
    x,y=max(x,y),min(x,y)
    while y:
        yu=x%y
        print('1',end=' ')
        print(x,y,yu)
        x=y
        print('2', end=' ')
        print(x, y, yu)
        y=yu
        print('3', end=' ')
        print(x, y, yu)
    return x
print(yue(4,6))
