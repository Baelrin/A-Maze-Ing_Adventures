# A-Maze-Ing Adventures

Welcome to **A-Maze-Ing Adventures**, an exciting maze-solving project that visualizes the pathfinding process using Python and the `curses` library. This project allows you to see how an algorithm navigates through a maze to find the shortest path from the start to the end.

## Table of Contents

- [A-Maze-Ing Adventures](#a-maze-ing-adventures)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example Maze](#example-maze)
  - [Contributing](#contributing)
    - [Steps to Contribute](#steps-to-contribute)
  - [License](#license)

## Introduction

A-Maze-Ing Adventures is designed to help you understand and visualize maze-solving algorithms. It uses a Breadth-First Search (BFS) algorithm to find the shortest path in a maze, and displays the process in a terminal using the `curses` library.

## Features

- Visualize the pathfinding process in real-time
- Customizable maze structure
- Adjustable visualization speed
- Clear distinction between start, end, and path points
- Easy to understand and extend

## Installation

To run A-Maze-Ing Adventures, you'll need to have Python installed on your system. You can clone the repository and install the required dependencies using the following commands:

```bash
git clone https://github.com/Baelrin/a-maze-ing-adventures.git
cd a-maze-ing-adventures
pip install -r requirements.txt
```

## Usage

You can run the project using the following command:

```bash
python master.py
```

The default maze is defined within the `master.py` file. You can customize the maze by modifying the `maze` variable.

### Example Maze

```python
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
```

## Contributing

We welcome contributions to improve A-Maze-Ing Adventures! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

### Steps to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy your journey through the mazes with **A-Maze-Ing Adventures**!
