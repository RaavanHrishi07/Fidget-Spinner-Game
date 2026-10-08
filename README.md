# Fidget Spinner Game

A Python Turtle fidget spinner game with interactive controls, momentum-based animation, speed feedback, and best-spin tracking.

## Features

- Interactive fidget spinner animation
- Spin using Space or mouse click
- Momentum-based spinning with gradual slowdown
- Real-time speed display
- Visual speed bar
- Temporary "BOOST!" feedback when spinning
- Current spin counter
- Best spin record tracking
- Reset and quit controls
- No external Python packages required

## Controls

| Action | Control |
|---|---|
| Spin | Space / Mouse Click |
| Reset Current Spins | R |
| Quit Game | Esc |

## Requirements

- Python 3.8 or newer
- Tkinter and Turtle support

Tkinter and Turtle are included with standard Python installations, so no external packages are required.

## Installation

Clone the repository:

    git clone https://github.com/RaavanHrishi07/Fidget-Spinner-Game.git

Navigate to the project directory:

    cd Fidget-Spinner-Game

## Run the Game

Start the game with:

    python main.py

## How It Works

The game uses Python's Turtle graphics library to draw and animate a three-arm fidget spinner.

Each time the player presses Space or clicks the window, the spinner receives a speed boost. The spinner then gradually slows down using a friction-based animation system.

The game displays:

- Current spin count
- Best spin count
- Current speed
- Visual speed level
- Temporary boost feedback

Pressing `R` resets the current spin count and speed while keeping the best spin record.

Pressing `Esc` closes the game.

## Project Structure

    Fidget-Spinner-Game/
    │
    ├── main.py
    ├── .gitignore
    └── README.md

## Technologies

- Python
- Turtle Graphics
- Math
- Time

## Author

**Hrishikesh Sharma**

GitHub: https://github.com/RaavanHrishi07

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.