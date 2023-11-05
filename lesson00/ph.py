def get_solved_people(a,n):
    main = a//n
    main += 1 if a%n != 0 else 0
    return main

a = int(input())
b = int(input())
n = int(input())

# assuming that in group a everyone solved 1 task
# and in b - n tasks
print("Yes" if a > get_solved_people(b,n) else "No")
