document.addEventListener('DOMContentLoaded', function() {
   document.getElementById('signup').addEventListener('click', postData)
}, false);


function postData () {
  const username = document.querySelector('input[name=email]').value;
  const password = document.querySelector('input[name=password]').value;

  if (username && password) {
    return fetch('http://localhost:5000/users/login', {
       method: 'POST',
       body: JSON.stringify({username, password}),
       headers: new Headers({
         'Content-Type': 'application/json'
       })
     })
     .then(res => res.json())
     .catch(error => console.error('Error:', error))
     .then(response => console.log('Success:', response));
  }
}
