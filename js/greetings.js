var time = new Date().getHours();
var greeting = document.getElementById("greetings");
if (time >= 5 && time < 12) {
  greeting.textContent = "Good Morning! Have a Nice Day.";
} else if (time >= 12 && time < 17) {
  greeting.textContent = "Good Afternoon!";
} else if (time >= 17 && time < 21) {
  greeting.textContent = "Good Evening!";
} else {
  greeting.textContent = "Good Night! Have a Healthy Sleep.";
}
