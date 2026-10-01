var toggle = document.getElementById("toggle");
var toggleIcon = document.getElementById("toggleIcon");
function change() {
  document.body.classList.toggle("dark-mode");
  if (toggleIcon.src.includes("light")) {
    toggleIcon.src = "/static/images/profile/dark.png";
  } else {
    toggleIcon.src = "/static/images/profile/light.png";
  }
}

function change2() {
  document.body.classList.toggle("dark-mode");
  if (toggleIcon.src.includes("light")) {
    toggleIcon.src = "/static/images/profile/dark.png";
  } else {
    toggleIcon.src = "/static/images/profile/light.png";
  }
}
