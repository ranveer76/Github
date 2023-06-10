// Load the XLSX library
const table = document.getElementById('excel-table');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const searchInput = document.getElementById('search');
const srInput = document.getElementById('sr');

// Load the Excel file using Fetch API
fetch('js/test1.xlsx')
    .then(response => response.arrayBuffer())
    .then(buffer => {
        // Convert the Excel buffer to a workbook object
        const workbook = XLSX.read(buffer, { type: 'array' });
        const worksheet = workbook.Sheets[workbook.SheetNames[0]];
        const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

        // Loop through the data and create HTML table rows and cells
        data.forEach(row => {
            const tr = document.createElement('tr');
            row.forEach(cellValue => {
                const td = document.createElement('td');
                td.textContent = cellValue;
                tr.appendChild(td);
            });
            if (table.rows.length > 0) {
                tr.innerHTML += `<td><button type="button" class="f" id="b${table.rows.length}" value="${table.rows.length}" onclick="deleteRow(${table.rows.length})">Delete</button></td>
      <td><button type="button" class="f1" value="${table.rows.length}" onclick="editRow(${table.rows.length})">Edit</button></td>`;
            } table.appendChild(tr);
        });
        for (let i = 1; i< table.rows.length; i++) {
            table.rows[i].cells[0].textContent = i;
            table.rows[i].setAttribute('id', `${i}`);
            table.rows[i].cells[4].setAttribute('id', `b${i}`);
            table.rows[i].cells[4].setAttribute('value', `${i}`);
            table.rows[i].cells[4].setAttribute('onclick', `deleteRow(${i})`);
            table.rows[i].cells[5].setAttribute('onclick', `editRow(${i})`);
            table.rows[i].cells[5].setAttribute('value', `${i}`);
    }
    });

// Function to add a new row to the table
function addRow() {
    const sr = table.rows.length;
    const tr = document.createElement('tr');

    tr.innerHTML = `
    <td>${sr}</td>
    <td>${nameInput.value}</td>
    <td>${emailInput.value}</td>
    <td>${phoneInput.value}</td>
    <td><button type="button" class="f" id="b${sr}" value="${sr}" onclick="deleteRow(${sr})">Delete</button></td>
    <td><button type="button" class="f1" value="${sr}" onclick="editRow(${sr})">Edit</button></td>
  `;

    table.appendChild(tr);
    for (let i = 1; i< table.rows.length; i++) {
        table.rows[i].cells[0].textContent = i;
        table.rows[i].setAttribute('id', `${i}`);
        table.rows[i].cells[4].setAttribute('id', `b${i}`);
        table.rows[i].cells[4].setAttribute('value', `${i}`);
        table.rows[i].cells[4].setAttribute('onclick', `deleteRow(${i})`);
        table.rows[i].cells[5].setAttribute('onclick', `editRow(${i})`);
        table.rows[i].cells[5].setAttribute('value', `${i}`);
}
    reset();
}

// Function to delete a row from the table
// Function to delete a row from the table
function deleteRow(index) {
    // Get the row index based on the button value
    const sr = parseInt(index) ;
    if(sr!=0){
        table.deleteRow(sr);
    }
    // Update the index of the remaining rows
    for (let i = 1; i< table.rows.length; i++) {
        table.rows[i].cells[0].textContent = i;
        table.rows[i].setAttribute('id', `${i}`);
        table.rows[i].cells[4].setAttribute('id', `b${i}`);
        table.rows[i].cells[4].setAttribute('value', `${i}`);
        table.rows[i].cells[4].setAttribute('onclick', `deleteRow(${i})`);
        table.rows[i].cells[5].setAttribute('onclick', `editRow(${i})`);
        table.rows[i].cells[5].setAttribute('value', `${i}`);
}
}

// Function to search the table for a given value
function search() {
    const val = searchInput.value.toLowerCase();

    for (let i = 0; i < table.rows.length; i++) {
        const row = table.rows[i];
        const name = row.cells[1].textContent.toLowerCase();
        const email = row.cells[2].textContent.toLowerCase();
        const phone = row.cells[3].textContent.toLowerCase();

        if (val === '') {
            row.style.display = '';
        } else if (name.includes(val) || email.includes(val) || phone.includes(val)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    }

    reset();
}

// Function to edit a row in the table
function editRow(sr) {
    const row = table.rows[sr];
    nameInput.value = row.cells[1].textContent;
    emailInput.value = row.cells[2].textContent;
    phoneInput.value = row.cells[3].textContent;
    srInput.value = sr;
}

// Function to update a row in the table
function updateRow() {
    const sr = srInput.value;

    if (sr !== '') {
        const row = table.rows[sr];
        row.cells[1].textContent = nameInput.value;
        row.cells[2].textContent = emailInput.value;
        row.cells[3].textContent = phoneInput.value;
    }
    reset();
}
function reset() {
    document.getElementById('name').value = '';
    document.getElementById('email').value = '';
    document.getElementById('phone').value = '';
    document.getElementById('sr').value = '';
    document.getElementById('search').value = '';
}