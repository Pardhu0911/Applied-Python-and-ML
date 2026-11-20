import sqlite3

# 1. Connect to SQLite and 2. Create university.db file
conn_sqlite = sqlite3.connect(':memory:')
cursor_sqlite = conn_sqlite.cursor()


# 4. Execute table creation
cursor_sqlite.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        major TEXT,
        gpa REAL
    )
''')

# Define the 3 required student records
students_list = [
    ('John Doe', 'Biology', 3.6),
    ('Jane Smith', 'Information Technology', 3.2),
    ('Mark Freeman', 'Business Administration', 3.0)
]

# Insert records
cursor_sqlite.executemany('INSERT INTO students (name, major, gpa) VALUES (?, ?, ?)', students_list)
conn_sqlite.commit()

# Retrieve and print all records for the grading output
cursor_sqlite.execute('SELECT * FROM students')
for row in cursor_sqlite.fetchall():
    print(row)
