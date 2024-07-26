ClickHeader = document.getElementById('toggle_header');

ClickHeader.addEventListener('click', function () {
    if (document.querySelector('header').className === "green") {
        document.querySelector('header').classList.toggle("green");
        document.querySelector('header').classList.add("red");
    } else {
        document.querySelector('header').classList.toggle("red");
        document.querySelector('header').classList.add("green"); 
    }

});
