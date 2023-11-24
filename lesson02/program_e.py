START = '^'
FINISH = '$'
DELIMITER = '#'


def main():
    s = input()
    if not s:
        print(0)
    else:
        print(count_palindromic_substrings(s) + len(s))


def get_extended_string(s):
    n = len(s)
    if n == 0:
        return START + FINISH
    extended = [START] + [DELIMITER + s[i] for i in range(n)] + [DELIMITER + FINISH]
    return ''.join(extended)


def count_palindromic_substrings(s):
    text = get_extended_string(s)
    n = len(text)
    dp = [0] * n
    center = 0
    radius = 0
    
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if radius > i:
            dp[i] = min(radius - i, dp[mirror])
        else:
            dp[i] = 0
        
        while text[i + 1 + dp[i]] == text[i - 1 - dp[i]]:
            dp[i] += 1
        
        if i + dp[i] > radius:
            center = i
            radius = i + dp[i]
    
    total = 0
    for i in range(n - 1):
        total += dp[i] // 2
    return total


if __name__ == "__main__":
    main()
