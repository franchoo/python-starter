def linear(a,x,b,y):
    return -a*x+b*y
def isInside(x1,y1,x2,y2,x,y):
    return (x1<=x<=x2 or x2<=x<=x1) and (y1<=y<=y2 or y2<=y<=y1)
t = int(input())
for n in range(0,t):
    x1,y1,x2,y2,xm,ym = [int(i) for i in input().strip().split()]
    X,Y = x1, y1
    a,b = y2-y1, x2-x1
    c = linear(a,x1,b,y1)
    d = linear(a,xm,b,ym)
    if d != 0:
        X = xm * c / d
        Y = ym * c / d
        print(('YES', 'NO')[isInside(x1,y1,x2,y2,X,Y) and isInside(0,0,xm,ym,X,Y)])
    else:
        if xm==0: isOnTop = xm/ym == x1/y1
        else:     isOnTop = ym/xm == y1/x1
        print(('YES', 'NO')[isOnTop and isInside(0,0,xm,ym,X,Y)])