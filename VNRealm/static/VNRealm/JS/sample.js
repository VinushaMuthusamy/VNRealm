


console.log("hi")
 document.addEventListener("DOMContentLoaded", function() {

const form = document.getElementById("reviewForm");
 const popup = document.getElementById("authPopup");
  const loginBtn = document.getElementById("loginBtn");
    const closeBtn = document.getElementById("closePopup");
     if (!form) return; // safety check
  const isAuthenticated = form.dataset.auth;
  form.addEventListener("submit", function(event) {
       if (isAuthenticated === "False") {

           event.preventDefault(); // stops the redirect to /otherpage/
           console.log("Form submission prevented!");
           //alert("gotta login");
           popup.style.display = "block";

       }
    // You can now handle the data with JS (AJAX, validation, etc.)
  });
  closeBtn.addEventListener("click", function() {
        popup.style.display = "none"; // hide popup

    });
  window.addEventListener("click", function(e) {
        if (e.target == popup) {
            popup.style.display = "none";
        }
        });
   if (loginBtn) {
        loginBtn.addEventListener("click", function() {
            window.location.href = loginBtn.dataset.loginUrl;
        });
    }

 });