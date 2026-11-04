
from itertools import product

def implies(a, b):
    return not a or b

def KB(P, Q, R):
    return (implies(Q, P) and
            implies(P, not Q) and
            (Q or R))

def check_entailment(query):
    for P, Q, R in product([False, True], repeat=3):
        if KB(P, Q, R) and not query(P, Q, R):
            return False, (P, Q, R)
    return True, None

print("P Q R | KB")

for P, Q, R in product([False, True], repeat=3):
    print(int(P), int(Q), int(R), "|", KB(P, Q, R))

queries = {
    "R": lambda P, Q, R: R,
    "R -> P": lambda P, Q, R: implies(R, P),
    "Q -> R": lambda P, Q, R: implies(Q, R)
}

for name, query in queries.items():
    result, counterexample = check_entailment(query)

    if result:
        print(name, ": Entailed")
    else:
        print(name, ": Not Entailed")
        print("Counterexample:", counterexample)
