document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.form');
    const emailInput = document.querySelector('#email');
    const passwordInput = document.querySelector('#password');
    const loginButton = document.querySelector('.login-button');
    const forgotPasswordLink = document.querySelector('.forgot-password a');
    const togglePasswordButton = document.querySelector('#togglePassword');

    form.addEventListener('submit', (e) => {
      e.preventDefault(); // Prevent form submission

      const email = emailInput.value.trim();
      const password = passwordInput.value.trim();

      if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
      }

      if (password.length < 6) {
        alert('Password must be at least 6 characters long.');
        return;
      }

      // Check specific email and password
      if (email === 'yaswanthvisa@gmail.com' && password === 'Yash@123') {
        // Handle successful login
        console.log('Form submitted:', { email, password });
        alert('Login successful!');
        emailInput.value = ''; // Clear email input
        passwordInput.value = ''; // Clear password input
        // Redirect to a new page or handle successful login
        // window.location.href = '/dashboard'; // Example redirect
      } else {
        // Handle invalid login
        alert('Invalid email or password.');
      }

      // Example of an AJAX request (uncomment to use)
      /*
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
      */
    });

    forgotPasswordLink.addEventListener('click', (e) => {
      e.preventDefault();
      const email = emailInput.value.trim();

      if (!validateEmail(email)) {
        alert('Please enter a valid email address to reset your password.');
        return;
      }

      
      
      alert('Password reset email sent to ' + email);
    });

    togglePasswordButton.addEventListener('click', () => {
      const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
      passwordInput.setAttribute('type', type);
      togglePasswordButton.textContent = type === 'password' ? 'Show' : 'Hide';
    });

    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    }
  });
