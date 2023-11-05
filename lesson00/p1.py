_, m = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    
    # error handling
    if l < 0 or r > len(arr) or l >= r:
        print("NOT FOUND")
    _min, _max = 1001, -1
    # base logic
    for i in range(l, r+1):
        _min = min(arr[i], _min)
        _max = max(arr[i], _max)
    if _min == _max:
        print("NOT FOUND")
    else: 
        print(_max)
