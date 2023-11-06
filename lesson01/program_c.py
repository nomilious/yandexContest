def merge(slice1, slice2):
    result = []
    ind1 = ind2 = 0
    n, m = len(slice1), len(slice2)
    while ind1 < n or ind2 < m:
        if ind2 >= m or (ind1< n and  slice1[ind1] <= slice2[ind2]):
            result.append(slice1[ind1])
            ind1 += 1
        elif ind1 >= n or (ind2 < m and slice1[ind1] > slice2[ind2]):
            result.append(slice2[ind2])
            ind2 += 1
    return result
def main():
    input()
    slice1 = list(map(int, input().split()))
    input()
    slice2 = list(map(int, input().split()))
    print(*merge(slice1, slice2))

if __name__ == "__main__":
    main()
