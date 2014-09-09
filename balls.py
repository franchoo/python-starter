t = int(input())
for x in range(0,t):
    n,k = [int(i) for i in input().strip().split()]
    balls = []
    for y in range(0, n//2):
        balls.append(n-1-y)
        balls.append(y)
    if n % 2 == 1:
        balls.append(n//2)
    print(balls.index(k))