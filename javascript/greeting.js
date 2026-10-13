const date = new Date();

const hour = date.getHours();

function greeting() {
  if (hour >= 6 && hour < 12) {
    return "Good morning! ☀️ Have a nice day.";
  } else if (hour >= 12 && hour < 16) {
    return "Good Afternoon 🌿";
  } else if (hour >= 16 && hour < 19) {
    return "Good Evening 🌆";
  } else if (hour >= 19 && hour < 22) {
    return "Good night! 🌙 How was your day?";
  } else {
    return "It’s getting late. Time to rest. Good Night! 🌌";
  }
}

document.getElementById("greeting-text").innerHTML = greeting(hour);
