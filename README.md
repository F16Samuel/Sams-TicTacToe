
# Tic-Tac-Toe Game

## Final Project

### Description
This is a simple Tic-Tac-Toe game implemented in Python. Players can choose to play against each other or against a computer opponent. The game features a console-based interface where players can input their moves, and the board is displayed after each turn.

### Directory Structure
```
finalTicTacToeGame
    ├── main.py         # Contains the base loop of the game
    ├── player.py       # Contains the logic for player vs player
    ├── comp.py         # Contains the logic for player vs computer
    ├── gamelogic.py    # Contains the logic for game inputs and win conditions
    ├── util.py         # Contains utility functions like clearing the console
    ├── display.py      # Contains functions to display the game board
    ├── README.md       # Documentation for the project
    └── LICENSE         # Project license
```

### File Descriptions

- **main.py**: 
    - Contains the main game loop that allows players to choose between Player vs Player (PvP) or Player vs Computer (PvE).
    - Manages game replayability.

- **player.py**: 
    - Implements the logic for a Player vs Player game mode.
    - Manages player moves and checks for win conditions or draws.

- **comp.py**: 
    - Implements the logic for a Player vs Computer game mode.
    - The computer randomly selects moves and checks for win conditions or draws.

- **gamelogic.py**: 
    - Contains functions to check for win conditions and update the move count.

- **util.py**: 
    - Contains utility functions such as clearing the console.

- **display.py**: 
    - Contains functions to display the Tic-Tac-Toe board in the console.

### How to Run the Game
1. Ensure you have Python installed on your machine.
2. Clone the repository:
    ```bash
    git clone https://github.com/F16Samuel/Sams-TicTacToe.git
    ```
3. Navigate to the project directory:
    ```bash
    cd Sams-TicTacToe
    ```
4. Run the game:
    ```bash
    python main.py
    ```

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
- Inspired by classic Tic-Tac-Toe gameplay.
- Developed for educational purposes to enhance Python programming skills.

