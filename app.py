from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Initialize database on startup
database.init_db()

@app.route('/')
def index():
    """Display task list and add form"""
    tasks = database.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    title = request.form.get('title', '').strip()
    if title:
        database.add_task(title)
    
    return redirect(url_for('index'))

@app.route('/toggle', methods=['POST'])
def toggle_task():
    """Toggle task completion status"""
    task_id = int(request.form.get('task_id'))
    database.toggle_task_completion(task_id)
    
    return redirect(url_for('index'))

import os

if __name__ == '__main__':
    # Set debug mode based on the FLASK_ENV environment variable
    debug_mode = os.getenv('FLASK_ENV', 'production') == 'development'
    app.run(debug=debug_mode)