// window.addEventListener('scroll', function() {
//     var elements = document.querySelectorAll('.services_images');
//     var windowHeight = window.innerHeight;
//     for (var i = 0; i < elements.length; i++) {
//     var position = elements[i].getBoundingClientRect().top;
//         if (position < windowHeight) {
//             elements[i].style.opacity = 1;
//         }
//     }
// });

window.addEventListener('load', function() {
    var elements = document.querySelectorAll('.services_images');
    for (var i = 0; i < elements.length; i++) {
      elements[i].style.opacity = 1;
    }
  });