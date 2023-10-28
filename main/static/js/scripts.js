const form = document.getElementById("registration-form");
const showPassword = document.getElementById("show-password");
const passwordInput = form.elements["password"];

showPassword.addEventListener("click", function () {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPassword.textContent = "Hide";
    } else {
        passwordInput.type = "password";
        showPassword.textContent = "Show";
    }
});

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const password = form.elements["password"].value;
    const confirmPassword = form.elements["confirm-password"].value;

    if (password !== confirmPassword) {
        alert("Passwords do not match. Please try again.");
    } else {
        alert("Registration successful!");
        form.reset();
    }
});
