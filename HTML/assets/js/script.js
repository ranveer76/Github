let data={
    'EXCEL-FETCH/':['Excel Fetch','excel_fetch.png'],
    'fee_eval/':['Fee Evaluation','fee_eval.png'],
    'ranveer76.github.io/':['Assignment_1','assignment_1.png'],
    'HTML_FORM/':['HTML Form','html_form.png'],
    'HTML_SEARCH/':['HTML Search','html_search.png'],
    'html-buttons/':['HTML Buttons','html_buttons.png'],
    'testing/':['Testing','testing.png'],
    'html-navbar/':['HTML Navbar','html_navbar.png'],
    'excel/':['Excel','excel_fetch.png'],
    'html_1/':['HTML 1','html_1.png'],
    'web-app/':['Web App','web_app.png'],
    'fee-lab-eval/':['Tribute Page','tribute.png'],
    'input-variables/':['Input Variables','input_variables.png'],
    'first html.html':['First HTML','first_html.png'],
}
let keys=Object.keys(data);
let values=Object.values(data);
let html='';
for(let i=0;i<keys.length;i++){
    html+=`<div id="${i}">
    <a href="${keys[i]}" class="btn btn-primary">
            <img src="assets/img/${values[i][1]}" alt="${values[i][0]}" class="img-fluid">
            <h5 class="card-title">${values[i][0]}</h5>
            </a>
        </div>`;
}
window.onload=()=>{
    console.log(data);
    console.log('loaded');
    document.getElementById('main').innerHTML+=html;
}