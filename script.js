

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

var counter = 6;
function changeImagePickBack() {
  
  if (counter == 6) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick6.jpeg";
    counter--;
  }
  else if (counter == 5) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick5.jpeg";
    counter--;
  }
  else if (counter == 4) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick4.jpeg";
    counter--;
  }
  else if (counter == 3) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick3.jpeg";
    counter--;
  }
  else if (counter == 2) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick2.jpeg";
    counter--;
  }
  else if (counter == 1) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick1.jpeg";
    counter--;
  }
  else if (counter == 0) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/Pick7.jpeg";
    counter = 6;
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

var counter = 1;
function changeImageShelfBack() {
  
  if (counter == 1) {
    document.getElementById("Shelf").src = "https://Shivaen.github.io/Shelf1.jpeg";
    counter--;
  }
  else if (counter == 0) {
    document.getElementById("Shelf").src = "https://Shivaen.github.io/Shelf2.jpeg";
    counter = 1;
  }
  
}

function openFormDOTS() {
  document.getElementById("myForm-DOTS").style.display = "block";
}

function closeFormDOTS() {
  document.getElementById("myForm-DOTS").style.display = "none";
}

var counter = 0;
function changeImageDOTS() {
  
  if (counter == 0) {
    document.getElementById("DOTS").src = "https://Shivaen.github.io/DOTS2.jpeg";
    counter++;
  }
  else if (counter == 1) {
    document.getElementById("DOTS").src = "https://Shivaen.github.io/DOTS3.jpeg";
    counter++;
  }
  else if (counter == 2) {
    document.getElementById("Pick").src = "https://Shivaen.github.io/DOTS1.jpeg";
    counter = 0;
  }

}

var counter = 2;
function changeImageDOTSBack() {
  
  if (counter == 2) {
    document.getElementById("DOTS").src = "https://Shivaen.github.io/DOTS2.jpeg";
    counter--;
  }
  else if (counter == 1) {
    document.getElementById("DOTS").src = "https://Shivaen.github.io/DOTS1.jpeg";
    counter--;
  }
  else if (counter == 0) {
    document.getElementById("DOTS").src = "https://Shivaen.github.io/DOTS3.jpeg";
    counter = 2;
  }
}

function openFormED() {
  document.getElementById("myForm-ED").style.display = "block";
}

function closeFormED() {
  document.getElementById("myForm-ED").style.display = "none";
}

var counter = 0;
function changeImageED() {
  
  if (counter == 0) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED2.jpeg";
    counter++;
  }
  else if (counter == 1) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED3.jpeg";
    counter++;
  }
  else if (counter == 2) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED4.jpeg";
    counter++;
  }
  else if (counter == 3) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED1.jpeg";
    counter = 0;
  }
}

var counter = 3;
function changeImageEDBack() {
  
  if (counter == 3) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED3.jpeg";
    counter--;
  }
  else if (counter == 2) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED2.jpeg";
    counter--;
  }
  else if (counter == 1) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED1.jpeg";
    counter--;
  }
  else if (counter == 0) {
    document.getElementById("ED").src = "https://Shivaen.github.io/ED4.jpeg";
    counter = 3;
  }
  
}