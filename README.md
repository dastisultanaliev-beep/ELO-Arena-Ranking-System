# ELO Arena — Ranking System

## Description

ELO Arena is a desktop application built with Python and CustomTkinter. It allows users to rank movies, songs, TV shows, games, and other items through pairwise comparisons.

## Features

- Add items to the ranking system.
- Compare two randomly selected items.
- Choose the item you prefer.
- Update ratings using an ELO-based formula.
- Display items sorted by rating.
- Store items and ratings in an SQLite database.
- Preserve rankings between application sessions.

## Technologies

- Python
- CustomTkinter
- SQLite3
- Random module

## Requirements

- Python 3.10 or newer
- customtkinter

## Installation

1. Install Python.
2. Install CustomTkinter:

   ```bash
   pip install customtkinter
   ```

3. Save the source code as `main.py`.
4. Run the application:

   ```bash
   python main.py
   ```

## How to Use

1. Enter the name of a movie, song, TV show, or another item.
2. Click **Add Item**.
3. Add at least two items.
4. Choose your preferred item from the two displayed buttons.
5. The ELO ratings will update automatically.
6. View the ranking board to see the current order.

## Database

The application uses SQLite to store item names and ratings in `arena.db`. The database is created automatically when the application starts.

## License

This project is available for personal and educational use.
