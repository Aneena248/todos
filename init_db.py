import sqlite3

try:

    com = sqlite3.connect('todos.db')
    cursor = com.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
    )
    """)

    seed = ['Learn Flask', 'Learn SQL', 'Build a project']

    for task in seed:
        cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    com.commit()
    com.close()
    print("Database ready.")

except Exception as e:
    print("Error initializing database:", e)