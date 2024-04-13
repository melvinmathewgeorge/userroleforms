  document.getElementById("registrationForm").addEventListener("submit", function(event) {
    var name = document.getElementById("id_name").value.trim();
    var password = document.getElementById("id_password").value.trim();
    var confirm_password = document.getElementById("id_confirm_password").value.trim();
    var email = document.getElementById("id_email").value.trim();

    if (password != confirm_password) {
      event.preventDefault(); 
      alert("Password and Confirm password not matching");
    } 
    if (name === "" || password === "" || email === "" ) {
      event.preventDefault(); 
      alert("Please fill in all fields.");
    }
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      event.preventDefault(); 
      alert("Please enter a valid email address.");
    }
  });