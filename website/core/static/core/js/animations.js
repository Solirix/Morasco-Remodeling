window.addEventListener('scroll', function() {
    //source is located in base.html on line 39 below </head> stuff

    var element = document.querySelector('.daddy-perry');
    var position = element.getBoundingClientRect().top;
    var windowHeight = window.innerHeight;
    if (position < windowHeight) {
      element.style.opacity = 1;
    }

    // If you want to add another fade in follow template below baby 
    // // fade in .new-div div
    // var element2 = document.querySelector('.new-div');
    // var position2 = element2.getBoundingClientRect().top;
    // var windowHeight2 = window.innerHeight;
    // if (position2 < windowHeight2) {
    //     element2.style.opacity = 1;
    // }
    //This message was generated by baby boy Perry bbg-4 for master thomas
  });