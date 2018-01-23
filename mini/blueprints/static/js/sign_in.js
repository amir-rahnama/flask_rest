document.addEventListener('DOMContentLoaded', function() {
   document.getElementById('signup').addEventListener('click', function() {
     print('he')
     const username = document.getElementsByName("email").value;
     const password = document.getElementsByName("password").value;

     // const encrypted = CryptoJS.SHA256(...);
     print(username, password)
     if (username && password) {
       fetch('http://localhost:5000/users/login', {
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
   })
}, false);
