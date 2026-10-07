G = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 0]]

P = [[1, 2, 3],
     [0, 4, 6],
     [7, 5, 8]]

M = [(-1, 0, "Up"), (1, 0, "Down"),
     (0, -1, "Left"), (0, 1, "Right")]


def search(b, r, c, d, path, prev):
    if b == G:
        return path[:]
    if d == 0:
        return None

    for dr, dc, name in M:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3 and (nr, nc) != prev:
            b[r][c], b[nr][nc] = b[nr][nc], b[r][c]
            path.append((name, [row[:] for row in b]))
            result = search(b, nr, nc, d - 1, path, (r, c))
            if result is not None:
                return result
            path.pop()
            b[r][c], b[nr][nc] = b[nr][nc], b[r][c]
    return None


def ids(b):
    r, c = next((i, j) for i in range(3)
                for j in range(3) if b[i][j] == 0)
    d = 0
    while True:
        print("Depth limit:", d)
        result = search(b, r, c, d, [], (-1, -1))
        if result is not None:
            print("\nGoal found!")
            for move, state in result:
                print("\nMove:", move)
                for row in state:
                    print(*row)
            print("\nTotal moves:", len(result))
            return
        d += 1


print("Initial state:")
for row in P:
    print(*row)

ids(P)
