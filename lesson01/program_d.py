def merge(slice1, slice2):
    result = []
    ind1 = ind2 = 0
    n, m = len(slice1), len(slice2)
    while ind1 < n or ind2 < m:
        if ind2 >= m or (ind1 < n and  slice1[ind1] <= slice2[ind2]):
            result.append(slice1[ind1])
            ind1 += 1
        elif ind1 >= n or (ind2 < m and slice1[ind1] > slice2[ind2]):
            result.append(slice2[ind2])
            ind2 += 1
    return result

def sort(array):
    if len(array) <= 1:
        return array
    n = len(array)
    k = round(n / 2)
    # mergeSort left
    slice1 = sort(array[:k])
    # mergeSort right
    slice2 = sort(array[k:])
    
    return merge(slice1, slice2)
    

def main():
    input()
    arr = list(map(int, input().split()))
    res = sort(arr)
    print(*res)


if __name__ == "__main__":
    main()
