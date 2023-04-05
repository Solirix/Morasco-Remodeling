document.addEventListener("DOMContentLoaded", function() {
    var words = ["BUILT", "DESIGNED", "DEVELOPED", "CREATED", "ENGINEERED", "MADE", "CONSTRUCTED", "CONCOCTED", "CONSTRUCTED"];
    var rotatingWord = document.getElementById("rotating-word");
    var index = 0;
    setInterval(function() {
    rotatingWord.innerHTML = words[index];
    index++;
    if (index == words.length) {
        index = 0;
    }
    }, 2000);

  });
