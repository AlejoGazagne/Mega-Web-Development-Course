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

var productImg = document.querySelector(".product-img")
productImg.addEventListener("mouseover", showReview)
productImg.addEventListener("mouseout", hideReview)

function print(){
    console.log("The video ended.")
}
var video = document.querySelector("#video")
video.addEventListener("ended", print)

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

function CreatUser(name, lastname){
    this.name = name;
    this.lastname = lastname;
}

function submitForm(){
    userName = document.getElementById("name").value
    userLastName = document.getElementById("lastname").value
    var user1 = new CreatUser(userName, userLastName)
    var greeting = "Hi " + user1.name + " " + user1.lastname + ", welcome"
    document.getElementById("tit").textContent = greeting
}