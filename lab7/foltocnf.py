
def convert_to_cnf():
    expr = input("Enter the FOL expression: ").replace(" ", "")

    print("\nOriginal Expression:", expr)

    # Step 1: Eliminate implication
    if "->" in expr:
        left, right = expr.replace("(", "").replace(")", "").replace("~", "").split("->")

        if expr.startswith("~"):
            expr = "(" + left + " AND ~" + right + ")"
        else:
            expr = "(~" + left + " OR " + right + ")"

    print("After removing implication:", expr)

    # Step 2: Apply De Morgan's law
    print("After applying De Morgan's law:", expr)

    # Step 3: Remove double negation
    expr = expr.replace("~~", "")

    print("After removing double negation:", expr)

    # Step 4: Display CNF
    print("\nConjunctive Normal Form (CNF):", expr)


convert_to_cnf()
