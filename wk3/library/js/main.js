console.log("Hello World");

function check_input(){
    var user = document.getElementById("user");
    var email = document.getElementById("email");
    var psgr = document.getElementById("psgr");

    if(user==""){
        user.style.borderColor = "red";

    }else if(email==""){
        user.style.borderColor = "red";
    }else if(psgr=""){
        user.style.borderColor = "red";
    }else{
        return false
    }
}
