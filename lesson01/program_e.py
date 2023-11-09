def radix_sort(strings, length):
    buckets = [[] for _ in range(10)]
    for i in range(length-1, -1, -1):
        for string in strings:
            digit = int(string[i])
            buckets[digit].append(string)
        strings = []
        print_info(length-i, buckets)
        for bucket in buckets:
            strings.extend(bucket)
            bucket.clear()
    return strings

def print_info(phase, buckets):
    print("**********")
    print(f"Phase {phase}")
    for ind, bucket in enumerate(buckets):
        print(f"Bucket {ind}:", ", ".join(bucket) or "empty")


def main():
    n = int(input())
    arr = [input().strip() for i in range(n)]
    max_length = len(arr[0])
    
    print("Initial array:")
    print(", ".join(arr))
    
    sorted_strings = radix_sort(arr, max_length)
    
    print("**********")
    print("Sorted array:")
    print(", ".join(sorted_strings))


if __name__ == "__main__":
    main()
