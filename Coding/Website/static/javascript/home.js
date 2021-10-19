var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("myRecommendations");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  slides[slideIndex-1].style.display = "block";  
}

//reference from w3 schools (above)
function deleteRec(aID) {
  fetch("/deleteRec", {
    method: "POST",
    body: JSON.stringify({ aID: aID }),
  }).then((_res) => {
    window.location.href = "/home";
  });
}