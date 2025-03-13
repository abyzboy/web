function updateProgress() {
    const checkboxes = document.querySelectorAll('.topic-card input[type="checkbox"]');
    const progressBar = document.getElementById('progressBar');
    const total = checkboxes.length;
    let completed = 0;

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            completed++;
             localStorage.setItem(checkbox.id, 'true'); // Сохраняем состояние в localStorage
        } else {
            localStorage.setItem(checkbox.id, 'false'); // Сохраняем состояние в localStorage
        }
    });

    const progress = (completed / total) * 100;
    progressBar.style.width = progress + '%';
}

// При загрузке страницы восстанавливаем состояние чекбоксов
window.onload = function() {
    const checkboxes = document.querySelectorAll('.topic-card input[type="checkbox"]');

    checkboxes.forEach(checkbox => {
        const checked = localStorage.getItem(checkbox.id) === 'true';
        checkbox.checked = checked;
    });
    updateProgress(); // Обновляем полосу прогресса после восстановления состояния
};