


console.log("hi")


document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reviewform');
    form.addEventListener('submit', (e) => {
        // Check if user is logged in
        const isAuthenticated = "{{ user.is_authenticated|yesno:'True,False' }}";
        if (isAuthenticated === "False") {
            e.preventDefault(); // stop the form submission
            alert("You must log in to post a review!");
           // window.location.href = '/login/?next=' + window.location.pathname;
        }
    });
});