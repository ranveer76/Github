function add(){
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let sr = document.getElementById('t').rows.length;
    document.getElementById('t').innerHTML += '<tr id="'+(sr)+'"><td>'+(sr+1)+'</td><td>'+name+'</td><td>'+email+'</td><td>'+phone+'</td><td><button type="button" class="f" id="b'+sr+'" value="'+sr+'" onclick="del(value)">Delete</button></td><td><button type="button" class="f1" value="'+(sr)+'" onclick="edit(value)">edit</button></td></tr>';
    document.getElementById('t').rows[sr].cells[4].value = sr;
    document.getElementById('t').rows[sr].cells[5].value = sr;
    reset();
}
function del(val){
    document.getElementById(val).remove();
    for(let i=0;i<document.getElementById('t').rows.length;i++){
        document.getElementById('t').rows[i].cells[0].innerHTML = i+1;
    }
}
function search(){
    let val = document.getElementById('search').value;
    for(let i=0;i<document.getElementById('t').rows.length;i++){
        if(val == ''){
            document.getElementById('t').rows[i].style.display = '';
        }
        else if(document.getElementById('t').rows[i].cells[0].innerHTML == val||document.getElementById('t').rows[i].cells[1].innerHTML == val || document.getElementById('t').rows[i].cells[2].innerHTML == val || document.getElementById('t').rows[i].cells[3].innerHTML == val){
            document.getElementById('t').rows[i].style.display = '';
        } else {
            document.getElementById('t').rows[i].style.display = 'none';
        }
    }
    reset();
}
function update(){
    let val=document.getElementById('sr').value;
    if (val != ''){
    document.getElementById(val).cells[1].innerHTML = document.getElementById('name').value;
    document.getElementById(val).cells[2].innerHTML = document.getElementById('email').value;
    document.getElementById(val).cells[3].innerHTML = document.getElementById('phone').value;
    }
    reset();
}
function edit(val){
    document.getElementById('name').value = document.getElementById(val).cells[1].innerHTML;
    document.getElementById('email').value = document.getElementById(val).cells[2].innerHTML;
    document.getElementById('phone').value = document.getElementById(val).cells[3].innerHTML;
    document.getElementById('sr').value = val;
}
function reset(){
    document.getElementById('name').value = '';
    document.getElementById('email').value = '';
    document.getElementById('phone').value = '';
    document.getElementById('sr').value = '';
    document.getElementById('search').value = '';
}