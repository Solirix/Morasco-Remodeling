// Get the alert element
const alert = document.querySelector('.alert');

// Show the alert
alert.classList.add('show');

// Hide the alert after 3 seconds
setTimeout(function() {
    alert.classList.remove('show');
}, 3000);
