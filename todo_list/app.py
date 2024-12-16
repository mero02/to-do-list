import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables desde .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.Date, nullable=True)  
    priority = db.Column(db.String(10), nullable=True) 
    category = db.Column(db.String(50), nullable=True)  
    description = db.Column(db.Text, nullable=True) 

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    deadline = request.form.get('deadline')
    priority = request.form.get('priority')
    category = request.form.get('category')
    description = request.form.get('description')

    if title:
        new_task = Task(
            title=title,
            deadline=datetime.strptime(deadline, '%Y-%m-%d') if deadline else None,
            priority=priority,
            category=category,
            description=description
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return "Tarea no encontrada", 404
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:id>', methods=['POST'])
def toggle_task_completion(id):
    task = Task.query.get(id)
    if not task:
        return "Tarea no encontrada", 404

    task.done = not task.done
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    title = request.form['title']
    deadline = request.form['deadline']
    priority = request.form.get('priority', 'baja')
    category = request.form.get('category', '')
    description = request.form.get('description', '')

    if deadline:
        try:
            deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
        except ValueError:
            return "Formato de fecha no válido", 400
    else:
        deadline = None

    task.title = title
    task.deadline = deadline
    task.priority = priority
    task.category = category
    task.description = description

    # Guardar cambios en la base de datos
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
