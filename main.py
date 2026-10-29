
import random
import sqlite3
import customtkinter as ctk

# Connect to the database
db = sqlite3.connect("arena.db")

# Create the items table
db.execute("""
    CREATE TABLE IF NOT EXISTS items (
        name TEXT PRIMARY KEY,
        rating REAL DEFAULT 1000
    )
""")
db.commit()

pair = []


def add():
    name = entry.get().strip()

    if not name:
        return

    db.execute(
        "INSERT OR IGNORE INTO items(name) VALUES (?)",
        (name,)
    )
    db.commit()

    entry.delete(0, "end")
    next_pair()


def next_pair():
    global pair

    items = db.execute(
        "SELECT name, rating FROM items"
    ).fetchall()

    if len(items) >= 2:
        pair = random.sample(items, 2)

        left.configure(text=pair[0][0])
        right.configure(text=pair[1][0])
    else:
        pair = []
        left.configure(text="?")
        right.configure(text="?")

    board.delete("1.0", "end")

    rankings = db.execute(
        "SELECT name, rating FROM items ORDER BY rating DESC"
    ).fetchall()

    for i, (name, rating) in enumerate(rankings, 1):
        board.insert(
            "end",
            f"{i}. {name} - {rating:.0f}\n"
        )


def win(i):
    if not pair:
        return

    (winner, winner_rating), (loser, loser_rating) = (
        pair[i],
        pair[1 - i]
    )

    delta = 32 * (
        1 - 1 / (
            1 + 10 ** ((loser_rating - winner_rating) / 400)
        )
    )

    db.execute(
        "UPDATE items SET rating = rating + ? WHERE name = ?",
        (delta, winner)
    )

    db.execute(
        "UPDATE items SET rating = rating - ? WHERE name = ?",
        (delta, loser)
    )

    db.commit()
    next_pair()


# Create the application window
app = ctk.CTk()
app.title("ELO Arena")
app.geometry("400x500")

# Input field
entry = ctk.CTkEntry(
    app,
    placeholder_text="Add a movie, song, TV show, etc."
)
entry.pack(fill="x", padx=10, pady=10)

# Add button
ctk.CTkButton(
    app,
    text="Add Item",
    command=add
).pack()

# Main title
ctk.CTkLabel(
    app,
    text="Which Is Better?",
    font=("Arial", 20)
).pack()

# Left item button
left = ctk.CTkButton(
    app,
    text="?",
    height=60,
    command=lambda: win(0)
)
left.pack(fill="x", padx=10, pady=3)

# Right item button
right = ctk.CTkButton(
    app,
    text="?",
    height=60,
    command=lambda: win(1)
)
right.pack(fill="x", padx=10, pady=3)

# Ranking board
board = ctk.CTkTextbox(app)
board.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# Display the initial rankings
next_pair()

# Start the application
app.mainloop()
