
let data = [
]
let data1 = [
]
function check_login(){
    data1 = JSON.parse(localStorage.getItem('data1'));
    data = JSON.parse(localStorage.getItem('data'));
    if(data1.length != 0){
        document.getElementById('login-button').style.display = 'none';
        document.getElementById('signup').style.display = 'none';
        document.getElementById('logout-button').style.display = 'block';
    }
    else if(data1.length == 0 && data.length > 0){
        document.getElementById('login-button').style.display = 'block';
        document.getElementById('signup').style.display = 'block';
        document.getElementById('logout-button').style.display = 'none';
        login();
    } else{
        document.getElementById('login-button').style.display = 'none';
        document.getElementById('signup').style.display = 'block';
        document.getElementById('logout-button').style.display = 'none';
        signup();
    }
}
const main_email="ranveerwalia@gmail.com";
let otp=Math.floor(100000 + Math.random() * 900000);
let i=0,email,phone,password,cpassword,name,x=0;

function login1(){
    let email = document.getElementById('login').value;
    let password = document.getElementById('password').value;
    data = JSON.parse(localStorage.getItem('data'));
    if(email == '' || password == ''){
        alert('Please fill all the fields');
    }
    else if(data != null){
        let flag = 0;
        for(let i = 0; i < data.length; i++){
            if((data[i].email == email || data[i].name == email) && data[i].password == password){
                flag = 1;
                break;
            }
        }
        if(flag == 1){
            data1 = [];
            data1 = data[i];
            localStorage.setItem('data1', JSON.stringify(data1));
            alert('Login successful');
            home();
        }
        else{
            alert('Invalid email or password');
        }
    }
    else{
        alert('Invalid email or password');
    }
}

function closePopup(){
    document.getElementById('popup').style.display = 'none';
}

function sendmessage(){
    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "ranveerwalia76@gmail.com",
        Password : "B06A00407F554EC90417C0E9CB747540EAB9",
        To : email,
        From : "ranveerwalia76@gmail.com",
        Subject : "OTP",
        Body : "Your OTP is "+otp
    }).then(
      message => alert(message)
    );
}
function popupOtp(){
    let otp1 = document.getElementById('popup-otp').value;
    name = document.getElementById('login').value;
    if(otp1 == otp){
        if(data == null){
            data = [];
        }
        data.push({name: name, email: email, phone: phone, password: password});
        if(data1 != null){
            data1 = [];
    }
    localStorage.setItem('data', JSON.stringify(data));
    alert('Signup successful');
    document.getElementById('email').value = '';
    document.getElementById('phone').value = '';
    document.getElementById('password').value = '';
    document.getElementById('password-confirm').value = '';
closePopup();
login();}
    else{
        alert('Invalid OTP');
    }
    document.getElementById('login').value = '';

}
function signup1(){
    name = document.getElementById('login').value;
    email = document.getElementById('email').value;
    phone = document.getElementById('phone').value;
    password = document.getElementById('password').value;
    cpassword = document.getElementById('password-confirm').value;
    if(name == '' || email == '' || password == '' || cpassword == ''){
        alert('Please fill all the fields');
    }
    else if(password != cpassword){
        alert('Password and Confirm Password does not match');
    }
    else{
        sendmessage();
        document.getElementById('popup').style.display = 'block';
    }
}
function forgot(){
    email = document.getElementById('login').value;
    let flag = 0;
    data = JSON.parse(localStorage.getItem('data'));
    if(data != null){for(i = 0; i < data.length; i++){
        if(data[i].email == email){
            flag = 1;
            break;
        }
    }
    if(flag == 1){
        sendmessage();
        alert('OTP sent to your email');
        document.getElementById('popup').style.display = 'block';
    }
    else{
        alert('Invalid email');
    }} else{
        alert('Invalid email');
    }
}
function popOtp(){
    let otp1 = document.getElementById('popup-otp').value;
    let password = document.getElementById('popup-password').value;
    let cpassword = document.getElementById('popconf-password').value;
    if(otp1 == otp && password == cpassword){
        data[i].password = password;
        localStorage.setItem('data', JSON.stringify(data));
        data1 = null;
        data1=data[i];
        localStorage.setItem('data1', JSON.stringify(data1));
        alert('Password changed successfully');
        closePopup();
    }

}
function logout(){
    data1 = [];
    localStorage.setItem('data1', JSON.stringify(data1));
    alert('Logout successful');
    x--;
    login();
}
function loginvalidate(){

    if(x<1){window.setTimeout(function() {
        // if(data != null){
        //     document.getElementById('login-button').style.display = 'none';
        //     document.getElementById('signup').style.display = 'none';
        //     document.getElementById('logout-button').style.display = 'block';
        // } else{
        //     document.getElementById('login-button').style.display = 'block';
        //     document.getElementById('signup').style.display = 'block';
        //     document.getElementById('logout-button').style.display = 'none';
        //     signup();
        // }
        x++;
        check_login();
    }, 5);}
}
function home(){
    document.getElementById("main").setAttribute("include-html", 'main.html');
    document.getElementsByClassName('active')[0].classList.remove('active');
    document.getElementById('home').classList.add('active');
    includeHTML();
    x--;
    loginvalidate();
}
function about(){
    document.getElementById("main").setAttribute("include-html", 'about.html');
    document.getElementsByClassName('active')[0].classList.remove('active');
    document.getElementById('about').classList.add('active');
    includeHTML();
    x--;
    loginvalidate();
}
function contact(){
    document.getElementById("main").setAttribute("include-html", 'contact.html');
    document.getElementsByClassName('active')[0].classList.remove('active');
    document.getElementById('contact').classList.add('active');
    includeHTML();
    x--;
    loginvalidate();
}
function login(){
    document.getElementById("main").setAttribute("include-html", 'login.html');
    document.getElementsByClassName('active')[0].classList.remove('active');    
    document.getElementById('login-button').classList.add('active');
    includeHTML();
    loginvalidate();
}
function signup(){
    document.getElementById("main").setAttribute("include-html", 'signup.html');
    document.getElementsByClassName('active')[0].classList.remove('active');
    document.getElementById('signup').classList.add('active');
    includeHTML();
}
window.onload = function() {
    includeHTML();
    if(data == null){
        data = [];
    } else{
        data = JSON.parse(localStorage.getItem('data'));
    }
    if(data1 == null){
        data1 = [];
        } else{
            JSON.parse(localStorage.getItem('data1'));
        }
    loginvalidate();
}
function includeHTML(){
    var z, i, elmnt, file, xhttp;
    z = document.getElementsByTagName("*");
    for(i = 0; i < z.length; i++){
        elmnt = z[i];
        file = elmnt.getAttribute("include-html");
        if(file){
            xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function(){
                if(this.readyState == 4){
                    if(this.status == 200){elmnt.innerHTML = this.responseText;}
                    if(this.status == 404){elmnt.innerHTML = "Page not found.";}
                    elmnt.removeAttribute("include-html");
                    includeHTML();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            return;
        }
    }
}