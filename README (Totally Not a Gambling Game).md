# YR-11-T2-2024

# Gambling Game

This is a gambling game built using Pygame where players place bets, sort arrays, and search for numbers. Players start with 50 points and progress through levels by correctly guessing the position of a target number in a sorted array.

## Features

- **User Input**: Players can enter a bet number between 1 and 100.
- **Sorting and Searching**: The game uses quicksort to sort an array and binary search to find a target number.
- **Scoring System**: Points are awarded or deducted based on the player's guess.
- **Levels**: Players advance through levels, with each level increasing the array size.

## Dependencies

- `pygame`: Used for the game interface and rendering.
- `random`: Used for generating random numbers.
- `time`: Used for measuring the time taken for sorting and searching.
- `Binary_Search` module: Contains `quickSort` and `binary_search` functions.

## SIDENOTE
You will need to have Pygame installed on your device

## How to Play
1. Enter a bet number between 1 and 50 when prompted.
2. Press SPACE to start sorting the array.
3. Press SPACE again to start searching for the target number.
4. Points and levels are updated based on the player's guess.

## Game Rules
Start with 50 points.
Each correct guess (exact or within 5 positions) increases points and levels.
Incorrect guesses reduce points by half and may decrease levels.
The game ends when points reach zero.

## Code Overview
- `main()`: Main game loop that handles user input, game logic, and rendering.
- `get_user_input()`: Function to get the player's bet number.
- `draw_text_input_prompt()`: Renders the input prompt for the player.
- `draw_array()`: Draws the array of bars representing the numbers.
- `draw_level()`: Displays the current level.
- `quickSort()`: Function from Binary_Search module to sort the array.
- `binary_search()`: Function from Binary_Search module to search for the target number.

# NOTE
This program is run by gambling game.py