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