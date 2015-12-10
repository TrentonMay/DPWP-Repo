console.log("Hello World");

function check_input(){
    console.log("You're a barf");

    var user = document.getElementById("user");
    var email = document.getElementById("email");
    var psgr = document.getElementById("psgr");

    if(user==""){
        user.style.borderColor = "red";
        return false
    }else if(email==""){
        user.style.borderColor = "red";
        return false
    }else if(psgr=""){
        user.style.borderColor = "red";
        return false
    }else{
        return true
    }
}
