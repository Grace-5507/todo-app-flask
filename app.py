from flask import Flask, jsonify, request

app = Flask(__name__)

todo_list = []

@app.route('/todo', methods=['GET'])
def get_todos():
    """
    this method handles requests sent to the GET endpoint of /todo.
        It returns the list of todo items
    """
    return jsonify({
        'todos': todo_list
    })

@app.route('/todo/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    if len(todo_list) == 0:
        return jsonify({'message': 'todolist is empty'}), 404
    elif id > len(todo_list):
        return jsonify({'message': 'todo does not exist'}), 404
    return jsonify({'todo': todo_list[id]})
    


@app.route('/todo', methods=['POST'])
def create_todos():
    """
    this method handles requests sent to the POST endpoint of /todo.
    It returns the list of todo items including the created item
    """
    todo = request.get_json()
    todo_list.append(todo)
    return jsonify({
        'todos': todo_list
    })

@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    """
    this method handles requests sent to the PUT endpoint(updation). 
    It returns the list of todo items including the updated item
    """
    todo_list[id] = request.get_json()
    return jsonify({
        'todos': todo_list
    })

@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    """
    this method handles deletion of todo items.
    """
    if len(todo_list) == 0:
        return jsonify({'message': 'todolist is empty'}), 404
    todo_list.pop(id)
    return jsonify({
        'todos': todo_list
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
         
