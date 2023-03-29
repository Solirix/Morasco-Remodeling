
    // var elements = document.querySelectorAll('.port_photos');
    // var windowHeight = window.innerHeight;
    // for (var i = 0; i < elements.length; i++) {
    // var position = elements[i].getBoundingClientRect().top;
    //     if (position < windowHeight) {
    //         elements[i].style.opacity = 1;
    //     }
    // }

    window.addEventListener('load', function() {
        var elements = document.querySelectorAll('.port_photos');
        for (var i = 0; i < elements.length; i++) {
          elements[i].style.opacity = 1;
        }
      });
