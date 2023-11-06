def partition(pivot, array):
    e = g = 0
    for n in range(len(array)):
        if array[n] < pivot:
            temp = array[n]# memorise the < than pivot
            array[n] = array[g]# move the > pivot to current pos
            array[g] = array[e]# move the == to pivot to pos G
            array[e] = temp
            e+=1
            g+=1
        elif array[n] == pivot:
            array[n], array[g] = array[g], array[n]
            g+=1
    return e, len(array) - e
        
        
        

n = int(input())

arr = list(map(int, input().split()))
x = int(input())
result = partition(x, arr)
print("\n".join(map(str, result)))
