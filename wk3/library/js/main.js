//The function below will check to see if all the text fields in the form has been filled out
function check_input(){

    var user_v = document.getElementById("user").value; //getting the value of the username
    var email_v = document.getElementById("email").value;   //getting the value of the email
    var psgr_v = document.getElementById("psgr").value; //getting the value of the passengers

    var user = document.getElementById("user"); //getting the id of the input for username
    var email = document.getElementById("email");   //getting the id of the input for email
    var psgr = document.getElementById("psgr"); //getting the id of the input for passengers

    if(user_v==""){
        user.style.borderColor = "red"; //Alerts the user by coloring the field red showing that they have not filled out the field
        return false;   //Prevents the page from moving forward
    }else if(email_v==""){
        email.style.borderColor = "red";    //Alerts the user by coloring the field red showing that they have not filled out the field
        return false;   //Prevents the page from moving forward
    }else if(psgr_v=="") {
        psgr.style.borderColor = "red"; //Alerts the user by coloring the field red showing that they have not filled out the field
        return false;   //Prevents the page from moving forward
    }else{
        return true;    //Allows the page to move forward if all of the inputs are filled out
    }
}
