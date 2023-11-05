t = int(input())
for i in range(t):
    n,a,b = map(int, input().split())
    groups = n//a
    print("YES" if n%a <= groups*(b-a) else "NO")
