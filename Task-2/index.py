from flask import Flask, render_template, url_for, request, redirect
import random
from todo_json import load_todos, save_todos

app = Flask(__name__)

todos = load_todos()

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    if (request.method == "POST"):
        todo_name = request.form["todo_name"]
        cur_id = random.randint(1,1000)
        todos.append({
            'id':cur_id,
            'name':todo_name,
        })
        save_todos(todos) 
    return render_template("index.html", items = todos)

@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id):
    global todos
    new_text = request.form['todo_text']
    for todo in todos:
        if todo['id'] == todo_id:
            todo['name'] = new_text 
            break
    save_todos(todos)  
    return redirect(url_for("home"))


@app.route("/delete/,<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]  
    save_todos(todos)  
    return redirect(url_for("home"))      

if __name__ == "__main__":
    app.run(debug=True)