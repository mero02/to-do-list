const deleteTaskModal = document.getElementById('deleteTaskModal');
deleteTaskModal.addEventListener('show.bs.modal', (event) => {
    const button = event.relatedTarget;
    const taskId = button.getAttribute('data-task-id');
    const taskTitle = button.getAttribute('data-task-title');

    const deleteMessage = deleteTaskModal.querySelector('#deleteMessage');
    deleteMessage.textContent = `¿Estás seguro de que deseas eliminar la tarea "${taskTitle}"?`;

    const deleteForm = deleteTaskModal.querySelector('#deleteForm');
    deleteForm.action = `/delete/${taskId}`;
});

function toggleCompletion(taskId, button) {
    fetch(`/complete/${taskId}`, { method: 'POST' })
        .then(response => {
            if (response.ok) {
                const row = button.closest('tr');
                if (button.classList.contains('btn-outline-success')) {
                    button.classList.remove('btn-outline-success');
                    button.classList.add('btn-success');
                    button.textContent = 'Completada';
                    row.classList.add('table-success');
                } else {
                    button.classList.remove('btn-success');
                    button.classList.add('btn-outline-success');
                    button.textContent = 'Completar';
                    row.classList.remove('table-success');
                }
            } else {
                console.error('Error al cambiar el estado de la tarea');
            }
        });
}

document.addEventListener('DOMContentLoaded', function () {
    // Referencia al modal de edición
    const editModal = document.getElementById('editTaskModal');

    // Agregar evento cuando se muestra el modal
    editModal.addEventListener('show.bs.modal', function (event) {
        // Obtener el botón que disparó el modal
        const button = event.relatedTarget;

        // Recuperar los atributos personalizados del botón
        const taskId = button.getAttribute('data-task-id');
        const title = button.getAttribute('data-task-title') || '';
        const deadline = button.getAttribute('data-task-deadline') || '';
        const priority = button.getAttribute('data-task-priority') || 'baja';
        const category = button.getAttribute('data-task-category') || '';
        const description = button.getAttribute('data-task-description') || '';

        // Precargar los datos en los campos del formulario
        document.getElementById('edit-title').value = title;
        document.getElementById('edit-deadline').value = deadline;
        document.getElementById('edit-priority').value = priority;
        document.getElementById('edit-category').value = category;
        document.getElementById('edit-description').value = description;

        // Actualizar la acción del formulario para apuntar a la URL de edición de la tarea
        document.getElementById('editTaskForm').action = `/edit/${taskId}`;
    });
});
