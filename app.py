from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task storage
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    """Display task list and add form"""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    global task_id_counter
    
    title = request.form.get('title', '').strip()
    if title:
        task = {
            'id': task_id_counter,
            'title': title,
            'completed': False
        }
        tasks.append(task)
        task_id_counter += 1
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggle task completion status"""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)