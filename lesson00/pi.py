sequence = input()

brackets = {"(": ")", "{": "}", "[": "]"}
stack = []

for i in range(len(sequence)):
    if sequence[i] in brackets.keys(): # is opening brackets
        stack.append(sequence[i])
    else:# closing brackets
        if len(stack) == 0 or sequence[i] != brackets.get(stack.pop()):
            print("no")
            break
else: 
    print("yes" if len(stack) == 0 else "no")
