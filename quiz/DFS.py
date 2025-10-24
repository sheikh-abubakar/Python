def dfs(cube):
    n = len(cube)
    m = len(cube[0])

    start = (0, 0)
    goal = (n - 1, m - 1)

    if cube[0][0] == 1 or cube[n - 1][m - 1] == 1:
        return -1

    stack = [[start]]     # DFS me stack use hota hai (LIFO)
    visited = [start]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(stack) > 0:
        # 🌀 Last path nikal lo (LIFO)
        path = stack.pop()
        x, y = path[-1]
        if (x, y) == goal:
            for (px, py) in path:
                cube[px][py] = "F"
            return cube # Path mil gaya

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if cube[nx][ny] == 0 and (nx, ny) not in visited:
                    new_path = path + [(nx, ny)]
                    stack.append(new_path)
                    visited.append((nx, ny))

    return -1