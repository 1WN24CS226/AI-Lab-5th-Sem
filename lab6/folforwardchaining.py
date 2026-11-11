def is_variable(x):
    return isinstance(x, str) and x.startswith('?')

def substitute(term, theta):
    while is_variable(term) and term in theta:
        term = theta[term]
    return term

def unify(x, y, theta):
    if theta is None:
        return None

    x = substitute(x, theta)
    y = substitute(y, theta)

    if x == y:
        return theta

    if is_variable(x):
        theta[x] = y
        return theta

    if is_variable(y):
        theta[y] = x
        return theta

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None

        for a, b in zip(x, y):
            theta = unify(a, b, theta)
            if theta is None:
                return None

        return theta

    return None

def match(premises, facts, theta=None):
    if theta is None:
        theta = {}

    if not premises:
        yield theta
        return

    first = premises[0]
    remaining = premises[1:]

    for fact in facts:
        new_theta = unify(first, fact, theta.copy())

        if new_theta is not None:
            yield from match(remaining, facts, new_theta)

def apply_substitution(sentence, theta):
    return tuple(substitute(x, theta) for x in sentence)

def forward_chaining(KB, rules, query):

    iteration = 1

    while True:
        new_facts = set()

        print("\nIteration:", iteration)

        for premises, conclusion in rules:

            for theta in match(premises, KB):

                inferred = apply_substitution(conclusion, theta)

                if inferred not in KB:
                    new_facts.add(inferred)
                    print("Inferred:", inferred)

        if not new_facts:
            break

        KB.update(new_facts)
        iteration += 1

    print("\nFinal Knowledge Base:")
    for fact in sorted(KB):
        print(fact)

    if query in KB:
        print("\nGOAL PROVED:", query)
        return True
    else:
        print("\nGOAL NOT PROVED:", query)
        return False

KB = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
}

rules = [

 
    (
        [
            ("American", "?p"),
            ("Weapon", "?q"),
            ("Sells", "?p", "?q", "?r"),
            ("Hostile", "?r")
        ],
        ("Criminal", "?p")
    ),


    (
        [("Missile", "?x")],
        ("Weapon", "?x")
    ),



    (
        [("Enemy", "?x", "America")],
        ("Hostile", "?x")
    ),


    (
        [
            ("Missile", "?x"),
            ("Owns", "A", "?x")
        ],
        ("Sells", "Robert", "?x", "A")
    )
]


query = ("Criminal", "Robert")
 
forward_chaining(KB, rules, query)
