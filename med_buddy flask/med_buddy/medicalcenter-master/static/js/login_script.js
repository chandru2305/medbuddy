const forms = document.querySelector(".forms"),
      pwShowHide = document.querySelectorAll(".eye-icon"),
      links = document.querySelectorAll(".link"),
      loginForm = document.querySelector(".form.login form"),
      emailField = loginForm.querySelector('input[type="email"]'),
      passwordField = loginForm.querySelector('input[type="password"]');

const validCredentials = {
    email: "crewx@gmail.com",
    password: "12345"
};

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");

        pwFields.forEach(password => {
            if (password.type === "password") {
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
            }
            password.type = "password";
            eyeIcon.classList.replace("bx-show", "bx-hide");
        });
    });
});

links.forEach(link => {
    link.addEventListener("click", e => {
       e.preventDefault(); // Preventing form submit
       forms.classList.toggle("show-signup");
    });
});

loginForm.addEventListener("submit", e => {
    e.preventDefault(); // Prevent the form from submitting the traditional way
    const email = emailField.value;
    const password = passwordField.value;

    if (email === validCredentials.email && password === validCredentials.password) {
        window.location.href = "./index.html"; // Replace with the URL of the next page
    } else {
        alert("Incorrect email or password. Please try again.");
    }
});
