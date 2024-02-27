function showReview(){
    //document.querySelector(".review-con").style.opacity = "100%"
    //document.querySelector(".product-img").style.filter = "brightness(0.6)"
    document.querySelector(".review-con").classList.add("hover-review");
    document.querySelector(".product-img").classList.add("hover-img");
}
function hideReview(){
    //document.querySelector(".review-con").style.opacity = "0%"
    //document.querySelector(".product-img").style.filter = "brightness(1)"
    document.querySelector(".review-con").classList.remove("hover-review");
    document.querySelector(".product-img").classList.remove("hover-img");
}

var sun = document.getElementById("sun-icon")
var moon = document.getElementById("moon-icon")
var body = document.getElementsByTagName("body")[0]
var introText = document.querySelector("#intro p")

function darkMode(){
    sun.style.display = "none"
    moon.style.display = "block"
    body.classList.toggle("body-dark")
    introText.style.color = "#eeeff1"
}
function lightMode(){
    sun.style.display = "block"
    moon.style.display = "none"
    body.classList.toggle("body-dark")
    introText.style.color = "#3c404a"
}