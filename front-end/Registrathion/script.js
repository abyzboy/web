const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function Registrathion(username, email, password) {
	const userData = {
	  email: email,
	  password: password,
	  username: username
	};
  
	fetch('http://127.0.0.1:5000/api/v1/auth/register', {
	  method: 'POST',
	  headers: {
		'Content-Type': 'application/json',
	  },
	  body: JSON.stringify(userData)
	})
	.then(response => response.json())
	.then(data => {
	  console.log('Успех:', data);
	})
	.catch(error => {
	  console.error('Ошибка:', error);
	});
  }

  function authorizeUser() {
    // Получаем значения из полей ввода
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Проверяем, что поля не пустые
    if (!email || !password) {
        alert('Пожалуйста, заполните все поля.');
        return;
    }

    // Вызываем функцию авторизации
    Authorization(email, password);
}

function Authorization(email, password) {
    const loginData = {
        email: email,
        password: password
    };

    fetch('http://127.0.0.1:5000/api/v1/auth/login', {  // Убедитесь, что это правильный эндпоинт для авторизации
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успех:', data);
        if (data.token) {
            localStorage.setItem('jwtToken', data.token);
			window.location.href = "/front-end/Курсы/index.html"; 
		}
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}