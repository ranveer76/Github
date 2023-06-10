function search(){
    var input = document.getElementById("input").value;
    var url = "https://www.google.com/search?q=" + input;
    window.open(url, "_self");
}
let data = [];
function signup(){
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    let password = document.getElementById("password").value;
    let password2 = document.getElementById("password-confirm").value;
    if(password == password2){
        alert('Welcome ' + name + '!'+'\n your email is ' + email +'\nyour phone no. is'+ phone +'\n your password is ' + password);
        data=[
            {
                'name':name,
                'email':email,
                'phone':phone,
                'password':password
            }
        ]
        console.log(data);
    }
    document.getElementById("name").value="";
    document.getElementById("email").value="";
    document.getElementById("phone").value="";
    document.getElementById("password").value="";
    document.getElementById("password-confirm").value="";
}