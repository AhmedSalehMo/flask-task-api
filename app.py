from flask import Flask, jsonify, request
import os

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "تعلم AWS App Runner", "completed": False},
    {"id": 2, "title": "إنشاء Flask API", "completed": False}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Task Management API!",
        "endpoints": {
            "GET /tasks": "List tasks",
            "POST /tasks": "Create new task",
            "PUT /tasks/<id>": "Update task",
            "DELETE /tasks/<id>": "Delete task",
            "GET /health": "Check API status"
        }
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
