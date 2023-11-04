k = int(input()) # capacity of the lift

n = int(input()) # number of levels

arr = []
for i in range(n):
    arr.append(int(input()))
    
res = arr[0] // k * 2 + arr[1] // k * 2 * 2 + arr[2] // k * 2 * 2 * 2
res += (arr[0]%k+arr[1]%k) // k * 4
res = 0
for i in range(n):
    res+= arr[i] // k * 2**(i+1)
    arr[i]= arr[i]%k
    
dk  = 0
dt = 0
for i in range(n):
    dt+=1
    if a[i] == 0:
        continue
    dk += abs(arr[i]- dk)
    arr[i] = 0
    if all([a[j] == 0 for j in range(len(a[i+1:]))):
        break
    if dk 
res+= dk
