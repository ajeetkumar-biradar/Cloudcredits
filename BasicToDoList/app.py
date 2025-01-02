from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if not task:
        return jsonify({"error": "Task content is required."}), 400
    new_task = {"id": len(tasks) + 1, "task": task, "completed": False}
    tasks.append(new_task)
    return render_template("index.html", tasks=tasks)


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return render_template("index.html", tasks=tasks)
    return jsonify({"error": "Task not found."}), 404


@app.route("/clear", methods=["POST"])
def clear_tasks():
    tasks.clear()
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
