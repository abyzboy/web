const dropdownToggle = document.getElementById("dropdownToggle"); // Изменено название переменной
const dropdownMenu = document.getElementById("dropdownMenu");

dropdownToggle.addEventListener("click", () => { // Изменено название переменной
  dropdownMenu.classList.toggle("show");
});

// Закрываем выпадающее меню при клике вне его
window.addEventListener("click", (event) => {
  if (!dropdownToggle.contains(event.target)) { // Проверяем, что клик был вне dropdownToggle
    if (dropdownMenu.classList.contains('show')) {
      dropdownMenu.classList.remove('show');
    }
  }
});

function goToMathCourse() {
    window.location.href = "/Page_math_course_70/index.html"; 
}

function goToProgress() {
    window.location.href = "/Прогресс/index.html"; 
}

function goToCoursePage() {
    window.location.href = "/Страница_темы/index.html"; 
}

function goToRegistrathion() {
    window.location.href = "/Registrathion/index.html"; 
}

function goToCourses() {
  window.location.href = "/Курсы/index.html"; 
}