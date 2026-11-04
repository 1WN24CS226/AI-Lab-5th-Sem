
import heapq

start = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal  = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def h(s):
    return sum(s[i] != goal[i] for i in range(9) if s[i] != 0)

def astar():
    pq = [(h(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, s = heapq.heappop(pq)

        if s == goal:
            path = []
            while s is not None:
                path.append(s)
                s = parent[s]
            for state in path[::-1]:
                for i in range(0, 9, 3):
                    print(*state[i:i+3])
                print()
            return

        z = s.index(0)

        for nz in (z-3, z+3, z-1, z+1):
            if not 0 <= nz < 9:
                continue
            if abs(nz // 3 - z // 3) + abs(nz % 3 - z % 3) != 1:
                continue

            t = list(s)
            t[z], t[nz] = t[nz], t[z]
            t = tuple(t)
            ng = g + 1

            if ng < cost.get(t, float('inf')):
                cost[t] = ng
                parent[t] = s
                heapq.heappush(pq, (ng + h(t), ng, t))

astar()
