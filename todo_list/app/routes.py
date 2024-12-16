from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db
from flask_login import login_required, current_user
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', tasks=tasks)

@main.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    deadline = request.form.get('deadline')
    priority = request.form.get('priority')
    category = request.form.get('category')
    description = request.form.get('description')

    if title:
        new_task = Task(
            title=title,
            deadline=datetime.strptime(deadline, '%Y-%m-%d').date() if deadline else None,
            priority=priority,
            category=category,
            description=description,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/complete/<int:id>', methods=['POST'])
@login_required
def toggle_task_completion(id):
    task = Task.query.get(id)
    if not task or task.user_id != current_user.id:
        return "Tarea no encontrada o acceso no autorizado", 404

    # Cambiar el estado de la tarea
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('main.home'))


@main.route('/edit/<int:task_id>', methods=['POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    # Verificar si la tarea pertenece al usuario actual
    if task.user_id != current_user.id:
        return "Acceso no autorizado", 403

    title = request.form['title']
    deadline = request.form.get('deadline')  
    priority = request.form.get('priority', 'baja')  
    category = request.form.get('category', '')
    description = request.form.get('description', '')

    # Validar y convertir la fecha si existe
    if deadline:
        try:
            deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
        except ValueError:
            return "Formato de fecha no válido", 400
    else:
        deadline = None

    # Actualizar los campos de la tarea
    task.title = title
    task.deadline = deadline
    task.priority = priority
    task.category = category
    task.description = description

    # Guardar cambios en la base de datos
    db.session.commit()
    return redirect(url_for('main.home'))
@main.route('/edit/<int:task_id>', methods=['GET'])
@login_required
def load_task(task_id):
    task = Task.query.get_or_404(task_id)

    # Verificar si la tarea pertenece al usuario actual
    if task.user_id != current_user.id:
        return "Acceso no autorizado", 403

    # Pasar los datos de la tarea al formulario de edición
    return render_template('edit.html', task=task)
