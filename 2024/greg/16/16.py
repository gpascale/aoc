import os
import heapq
import numpy as np

root = os.path.dirname(os.path.realpath(__file__))

#     distances[start] = 0
#     
#     

#     while pq:
#         current_distance, current_node = heapq.heappop(pq)

#         if current_node in visited:
#             continue

#         visited.add(current_node)

#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))

#     return distances

def print_grid(grid):
    for line in grid:
        print(''.join(line))


dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def dijk(grid, ys, xs, dr=None):
    dist = np.full((len(grid), len(grid[0]), len(dirs)), -1, dtype=int)
    if dr:
        pq = [(0, (ys, xs, dr))]
    else:
        pq = [(0, (ys, xs, 0))]
        pq += [(0, (ys, xs, 1))]
        pq += [(0, (ys, xs, 2))]
        pq += [(0, (ys, xs, 3))]
    print(pq)

    while pq:
        cur, (y, x, dr) = heapq.heappop(pq)
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == '#':
            continue
        if dist[y, x, dr] != -1:
            continue
        dist[y, x, dr] = cur
        heapq.heappush(pq, (cur + 1000, (y, x, (dr + 1 + 4) % 4 )))
        heapq.heappush(pq, (cur + 1000, (y, x, (dr - 1 + 4) % 4 )))
        heapq.heappush(pq, (cur + 1, (y + dirs[dr][1], x + dirs[dr][0], dr)))
    return dist


def part_a(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    grid = [list(line) for line in grid]
    xs, ys = [(line.index('S'), i) for i, line in enumerate(grid) if 'S' in line][0]
    xe, ye = [(line.index('E'), i) for i, line in enumerate(grid) if 'E' in line][0]
    print_grid(grid)

    dist = dijk(grid, ys, xs, 1)
    return dist[ye, xe, :].min()


def part_b(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    grid = [list(line) for line in grid]
    xs, ys = [(line.index('S'), i) for i, line in enumerate(grid) if 'S' in line][0]
    xe, ye = [(line.index('E'), i) for i, line in enumerate(grid) if 'E' in line][0]
    print_grid(grid)


    dist_from = dijk(grid, ys, xs, 1)
    dist_to = dijk(grid, ye, xe)
    min_dist = dist_from[ye, xe].min()

    is_part = np.zeros((len(grid), len(grid[0])), dtype=int)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for dr in range(4):
                d_from = dist_from[y, x, dr]
                d_to = dist_to[y, x, (dr + 4 + 2) % 4]
                if d_from != -1 and d_to != -1 and d_from + d_to == min_dist:
                    is_part[y, x] = 1
    return np.sum(is_part)

print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
