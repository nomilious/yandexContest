import random as rand
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
    return equal

def quickSort(array, l,r):
    if l < r:
        x = array[rand.randint(l,min(len(array)-1,r))]
        p = partition(array,l,r, x)
        quickSort(array, l, p)
        quickSort(array, p+1, r)
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
n = int(input())
arr = list(map(int, input().split()))
if not is_sorted(arr):
    quickSort(arr, 0, n)
print(*arr)
