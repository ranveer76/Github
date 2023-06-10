let i=0
window.onload=function(){
    change();
    screen_width();
}
window.onresize=function(){
    screen_width();
}

function screen_width(){
    let x=window.innerWidth;
    let y=window.innerHeight;
    let z=`<p>Width:${x}</p><p>Height:${y}</p>`;
    document.getElementById('screen').innerHTML=z;
}
function add_a(){
    let a="https://www.google.com/",a1="Google"+i;
    let y=`<button type="button" id="a_btn_${i}" class="remove" onclick="remove(${i})">X</button>`
    let x=`<div id="${i}"><a href="${a}" id="a_${i}" target="_blank">${a1}</a>`+y+"</div>";
    return x;
}
function add_b(){
    let b=`<div id="${i}"><button type="button" id="button_${i}" onclick="">BUTTON_${i}</button>`
    let y=`<button type="button" id="button_btn_${i}" class="remove" onclick="remove(${i})">X</button></div>`
    let x=b+y;
    return x;
}
function add_c(){
    let c=`<div id="${i}"><input type="text" id="input_${i}" placeholder="INPUT_${i}">`
    let y=`<button type="button" id="input_btn_${i}" class="remove" onclick="remove(${i})">X</button></div>`
    let x=c+y;
    return x;
}
function remove(l){
    let x=document.getElementById(`${l}`);
    x.remove();
}
function add(j){
    let x=document.getElementById('testing');
    x.innerHTML+=j;
    i++;
}
function change(){
    let change=document.getElementById('select_1').value;
    let b=document.getElementById('add_btn_1');
    if(change=="1"){
        b.setAttribute("onclick","add(add_a())");
    }
    else if(change=="2"){
        b.setAttribute("onclick","add(add_b())");
    } else if(change=="3"){
        b.setAttribute("onclick","add(add_c())");
    }
}