console.log("Hello World");

function check_input(){
    console.log("You're a barf");

    var user_v = document.getElementById("user").value;
    var email_v = document.getElementById("email").value;
    var psgr_v = document.getElementById("psgr").value;

    var user = document.getElementById("user");
    var email = document.getElementById("email");
    var psgr = document.getElementById("psgr");

    if(user_v==""){
        user.style.borderColor = "red";
        alert("Oops! Looks like you forgot to fill out your username");
        return false;
    }else if(email_v==""){
        email.style.borderColor = "red";
        alert("Oops! Looks like you forgot to fill out your email");
        return false;
    }else if(psgr_v=="") {
        psgr.style.borderColor = "red";
        alert("Oops! Looks like you forgot to fill out how many passengers you'd like");
        return false;
    }else{
        return true;
    }
}
