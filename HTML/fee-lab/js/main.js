window.onload = function () {
    index();
}

function search() {
    let search = document.getElementById('search').value;
    const p = document.getElementById('tribute-para');
    let regex = new RegExp(search, 'gi');
    let x= p.textContent.search(regex);
    if (search != "" && x != -1) {
        p.innerHTML = p.textContent.replace(regex, `<mark>$&</mark>`);
    }
    else {
        let t = document.getElementById('outter');
        p.innerHTML = p.textContent.replace(regex, `$&`);
        t.innerHTML =`<h1>Not Found Error</h1><br>
        !>> ${search} not found in the page.
        <br><br>!>> we could redirect you to google search or wikipedia search for ${search}...
        <br><br>!>> click on the search button to continue
        <br><br><button type="button" id="s1" onclick='s1()'>wikipedia search</button>
        <button type="button" id="s2" onclick='s2()'>google search</button>
        <br><br>!>> click on cancel to stay on the page
        <button type="button" id="c" onclick='cancel()'>cancel</button>`;
        t.style.display = "block";
    }
}
function cancel() {
    document.getElementById('outter').style.display = "none";
    document.getElementById('search').value = "";
}
function s1(){
    let se = document.getElementById('search').value;
    window.open("https://en.m.wikipedia.org/wiki/" + se);
    cancel();
}
function s2(){
    let se = document.getElementById('search').value;
    window.open("https://www.google.com/search?q=" + se);
    cancel();
}
function screenTop() {
    window.scrollTo(0, 0);
}
function index() {
    screenTop();
    document.getElementById('tribute-data').innerHTML = a;
    document.getElementById('image').src = "https://upload.wikimedia.org/wikipedia/commons/6/6e/A._P._J._Abdul_Kalam.jpg";
    document.getElementById('caption').innerHTML = `
    Great Indian scientist and

    politician who played a leading

    role in the development of India’s

    missile and nuclear weapons

    programs.`;
    document.getElementById('nav').classList.add('active');
    if (document.getElementById('nav1').classList.contains('active')) {
        document.getElementById('nav1').classList.remove('active');
    }
    else if (document.getElementById('nav2').classList.contains('active')) {
        document.getElementById('nav2').classList.remove('active');
    }
    else if (document.getElementById('nav3').classList.contains('active')) {
        document.getElementById('nav3').classList.remove('active');
    }
}
function early() {
    screenTop();
    document.getElementById('tribute-data').innerHTML = a1;
    document.getElementById('image').src = "http://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Vladimir_Putin_with_Abdul_Kalam_26_January_2007.jpg/450px-Vladimir_Putin_with_Abdul_Kalam_26_January_2007.jpg";
    document.getElementById('caption').innerHTML = "Kalam with Russian President Vladimir Putin at the Kremlin in Moscow, 2007";
    document.getElementById('nav1').classList.add('active');
    if (document.getElementById('nav').classList.contains('active')) {
        document.getElementById('nav').classList.remove('active');
    }
    else if (document.getElementById('nav2').classList.contains('active')) {
        document.getElementById('nav2').classList.remove('active');
    }
    else if (document.getElementById('nav3').classList.contains('active')) {
        document.getElementById('nav3').classList.remove('active');
    }
}


function career() {
    screenTop();
    document.getElementById('tribute-data').innerHTML = a2;
    document.getElementById('image').src = "http://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Dr_A_P_J_Abdul_Kalam_addresses_the_14th_Convocation_ceremony_at_the_Indian_Institute_of_Technology_Guwahati.jpg/450px-Dr_A_P_J_Abdul_Kalam_addresses_the_14th_Convocation_ceremony_at_the_Indian_Institute_of_Technology_Guwahati.jpg";
    document.getElementById('caption').innerHTML = "Kalam addresses engineering students at IIT Guwahati";
    document.getElementById('nav2').classList.add('active');
    if (document.getElementById('nav').classList.contains('active')) {
        document.getElementById('nav').classList.remove('active');
    }
    else if (document.getElementById('nav1').classList.contains('active')) {
        document.getElementById('nav1').classList.remove('active');
    }
    else if (document.getElementById('nav3').classList.contains('active')) {
        document.getElementById('nav3').classList.remove('active');
    }
}

