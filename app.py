from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database file path
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.db')

def init_db():
    """Initialize the database and create tasks table if it doesn't exist"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            due_date DATE
        )
    ''')
    
    # Add due_date column to existing table if it doesn't exist
    try:
        cursor.execute('ALTER TABLE tasks ADD COLUMN due_date DATE')
    except sqlite3.OperationalError:
        # Column already exists or other error, continue
        pass
    
    conn.commit()
    conn.close()

# Initialize database when module is loaded
init_db()

def get_all_tasks():
    """Get all tasks from database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, completed, due_date FROM tasks ORDER BY id')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to list of dictionaries for template compatibility
    tasks = []
    for row in rows:
        tasks.append({
            'id': row[0],
            'title': row[1],
            'completed': bool(row[2]),
            'due_date': row[3]
        })
    return tasks

def add_task_to_db(title, due_date=None):
    """Add a new task to database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed, due_date) VALUES (?, 0, ?)', (title, due_date))
    conn.commit()
    conn.close()

def toggle_task_in_db(task_id):
    """Toggle task completion status in database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 - completed WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    """Delete a task from database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Display task list and add form"""
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    title = request.form.get('title', '').strip()
    due_date = request.form.get('due_date', '').strip()
    
    # Convert empty string to None for database
    if not due_date:
        due_date = None
    
    if title:
        add_task_to_db(title, due_date)
    
    return redirect(url_for('index'))

@app.route('/toggle', methods=['POST'])
def toggle_task():
    """Toggle task completion status"""
    task_id = int(request.form.get('task_id'))
    toggle_task_in_db(task_id)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_task():
    """Delete a task"""
    task_id = int(request.form.get('task_id'))
    delete_task_from_db(task_id)
    return redirect(url_for('index'))

import os

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Set debug mode based on the FLASK_ENV environment variable
    debug_mode = os.getenv('FLASK_ENV', 'production') == 'development'
    app.run(debug=debug_mode)