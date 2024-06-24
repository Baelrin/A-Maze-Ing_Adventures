import curses
import queue
import time
from curses import wrapper

maze = [
    ["#", "#", "#", "#", "O", "#", "#", "#", "#"],
    ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", "#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", "#", "#", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"],
]


def print_maze(maze, stdscr, path=None):
    """
    Print the maze on the screen with the path highlighted.

    :param maze: The maze structure
    :param stdscr: The curses screen object
    :param path: The path to highlight
    """
    if path is None:
        path = []
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    YELLOW = curses.color_pair(4)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "*", RED)
            elif value == "O":
                stdscr.addstr(i, j * 2, "O", GREEN)
            elif value == "X":
                stdscr.addstr(i, j * 2, "X", YELLOW)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)


def find_start(maze, start):
    """
    Find the starting position in the maze.

    :param maze: The maze structure
    :param start: The start character
    :return: The coordinates of the start position
    """
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_path(maze, stdscr, delay=0.2):
    """
    Find the path from start to end in the maze.

    :param maze: The maze structure
    :param stdscr: The curses screen object
    :param delay: The delay in seconds for visualization
    :return: The path from start to end
    """
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    if start_pos is None:
        raise ValueError("Start position not found in the maze")

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(delay)

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    """
    Find the neighboring cells in the maze.

    :param maze: The maze structure
    :param row: The current row
    :param col: The current column
    :return: A list of neighboring cells
    """
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    """
    The main function to initialize curses and find the path.

    :param stdscr: The curses screen object
    """
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    find_path(maze, stdscr, delay=0.1)
    stdscr.getch()


wrapper(main)
