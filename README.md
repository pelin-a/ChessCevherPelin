Pelinsu Altun : 88167086
Cevher Yuksel : 52812061

Chess Game Project

Overview:
This project is a terminal-based implementation of the classic chess game.
It allows two players to compete, with features such as checking for valid moves, 
implementing check and checkmate logic, and providing a fully interactive game experience.
The program handles the game rules, board representation, and game logic.

Features:
Interactive chess game for two players.
Validation of moves based on the rules of chess.
Detection of check and checkmate conditions.

Project Structure
The project is divided into multiple classes:
Main Classes:

Game Class:
Manages the overall flow of the game.
Handles player turns, move validation, and game termination.
Checks for conditions like check and checkmate.

Board Class:
Represents the chessboard.
Stores the positions of pieces and provides methods to access and modify the board state.
Includes utility methods like safe_move and simulate_move for handling game logic.

Player Class
Represents the players.
Stores player-specific information like name, color, and captured pieces.

Piece Class (Abstract Base Class):
Parent class for all specific chess pieces (e.g., King, Queen, Pawn).
Defines common methods like get_color, get_location, and set_location.

Specific Piece Classes (King, Queen, Bishop, Knight, Rook, Pawn):

Implements piece-specific move validation using possible_moves().

Contributions:
Tasks and Responsibilities:

Pelinsu ALtun:
Game Logic and Flow:
Implemented the Game class to manage the game's flow, including player turns and win/loss conditions.
Added logic for in_check and checkmate detection.
Developed the move execution logic, including capturing pieces and validating moves.
Player Management:
Created the Player class to handle player details and interactions.
Board Management:
Designed the Board class for maintaining the state of the chessboard.
Implemented utility methods like safe_move and for handling complex rules such as check and checkmate.
Pawn Class:
Developed the Pawn class, including the possible_moves() method to handle pawn-specific movement and capturing.

Cevher:
Piece-Specific Classes:
Implemented the classes for King, Queen, Bishop, Knight, and Rook.
Developed possible_moves() methods for each piece, ensuring adherence to chess rules.


How to Play

Run the program in a terminal.
Players will be prompted to enter their names and colors.
Take turns entering moves in the format:
Starting square, and destination square 
Example input: e2 e4.

The program will validate moves and notify players of checks and checkmates.
The game ends when one player wins by checkmate.
