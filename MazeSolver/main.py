from maze_data import maze
from maze_data import start
from maze_data import goal

from astar import find_path

print("\n")
print("=" * 40)
print("A* MAZE SOLVER")
print("=" * 40)

path, explored = find_path(
    maze,
    start,
    goal
)

if path:

    print("\nPath Found!\n")

    for row in range(len(maze)):

        for col in range(len(maze[0])):

            point = (row, col)

            if point == start:
                print("S", end=" ")

            elif point == goal:
                print("G", end=" ")

            elif point in path:
                print("*", end=" ")

            elif maze[row][col] == 1:
                print("#", end=" ")

            else:
                print(".", end=" ")

        print()

    print("\nCoordinates:\n")

    for node in path:
        print(node)

    print(
        f"\nNodes Explored: {explored}"
    )

    print(
        f"Path Length: {len(path)}" 
    )

    print(
    f"Efficiency Score: {len(path)/explored:.2f}"
)

else:

    print(
        "\nNo path found."
    )