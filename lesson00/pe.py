n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0] * n  
prefix_sum[0] = arr[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
res = []

res.append(prefix_sum[- 1] - arr[0] * n)    
for i in range(1, n):
    temp = i * arr[i] - prefix_sum[i-1] + prefix_sum[- 1] - prefix_sum[i] - (n - 1 - i) * arr[i]
    res.append(temp)

print(*res)
