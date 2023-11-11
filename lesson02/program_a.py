xlen = []
hash = []
x = 257
p = 10 ** 9 + 7


def preparation(string):
    global hash, xlen
    hash.append(0)
    xlen.append(1)
    # fill arrays
    for i in range(len(string)):
        hash.append((hash[i] * x + ord(string[i])) % p)
        xlen.append((xlen[i] * x) % p)


def is_equal(string, from1, from2, length):
    # hash of first and second substrings
    first_substr = (hash[from1 + length] + hash[from2] * xlen[length]) % p
    second_substr = (hash[from2 + length] + hash[from1] * xlen[length]) % p
    return first_substr == second_substr


def main():
    string = input()
    queries = int(input())
    preparation(string)
    
    for i in range(queries):
        k, from1, from2 = map(int, input().split())
        if is_equal(string, from1, from2, k):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
