
function openFormPick() {
  document.getElementById("myForm-pick").style.display = "block";
}

function closeFormPick() {
  document.getElementById("myForm-pick").style.display = "none";
}

var counter = 0;
function changeImagePick() {
  
  if (counter == 0) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick2.jpeg";
    counter++;
  }
  else if (counter == 1) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick3.jpeg";
    counter++;
  }
  else if (counter == 2) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick4.jpeg";
    counter++;
  }
  else if (counter == 3) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick5.jpeg";
    counter++;
  }
  else if (counter == 4) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick6.jpeg";
    counter++;
  }
  else if (counter == 5) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick7.jpeg";
    counter++;
  }
  else if (counter == 6) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick1.jpeg";
    counter = 0;
  }
}

function openFormShelf() {
  document.getElementById("myForm-shelf").style.display = "block";
}

function closeFormShelf() {
  document.getElementById("myForm-shelf").style.display = "none";
}

var counter = 0;
function changeImageShelf() {
  
  if (counter == 0) {
    document.getElementById("Shelf").src = "https://Shivaen.github.io/Shelf2.jpeg";
    counter++;
  }
  else if (counter == 1) {
    document.getElementById("Shelf").src = "https://Shivaen.github.io/Shelf1.jpeg";
    counter = 0;
  }
  
}