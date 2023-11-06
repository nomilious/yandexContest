def partition(array, l, r, pivot):
    equal = great = l
    for n in range(l, r):
        if array[n] < pivot:
            temp = array[n]
            array[n] = array[great]
            array[great] = array[equal]
            array[equal] = temp
            equal += 1
            great += 1
        elif array[n] == pivot:
            array[n], array[great] = array[great], array[n]
            great += 1
    return equal, r-equal

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Check if x is in the array; if not, append it to the end of the array
result = partition(arr, 0, len(arr), x)

print("\n".join(map(str, result)))
