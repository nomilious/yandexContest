def prefix_function(string):
    p = [0]
    for i in range(1, len(string)):
        j = p[i - 1]
        
        while j > 0 and string[i] != string[j]:
            j = p[j - 1]
        
        p.append(
            j + 1
            if string[i] == string[j]
            else j
        )
    return p


def main():
    string = input()
    p = prefix_function(string)
    res = len(string) - p[-1]
    print(res)


if __name__ == "__main__":
    main()
