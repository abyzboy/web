function sendContent(element) {
  const title = element.querySelector('h3').textContent; // Получаем текст заголовка
  const video = element.dataset.video;

  localStorage.setItem('selectedTitle', title); // Сохраняем заголовок в localStorage
  localStorage.setItem('selectedVideo', video);
  
  window.location.href = "/Страница_темы/index.html"; // Переходим на другую страницу
}
