import heapq

# Manhattan Distance
# I tested Euclidean too but Manhattan works better
# for grid based movement.

def heuristic(pos, target):
    return abs(pos[0] - target[0]) + abs(pos[1] - target[1])


def find_path(maze, start, goal):

    open_list = []

    heapq.heappush(
        open_list,
        (0, start)
    )

    came_from = {}

    cost = {
        start: 0
    }

    visited_nodes = 0

    while open_list:

        current = heapq.heappop(open_list)[1]

        visited_nodes += 1

        if current == goal:

            path = []

            while current in came_from:

                path.append(current)

                current = came_from[current]

            path.append(start)

            return (
                path[::-1],
                visited_nodes
            )

        row, col = current

        moves = [

            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)

        ]

        for move in moves:

            r, c = move

            if (
                r < 0
                or c < 0
                or r >= len(maze)
                or c >= len(maze[0])
            ):
                continue

            if maze[r][c] == 1:
                continue

            new_cost = cost[current] + 1

            if (
                move not in cost
                or
                new_cost < cost[move]
            ):

                cost[move] = new_cost

                priority = (
                    new_cost
                    +
                    heuristic(
                        move,
                        goal
                    )
                )

                heapq.heappush(
                    open_list,
                    (priority, move)
                )

                came_from[move] = current

    return None, visited_nodes