from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return jsonify({"message": "Task Manager API", "version": "1.0"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data['title'], "done": False}
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/health')
def health():
    return jsonify({"status": "ok"})
