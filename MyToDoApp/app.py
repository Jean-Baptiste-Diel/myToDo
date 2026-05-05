from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle ToDo
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Créer la base
with app.app_context():
    db.create_all()

# Ajouter une tâche .
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    todo = Todo(title=data['title'])
    db.session.add(todo)
    db.session.commit()
    return jsonify({'id': todo.id, 'title': todo.title, 'completed': todo.completed})

# Récupérer toutes les tâches
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([
        {'id': t.id, 'title': t.title, 'completed': t.completed}
        for t in todos
    ])

# Récupérer une tâche
@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({'id': todo.id, 'title': todo.title, 'completed': todo.completed})

# Modifier une tâche
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json

    todo.title = data.get('title', todo.title)
    todo.completed = data.get('completed', todo.completed)

    db.session.commit()
    return jsonify({'message': 'updated'})

# Supprimer une tâche
# @app.route('/todos/<int:id>', methods=['DELETE'])
# def delete_todo(id):
#     todo = Todo.query.get_or_404(id)
#     db.session.delete(todo)
#     db.session.commit()
#     return jsonify({'message': 'deleted'})

if __name__ == '__main__':
    app.run(debug=True)