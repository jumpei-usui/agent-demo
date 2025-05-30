import sqlite3
import os

DATABASE_PATH = 'tasks.db'

def init_db():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

def get_all_tasks():
    """Get all tasks from the database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, title, completed FROM tasks ORDER BY id')
    rows = cursor.fetchall()
    
    tasks = []
    for row in rows:
        tasks.append({
            'id': row[0],
            'title': row[1],
            'completed': bool(row[2])
        })
    
    conn.close()
    return tasks

def add_task(title):
    """Add a new task to the database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, 0))
    task_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return task_id

def toggle_task_completion(task_id):
    """Toggle the completion status of a task"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # First get current status
    cursor.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,))
    result = cursor.fetchone()
    
    if result:
        current_status = result[0]
        new_status = 1 if current_status == 0 else 0
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
    
    conn.close()