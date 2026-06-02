const form = document.getElementById("resultForm");
const regnoInput = document.getElementById("registerno");
const error = document.getElementById("error");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  

  localStorage.setItem("regno", regnoInput.value.trim());
  window.location.href = "resultwebpage2.html";
});