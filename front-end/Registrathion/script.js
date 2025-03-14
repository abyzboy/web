const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function Registrathion(Username, Email, Password) {
	// Данные для отправки (может быть объектом, FormData и т.д.)
const data = {
	username: Username,
	email: Email,
	password: Password
  };
  
  fetch('http://127.0.0.1:5000/api/v1/auth/register', {
	method: 'POST',
	headers: {
	  'Content-Type': 'application/json', // Указываем тип данных
	},
	body: JSON.stringify(data) // Конвертируем объект в JSON-строку
  })
  .then(response => {
	if (!response.ok) throw new Error('Ошибка сети');
	return response.json(); // Парсим JSON-ответ
  })
  .then(result => {
	console.log('Успех:', result);
  })
  .catch(error => {
	console.error('Ошибка:', error);
  });
}