function presidence() {
    screenTop();
    document.getElementById('tribute-data').innerHTML = a3;
    document.getElementById('image').src = "http://upload.wikimedia.org/wikipedia/commons/thumb/3/30/APJAbdulKalam.jpg/450px-APJAbdulKalam.jpg";
    document.getElementById('caption').innerHTML = "Kalam at Bijnor a week before his death";
    document.getElementById('nav3').classList.add('active');
    if (document.getElementById('nav').classList.contains('active')) {
        document.getElementById('nav').classList.remove('active');
    }
    else if (document.getElementById('nav1').classList.contains('active')) {
        document.getElementById('nav1').classList.remove('active');
    }
    else if (document.getElementById('nav2').classList.contains('active')) {
        document.getElementById('nav2').classList.remove('active');
    }
}

let a3 = `            <!--Achievements and other

details of the person-->

<h1 class="title-APJ">    Presidency And Death</h1>
<p id="tribute-para">
Presidency

Kalam served as the 11th President of India, succeeding K. R. Narayanan. He won the 2002 presidential election with an electoral vote of 922,884, surpassing the 107,366 votes won by Lakshmi Sahgal. His term lasted from 25 July 2002 to 25 July 2007.During his term as president, he was affectionately known as the People's President.

Death
On 27 July 2015, Kalam travelled to Shillong to deliver a lecture on "Creating a Livable Planet Earth" at the Indian Institute of Management Shillong. While climbing a flight of stairs, he experienced some discomfort, but was able to enter the auditorium after a brief rest.At around 6:35 p.m. IST, only five minutes into his lecture, he collapsed.He was rushed to the nearby Bethany Hospital in a critical condition; upon arrival, he lacked a pulse or any other signs of life.Despite being placed in the intensive care unit, Kalam was confirmed dead of a sudden cardiac arrest at 7:45 p.m IST.
</p>

<div>

<details>
<summary> <p>Remembering APJ Abdul Kalam: Here's a look at his five ground-breaking scientific achievements....</p></summary>
    <p>1/6. 89th Birth Anniversary. ... <br><br>

    2/6. India's first Satellite Launch Vehicle (SLV). ... <br><br>

    3/6. Ballistic missiles project. ... <br><br>

    4/6. Nuclear tests at Pokhran. ... <br><br>

    5/6. Universal healthcare plan. ... <br><br>

    6/6. 'Kalam-Raju tablet'<br></p>
</details>

</div>
<a id="r1" onclick="career()">Back</a>`;


