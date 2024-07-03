from typing import List, Set, Tuple, TypedDict


class Point(TypedDict):
    x: int
    y: int


def dfs_walk(
    maze: List[str],
    wall: str,
    curr: Point,
    end: Point,
    path: List[Point],
    seen: Set[Tuple[int, int]],
    shortest_path: List[Point],
) -> None:
    # Base cases
    if (
        curr["x"] < 0
        or curr["x"] >= len(maze[0])
        or curr["y"] < 0
        or curr["y"] >= len(maze)
    ):
        return
    if maze[curr["y"]][curr["x"]] == wall:
        return
    if (curr["y"], curr["x"]) in seen:
        return

    # Add current point to path
    path.append(curr)
    seen.add((curr["y"], curr["x"]))

    # Check if we've reached the end
    if curr["y"] == end["y"] and curr["x"] == end["x"]:
        if not shortest_path or len(path) < len(shortest_path):
            shortest_path[:] = path[:]
        path.pop()
        seen.remove((curr["y"], curr["x"]))
        return

    # Recursive exploration
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_point = Point(x=curr["x"] + dx, y=curr["y"] + dy)
        dfs_walk(maze, wall, next_point, end, path, seen, shortest_path)

    # Backtrack
    path.pop()
    seen.remove((curr["y"], curr["x"]))


def maze_solver(maze: List[str], wall: str, start: Point, stop: Point) -> List[Point]:
    shortest_path: List[Point] = []
    dfs_walk(maze, wall, start, stop, [], set(), shortest_path)
    return shortest_path


def main() -> List[Point]:
    maze = [
        "x xxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "xxxxxxxxxxxx",
    ]
    return maze_solver(maze, "x", Point(x=1, y=0), Point(x=10, y=0))


if __name__ == "__main__":
    maze = [
        "x xxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "xxxxxxxxxxxx",
    ]
    print(f"{5 * '*'} Traversing {5 * '*'}")
    for line in maze:
        print(line)
    print("\n")
    finished = main()
    print(f"{5 * '*'} Found Solution {5 * '*'}")
    print(finished)
    print("\n")
    print(f"{5 * '*'} Recreated Map {5 * '*'}")
    for y, y_line in enumerate(maze):
        new_line = ""
        for x, x_line in enumerate(y_line):
            point = Point(x=x, y=y)
            if point in finished:
                new_line += "o"
            else:
                new_line += maze[y][x]
        print(new_line)
