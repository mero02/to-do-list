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