let a2 = `            <!--Achievements and other

details of the person-->

<h1 class="title-APJ">   Career as a scientist</h1>

<p id="tribute-para">
After graduating from the Madras Institute of Technology in 1960, Kalam joined the Aeronautical
Development Establishment of the Defence Research and Development Organisation (by Press Information
Bureau, Government of India) as a scientist after becoming a member of the Defence Research &
Development Service (DRDS). He started his career by designing a small hovercraft, but remained
unconvinced by his choice of a job at DRDO.Kalam was also part of the INCOSPAR committee working under
Vikram Sarabhai, the renowned space scientist.In 1969, Kalam was transferred to the Indian Space
Research Organisation (ISRO) where he was the project director of India's first Satellite Launch Vehicle
(SLV-III) which successfully deployed the Rohini satellite in near-earth orbit in July 1980; Kalam had
first started work on an expandable rocket project independently at DRDO in 1965.In 1969, Kalam received
the government's approval and expanded the programme to include more engineers.

In 1963 to 1964, he visited NASA's Langley Research Center in Hampton, Virginia; Goddard Space Flight
Center in Greenbelt, Maryland; and Wallops Flight Facility.Between the 1970s and 1990s, Kalam made an
effort to develop the Polar Satellite Launch Vehicle (PSLV) and SLV-III projects, both of which proved
to be successful.

Kalam was invited by Raja Ramanna to witness the country's first nuclear test Smiling Buddha as the
representative of TBRL, even though he had not participated in its development. In the 1970s, Kalam also
directed two projects, Project Devil and Project Valiant, which sought to develop ballistic missiles
from the technology of the successful SLV programme.Despite the disapproval of the Union Cabinet, Prime
Minister Indira Gandhi allotted secret funds for these aerospace projects through her discretionary
powers under Kalam's directorship.Kalam played an integral role convincing the Union Cabinet to conceal
the true nature of these classified aerospace projects.His research and educational leadership brought
him great laurels and prestige in the 1980s, which prompted the government to initiate an advanced
missile programme under his directorship.Kalam and Dr V S Arunachalam, metallurgist and scientific
adviser to the Defence Minister, worked on the suggestion by the then Defence Minister, R. Venkataraman
on a proposal for simultaneous development of a quiver of missiles instead of taking planned missiles
one after another.R Venkatraman was instrumental in getting the cabinet approval for allocating ₹ 3.88
billion for the mission, named Integrated Guided Missile Development Programme (IGMDP) and appointed
Kalam as the chief executive.Kalam played a major part in developing many missiles under the mission
including Agni, an intermediate range ballistic missile and Prithvi, the tactical surface-to-surface
missile, although the projects have been criticised for mismanagement and cost and time overruns.

Kalam served as the Chief Scientific Adviser to the Prime Minister and Secretary of the Defence Research
and Development Organisation from July 1992 to December 1999. The Pokhran-II nuclear tests were
conducted during this period in which he played an intensive political and technological role. Kalam
served as the Chief Project Coordinator, along with Rajagopala Chidambaram, during the testing
phase.Media coverage of Kalam during this period made him the country's best known nuclear scientist.

In 1998, along with cardiologist Soma Raju, Kalam developed a low cost coronary stent, named the
"Kalam-Raju Stent".In 2012, the duo designed a rugged tablet computer for health care in rural areas,
which was named the "Kalam-Raju Tablet".
</p>

<div>
<details>
    <summary>
        <p>Remembering APJ Abdul Kalam: Here's a look at his five ground-breaking scientific
            achievements....</p>
    </summary>
    <p>1/6. 89th Birth Anniversary. ... <br><br>

    2/6. India's first Satellite Launch Vehicle (SLV). ... <br><br>

    3/6. Ballistic missiles project. ... <br><br>

    4/6. Nuclear tests at Pokhran. ... <br><br>

    5/6. Universal healthcare plan. ... <br><br>

    6/6. 'Kalam-Raju tablet'<br></p>
</details>
</div>
<a onclick="early()" id="r1">Back</a>

<a onclick="presidence()" id="r2">    Next...</a>`;


let a1 = `            <!--Achievements and other

details of the person-->

<h1 class="title-APJ">Early life and education</h1>

<p id="tribute-para">
Avul Pakir Jainulabdeen Abdul Kalam was born on 15 October 1931 to a Tamil Muslim family in the
pilgrimage centre of Rameswaram on Pamban Island, then in the Madras Presidency and now in the State of
Tamil Nadu. His father Jainulabdeen was a boat owner and imam of a local mosque; his mother Ashiamma was
a housewife.His father owned a ferry that took Hindu pilgrims back and forth between Rameswaram and the
now uninhabited Dhanushkodi.Kalam was the youngest of four brothers and one sister in his family.His
ancestors had been wealthy traders and landowners, with numerous properties and large tracts of land.
Their business had involved trading groceries between the mainland and the island and to and from Sri
Lanka, as well as ferrying pilgrims between the mainland and Pamban. As a result, the family acquired
the title of "Mara Kalam Iyakkivar" (wooden boat steerers), which over the years became shortened to
"Marakier." With the opening of the Pamban Bridge to the mainland in 1914, however, the businesses
failed and the family fortune and properties were lost over time, apart from the ancestral home.By his
early childhood, Kalam's family had become poor; at an early age, he sold newspapers to supplement his
family's income.

In his school years, Kalam had average grades but was described as a bright and hardworking student who
had a strong desire to learn. He spent hours on his studies, especially mathematics.After completing his
education at the Schwartz Higher Secondary School, Ramanathapuram, Kalam went on to attend Saint
Joseph's College, Tiruchirappalli, then affiliated with the University of Madras, from where he
graduated in physics in 1954.He moved to Madras in 1955 to study aerospace engineering in Madras
Institute of Technology.While Kalam was working on a senior class project, the Dean was dissatisfied
with his lack of progress and threatened to revoke his scholarship unless the project was finished
within the next three days. Kalam met the deadline, impressing the Dean, who later said to him, "I was
putting you under stress and asking you to meet a difficult deadline".He narrowly missed achieving his
dream of becoming a fighter pilot, as he placed ninth in qualifiers, and only eight positions were
available in the IAF.
</p>

<div>
<details>
    <summary>
        <p>Remembering APJ Abdul Kalam: Here's a look at his five ground-breaking scientific
            achievements....</p>
    </summary>
    <p>1/6. 89th Birth Anniversary. ... <br><br>

    2/6. India's first Satellite Launch Vehicle (SLV). ... <br><br>

    3/6. Ballistic missiles project. ... <br><br>

    4/6. Nuclear tests at Pokhran. ... <br><br>

    5/6. Universal healthcare plan. ... <br><br>

    6/6. 'Kalam-Raju tablet'<br></p>

</details>

</div>
<a onclick="index()" id="r1">Back</a>

<a onclick="career()" id="r2">Next...</a>`;


