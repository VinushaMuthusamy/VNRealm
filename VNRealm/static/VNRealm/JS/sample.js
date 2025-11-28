

//loading  test
console.log("hi")
 document.addEventListener("DOMContentLoaded", function() {

     //review post
    const form = document.getElementById("reviewForm");
    //authentication pop window
    const popup = document.getElementById("authPopup");
    //login/signup page redirection
    const loginBtn = document.getElementById("loginBtn");
    //closing popup
    const closeBtn = document.getElementById("closePopup");
    //check if no form
     if (!form) return;
     //dataset reads metadata info such as authentication state
  const isAuthenticated = form.dataset.auth;

  //pop up window function
  form.addEventListener("submit", function(event) {
      //if not authenticated window will appear
       if (isAuthenticated === "False") {

           // stops the redirect to login page
           event.preventDefault();
           console.log("submission prevented");
           //alert("gotta login");
           popup.style.display = "block";

       }
  });
  //clicking close button in the window will close it
  closeBtn.addEventListener("click", function() {
        popup.style.display = "none"; // hide popup

    });

  //clicking outside the window will also close it
  window.addEventListener("click", function(e) {
        if (e.target === popup) {
            popup.style.display = "none";
        }
        });

  //if login/signup button clicked it would redirect to login page
   if (loginBtn) {
        loginBtn.addEventListener("click", function() {
            window.location.href = loginBtn.dataset.loginUrl;
        });
    }

 });