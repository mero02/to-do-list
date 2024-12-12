document.addEventListener('DOMContentLoaded', () => {
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