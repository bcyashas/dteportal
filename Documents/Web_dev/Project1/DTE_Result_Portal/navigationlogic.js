const form = document.getElementById("resultForm");
const regnoInput = document.getElementById("registerno");
const error = document.getElementById("error");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (regnoInput.value === "") {
    error.innerHTML = "Register Number is required";
    return;
  }

  localStorage.setItem("regno", regnoInput.value.trim());
  window.location.href = "resultwebpage2.html";
});