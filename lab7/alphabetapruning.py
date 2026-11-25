def alpha_beta(node, depth, alpha, beta, maximizing_player):

    if depth == 0 or isinstance(node, int):
        return node

    if maximizing_player:
        value = float('-inf')

        for child in node:
            value = max(value, alpha_beta(child, depth - 1,
                                          alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruned Branch: ",child)
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(value, alpha_beta(child, depth - 1,
                                          alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                print("Pruned Branch: ",child)
                break

        return value


# Main program
tree = [
    [3, 5],
    [6, 9],
    [1, 2],
    [0, -1]
]

depth = 2

result = alpha_beta(tree, depth, float('-inf'),
                    float('inf'), True)

print("Optimal value:", result)