let a = `  <!--Achievements and other

details of the person-->

<h1 class="title-APJ">

About the Legend

</h1>

<p id="tribute-para">A.P.J. Abdul Kalam, in full

Avul Pakir Jainulabdeen Abdul Kalam,

was born on October 15, 1931, in

Rameswaram, Tamil Nadu, India. He served as the 11th President

of India from 2002 to 2007. Kalam earned a degree in

aeronautical engineering from the

Madras Institute of Technology and in

1958 joined the Defence Research and

Development Organisation (DRDO). In 1969, he moved to the Indian

Space Research Organisation, where he

was project director of the SLV-III, the

first satellite launch vehicle that was

both designed and produced in India.
 Rejoining DRDO in 1982,

Kalam planned the program that produced

a number of successful missiles, which

helped earn him the nickname <strong>

    “Missile Man.”</strong>
 Among those successes

was Agni, India’s first intermediate-range

ballistic missile, which incorporated

aspects of the SLV-III and was launched

in 1989.
 He also played a

pivotal organisational, technical,

and political role in India's Pokhran-II

nuclear tests in 1998, the first since

the original nuclear test by India in 1974.
 From 1992 to 1997 Kalam

was scientific adviser to the defense

minister, and he later served as principal

scientific adviser (1999–2001) to the

government with the rank of cabinet minister.
 His prominent role in

the country’s 1998 nuclear weapons tests

solidified India as a nuclear power and

established Kalam as a national hero,

although the tests caused great concern

in the international community.
 In 1998 Kalam put

forward a countrywide plan called

Technology Vision 2020, which he described

as a road map for transforming India from

a less-developed to a developed society

in 20 years. The plan called for, among

other measures, increasing agricultural

productivity, emphasizing technology as

a vehicle for economic growth, and

widening access to health care and

education.
 Kalam received <b>7</b>

honorary doctorates from <b>40</b>

universities. The Government of India

honoured him with the <b>Padma Bhushan

    in 1981</b> and the <b>Padma Vibhushan

    in 1990</b> for his work with ISRO and

DRDO and his role as a scientific advisor

to the Government.
 In 1997, Kalam received

India's highest civilian honour, the

Bharat Ratna, for his contribution to

the scientific research and modernisation

of defence technology in India.
 In 2013, he was the

recipient of the Von Braun Award from

the National Space Society "to recognize

excellence in the management and leadership

of a space-related project".
 While delivering a

lecture at the Indian Institute of

Management Shillong, Kalam collapsed and

died from an apparent cardiac arrest on

<b>27 July 2015</b>, aged 83.
 Wheeler Island, a

national missile test site in Odisha, was

renamed <b>Kalam Island</b> in September

2015.
 A prominent road in

New Delhi was renamed from Aurangzeb

Road to <b>Dr APJ Abdul Kalam Road</b>

in August 2015.
 In February 2018,

scientists from the Botanical Survey

of India named a newly found plant

species as Drypetes kalamii, in his

honour.

<br><br><br>

</p>

<div>

<details>

    <summary>
        <p>Remembering APJ Abdul Kalam: Here's a look at his five ground-breaking scientific
            achievements....</p>
    </summary>

    <p>1/6. 89th Birth Anniversary. ... <br><br>

    2/6. India's first Satellite Launch Vehicle (SLV). ... <br><br>

    3/6. Ballistic missiles project. ... <br><br>

    4/6. Nuclear tests at Pokhran. ... <br><br>

    5/6. Universal healthcare plan. ... <br><br>

    6/6. 'Kalam-Raju tablet'<br></p>
</details>
</div>
<a onclick="early()" id="r2">Next...</a>`;