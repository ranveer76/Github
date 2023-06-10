function dark(){
    document.body.style.backgroundImage = "url('https://static.vecteezy.com/system/resources/previews/002/197/246/large_2x/glowing-neon-line-clipboard-with-checklist-icon-isolated-on-brick-wall-background-control-list-symbol-survey-poll-or-questionnaire-feedback-form-illustration-isolated-on-brick-wall-vector.jpg')";
    document.body.style.backgroundColor = "black";
    document.getElementsByTagName('main')[0].style.backgroundColor = '#00000079';
    document.body.style.color = "white";
}
function light(){
    document.body.style.backgroundImage = "url('https://th.bing.com/th/id/OIP.82IswyeZOHY1W43XDjzz_AHaEK?pid=ImgDet&rs=1')";
    document.body.style.color = "black";
    document.getElementsByTagName('img')[1].style.backgroundColor = "rgb(0 0 0 / 32%)";
    document.getElementsByTagName('main')[0].style.backgroundColor = '#00000024';
    for(var i = 0; i < document.getElementsByTagName('input').length; i++){
        document.getElementsByTagName('input')[i].style.border = "1px solid black";
    }
    for(var i = 0; i < document.getElementsByTagName('textarea').length; i++){
        document.getElementsByTagName('textarea')[i].style.border = "1px solid black";
    }
    for(var i = 0; i < document.getElementsByTagName('select').length; i++){
        document.getElementsByTagName('select')[i].style.border = "1px solid black";
    }
}
function save(){
    let prefix=document.getElementById('prefix').value;
    let first_name=document.getElementById('first-name').value;
    let last_name=document.getElementById('last-name').value;
    let company=document.getElementById('company').value;
    let email=document.getElementById('email').value;
    let phone=document.getElementById('phone').value;
    let website=document.getElementById('website_url').value;
    let banner_type=document.getElementById('bannertype').value;
    let banner_size=document.getElementById('bannersize').value;
    let banner_concept=document.getElementById('bannerconcept').value;
    let banner_content=document.getElementById('bannercontent').value;
    let message=document.getElementById('bannercomments').value;
    let query=document.getElementById('query').value;
    let data={
        prefix:prefix,
        first_name:first_name,
        last_name:last_name,
        company:company,
        email:email,
        phone:phone,
        website:website,
        banner_type:banner_type,
        banner_size:banner_size,
        banner_concept:banner_concept,
        banner_content:banner_content,
        message:message,
        query:query
    }
    localStorage.setItem('data',JSON.stringify(data));
    alert('Data Saved');
    console.log(data);
}
function load(){
    let data=JSON.parse(localStorage.getItem('data'));
    document.getElementById('prefix').value=data.prefix;
    document.getElementById('first-name').value=data.first_name;
    document.getElementById('last-name').value=data.last_name;
    document.getElementById('company').value=data.company;
    document.getElementById('email').value=data.email;
    document.getElementById('phone').value=data.phone;
    document.getElementById('website_url').value=data.website;
    document.getElementById('bannertype').value=data.banner_type;
    document.getElementById('bannersize').value=data.banner_size;
    document.getElementById('bannerconcept').value=data.banner_concept;
    document.getElementById('bannercontent').value=data.banner_content;
    document.getElementById('bannercomments').value=data.message;
    document.getElementById('query').value=data.query;
}
function clear(){
    localStorage.clear();
    alert('Data Cleared');
}