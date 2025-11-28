


console.log("hi")
 document.addEventListener("DOMContentLoaded", function() {

const form = document.getElementById("reviewForm");
 const popup = document.getElementById("authPopup");
  const loginBtn = document.getElementById("loginBtn");
    const closeBtn = document.getElementById("closePopup");
    //check
     if (!form) return;
  const isAuthenticated = form.dataset.auth;
  form.addEventListener("submit", function(event) {
       if (isAuthenticated === "False") {

           // stops the redirect to login page
           event.preventDefault();
           console.log("submission prevented");
           //alert("gotta login");
           popup.style.display = "block";

       }
  });
  closeBtn.addEventListener("click", function() {
        popup.style.display = "none"; // hide popup

    });
  window.addEventListener("click", function(e) {
        if (e.target === popup) {
            popup.style.display = "none";
        }
        });
   if (loginBtn) {
        loginBtn.addEventListener("click", function() {
            window.location.href = loginBtn.dataset.loginUrl;
        });
    }

 });