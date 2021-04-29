import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Todo

@app.route('/todo', methods=['GET'])
def get_todos():
    """
    this method handles requests sent to the GET endpoint of /todo.
        It returns the list of todo items
    """
    todos = db.session.query(Todo).all()
    todo_list = []
    for todo in todos:
        todo_list.append(todo.as_dict())
    return jsonify({
        'todos': todo_list
    })

@app.route('/todo/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    try:
        item = db.session.query(Todo).filter(Todo.id == id).one()
        return jsonify({
            'todos': item.as_dict()
        })
    except Exception as e:
        print(e)
        return jsonify({
            'todos': item.as_dict()
        })


@app.route('/todo', methods=['POST'])
def create_todos():
    """
    this method handles requests sent to the POST endpoint of /todo.
    It returns the list of todo items including the created item
    """
    todo = request.get_json()
    new_todo = Todo(description=todo['description'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({
        'todos': new_todo.as_dict()
    })

@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    """
    this method handles requests sent to the PUT endpoint(updation). 
    It returns the list of todo items including the updated item
    """
    req = request.get_json()  
    todo = db.session.query(Todo).filter(Todo.id == id).one()
    todo.description = req['description']
    db.session.commit()
    return jsonify({
        'message': 'todo updated successfully'
        })

@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    """
    this method handles deletion of todo items.
    """
    try:
        todo = db.session.get(Todo, id)
        db.session.delete(todo)
        db.session.commit()
        return jsonify({
            'todos': 'todo deleted successfully'
        })
    except Exception as e:
        return jsonify({
            'error': e
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
