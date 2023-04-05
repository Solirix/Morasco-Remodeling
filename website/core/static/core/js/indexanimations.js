window.addEventListener('scroll', function() {
  var element = document.querySelector('.daddy-perry');
  var position = element.getBoundingClientRect().top;
  var windowHeight = window.innerHeight;
  if (position < windowHeight) {
    element.style.opacity = 1;
  }
});

