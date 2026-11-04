
import random
import math
from itertools import combinations

def cost(s):
    return sum(s[i] == s[j] or abs(s[i]-s[j]) == abs(i-j)
               for i, j in combinations(range(4), 2))

def simulated_annealing(s):
    T = 100

    while T > 0.01:
        if cost(s) == 0:
            return s

        i, j = random.sample(range(4), 2)
        nxt = s[:]
        nxt[i], nxt[j] = nxt[j], nxt[i]

        delta = cost(s) - cost(nxt)

        if delta > 0 or random.random() < math.exp(delta / T):
            s = nxt

        print("State:", s, "Cost:", cost(s), "Temperature:", round(T, 2))
        T *= 0.95

    return s

initial = [3, 1, 2, 0]
result = simulated_annealing(initial)

print("\nFinal State:", result)
print("Final Cost:", cost(result))

if cost(result) == 0:
    print("Solution Found!")
else:
    print("Solution Not Found!")
