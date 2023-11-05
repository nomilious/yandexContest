def remove_zeros_from_end(arr):
    # Iterate through the array from the end
    i = len(arr) - 1
    while i >= 0 and arr[i] == 0:
        # Remove 0 from the end of the array
        arr.pop()
        i -= 1
    return arr


# Чтение входных данных
capacity = int(input())
n = int(input())
floors = [int(input()) for _ in range(n)]
floors = remove_zeros_from_end(floors)
n = len(floors)

time = 0

for i in range(n):
    time += (floors[i] // capacity) * 2 * (i+1)
    floors[i] = floors[i] % capacity
onBoard = 0
floor = n-1

while floor >= 0:
    if floors[floor] == 0:
        floor -=1
        continue
    if onBoard == 0:
        time += (floor+1)*2
    onBoard+=floors[floor]
    if onBoard > capacity:
        floors[floor] = onBoard % capacity
        onBoard = 0
    else:
        floors[floor] = 0
        floor-=1

print(time)
