const pop= document.getElementById('pop_up');

const hide_pop= () => { pop.style.display= 'none'; }
const show_pop= () => { pop.style.display= 'block'; }

document.addEventListener('mouseleave', show_pop);
document.getElementsByClassName('close')[0].addEventListener('click', hide_pop);

function save(){
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;

    if(name == "" || email == ""){
        alert("Please fill your name and email to continue\n\nelse close the pop up");
    }else{
        alert("Thank you for subscribing\n\nYou will be notified when we launch");
    }
    document.getElementById('name').value = "";
    document.getElementById('email').value = "";
}

function back(){
    document.body.classList.remove('back2');
}
function back2(){
    document.body.classList.add('back2');
}