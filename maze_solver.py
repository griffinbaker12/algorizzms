from collections import deque
from typing import List, Set, Tuple, TypedDict

# So, questions from here:
# 1) What exactly is a TypedDict? Think I get the general idea.
# 2) Why doses BFS guarantee to find the shortest path?


class Point(TypedDict):
    x: int
    y: int


def bfs_shortest_path(
    maze: List[str], wall: str, start: Point, end: Point
) -> List[Point]:
    queue = deque([(start, [start])])
    seen: Set[Tuple[int, int]] = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path  # This is guaranteed to be the shortest path

        if (current["y"], current["x"]) in seen:
            continue

        seen.add((current["y"], current["x"]))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current["x"] + dx, current["y"] + dy
            if (
                0 <= next_y < len(maze)
                and 0 <= next_x < len(maze[0])
                and maze[next_y][next_x] != wall
            ):
                next_point = Point(x=next_x, y=next_y)
                queue.append((next_point, path + [next_point]))

    return []  # No path found


# Example usage
maze = [
    "x xxxxxxxx x",
    "x        x x",
    "x        x x",
    "x xxxxxxxx x",
    "x          x",
    "xxxxxxxxxxxx",
]

start = Point(x=1, y=0)
end = Point(x=10, y=0)

shortest_path = bfs_shortest_path(maze, "x", start, end)
print("Shortest path:", shortest_path)

# Visualization
for y, row in enumerate(maze):
    print(
        "".join(
            "o" if Point(x=x, y=y) in shortest_path else c for x, c in enumerate(row)
        )
    )
