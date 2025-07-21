from flask import Flask, render_template, request, redirect
import json, os
app = Flask(__name__)
DATA_FILE = 'tasks.json'
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index_json.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    title = request.form['title']
    new_id = max([task['id'] for task in tasks], default=0) + 1
    tasks.append({'id': new_id, 'title': title, 'status': 'Not Completed'})
    save_tasks(tasks)
    return redirect('/')
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = request.form['title']
            break
    save_tasks(tasks)
    return redirect('/')
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect('/')
@app.route('/toggle_status/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed' if task['status'] == 'Not Completed' else 'Not Completed'
            break
    save_tasks(tasks)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
