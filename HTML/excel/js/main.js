let table = document.querySelector('.table');
let i=0;
table.innerHTML = '<table><thead><tr><th>Row</th><th>Name</th><th>Phone</th><th>Email</th></tr></thead><tbody></tbody></table>';
// (
//     async () => {
//         let wb = XLSX.read(await(await fetch("./excel.xlsx")).arrayBuffer());
//         console.log(wb);
//         let sheet=wb.SheetNames[0];
//         let ws = wb.Sheets[sheet];
//         let html = XLSX.utils.sheet_to_html(ws);
//         table.innerHTML += `<h1>Excel to HTML ${sheet}</h1>${html}`;
//     }
// )()
function exportExcel() {
    let wb = XLSX.utils.table_to_book(table);
    XLSX.writeFile(wb, 'excel.xlsx');
}
function upload(){
    let file = document.querySelector('#file').files[0];
    let reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onload = function(){
        let data = new Uint8Array(reader.result);
        let wb = XLSX.read(data, {type:'array'});
        console.log(wb);
        let sheet=wb.SheetNames[0];
        let ws = wb.Sheets[sheet];
        let html = XLSX.utils.sheet_to_html(ws);
        table.innerHTML += `<h1>Excel to HTML ${sheet}</h1><button type="button" id="fix" onclick="fix()">fix</button>${html}`;
    }
}
function fix(){
    document.getElementsByTagName('tr')[0].innerHTML='<th data-t="s" data-v="SR.NO." id="sjs-A1">SR.NO.</th><th data-t="s" data-v="NAME" id="sjs-B1">NAME</th><th data-t="s" data-v="AREA" id="sjs-C1">AREA</th><th data-t="s" data-v="PHONE NO." id="sjs-D1">PHONE NO.</th><th data-t="s" data-v="BOX NO." id="sjs-E1">BOX NO.</th><th data-t="s" data-v="BOX NO.2" id="sjs-F1">BOX NO.2</th><th data-t="s" data-v="PRICE" id="sjs-G1">PRICE</th><th data-t="s" data-v="PACK" id="sjs-H1">PACK</th><th data-t="s" data-v="PACK 2" id="sjs-I1">PACK 2</th><th data-t="s" data-v="PACK 3" id="sjs-J1">PACK 3</th><th data-t="s" data-v="JAN" id="sjs-K1">JAN</th><th data-t="s" data-v="FEB" id="sjs-L1">FEB</th><th data-t="s" data-v="MAR" id="sjs-M1">MAR</th><th data-t="s" data-v="APRIL" id="sjs-N1">APRIL</th><th data-t="s" data-v="MAY" id="sjs-O1">MAY</th><th data-t="s" data-v="JUNE" id="sjs-P1">JUNE</th><th data-t="s" data-v="JULY" id="sjs-Q1">JULY</th><th data-t="s" data-v="AUG" id="sjs-R1">AUG</th><th data-t="s" data-v="SEP" id="sjs-S1">SEP</th><th data-t="s" data-v="OCT" id="sjs-T1">OCT</th><th data-t="s" data-v="NOV" id="sjs-U1">NOV</th><th data-t="s" data-v="DEC" id="sjs-V1">DEC</th><th data-t="s" data-v="BAL" id="sjs-W1">BAL</th>';
    for(let j=0;j<document.getElementsByTagName('tr').length;j++){
        for(let k=5;k<document.getElementsByTagName('tr')[j].cells.length;k++){
            document.getElementsByTagName('tr')[j].cells[k].style.display = 'none';
        }
        if(j>0){
            document.getElementsByTagName('tr')[j].setAttribute('id',j);
            document.getElementsByTagName('tr')[j].innerHTML +=     
            `<td><button type="button" id="edit${j}" onclick="edit(${j})">Edit</button></td>
            <td><button type="button" id="del${j}" onclick="del(${j})">Delete</button></td>`;
        }
    }
}
function add(){
    let name = document.querySelector('#name').value;
    let phone = document.querySelector('#phone').value;
    let email = document.querySelector('#email').value;
    let row = i;

    document.querySelector('tbody').innerHTML += 
    `<tr id="${row}"><td id="row${row}">${row +1}</td>
    <td id="name${row}">${name}</td>
    <td id="phone${row}">${phone}</td>
    <td id="email${row}">${email}</td></tr>`;

    document.getElementById(row).innerHTML +=
    `<td><button type="button" id="edit${row}" onclick="edit(${row})">Edit</button></td>
    <td><button type="button" id="del${row}" onclick="del(${row})">Delete</button></td>`;
    i++;
    reset();
}
function del(row){
    document.getElementById(row).remove();
    i--;
    for(let j=0;j<document.getElementsByTagName('tr').length;j++){
        document.getElementsByTagName('tr')[j+1].cells[0].innerText = j+1;
    }
}
function edit(row){
    document.querySelector('#name').value = document.querySelector(`#name${row}`).innerText;
    document.querySelector('#phone').value = document.querySelector(`#phone${row}`).innerText;
    document.querySelector('#email').value = document.querySelector(`#email${row}`).innerText;
    document.querySelector('#index').value = row;
}
function update(){
    let name = document.querySelector('#name').value;
    let phone = document.querySelector('#phone').value;
    let email = document.querySelector('#email').value;
    let row = document.querySelector('#index').value;
    document.querySelector(`#name${row}`).innerText = name;
    document.querySelector(`#phone${row}`).innerText = phone;
    document.querySelector(`#email${row}`).innerText = email;
    reset();
}
function search(){
    let search = document.querySelector('#search').value;
    search = search.toUpperCase();
    let rows = document.getElementsByTagName('tr');
    for(let j=1;j<i+1;j++){
        if(rows[j].cells[1].innerText.toUpperCase().includes(search) || rows[j].cells[2].innerText.toUpperCase().includes(search) || rows[j].cells[3].innerText.toUpperCase().includes(search)){
            rows[j].style.display = '';
        }
        else{
            rows[j].style.display = 'none';
        }
    }
}
function reset(){
    document.querySelector('#name').value = '';
    document.querySelector('#phone').value = '';
    document.querySelector('#email').value = '';
    document.querySelector('#file').value = '';
    document.querySelector('#index').value = '';
}