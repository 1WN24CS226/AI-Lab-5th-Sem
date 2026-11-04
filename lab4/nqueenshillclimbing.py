
from itertools import combinations

def cost(s):
    return sum(s[i] == s[j] or abs(s[i]-s[j]) == abs(i-j)
               for i, j in combinations(range(4), 2))

def hill_climbing(s):
    while True:
        c = cost(s)
        best, bc = s, c

        for i, j in combinations(range(4), 2):
            t = s[:]
            t[i], t[j] = t[j], t[i]
            if cost(t) < bc:
                best, bc = t, cost(t)

        print(s, "Cost =", c)

        if bc >= c:
            return s

        s = best

s = [3, 1, 2, 0]
result = hill_climbing(s)

print("Final state:", result)
print("Final cost:", cost(result))
