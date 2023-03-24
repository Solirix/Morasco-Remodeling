const firebaseConfig = {

    apiKey: "AIzaSyCyr_FLgMWP-EtOamoM8wWWV76udhCTCBk",

    authDomain: "customer-info-relay-dc5d8.firebaseapp.com",

    databaseURL: "https://customer-info-relay-dc5d8-default-rtdb.firebaseio.com",

    projectId: "customer-info-relay-dc5d8",

    storageBucket: "customer-info-relay-dc5d8.appspot.com",

    messagingSenderId: "858151144597",

    appId: "1:858151144597:web:ed74faf70f0b1387159f9c"

  };
//init firebase
firebase.initializeApp(firebaseConfig);

//reference the database. Given name contactForm
var contactFormDB = firebase.database().ref('contactForm')

//calls submitForm function when submit button is clicked
document.getElementById('contactForm').addEventListener('submit', submitForm);

function submitForm(e){
    e.preventDefault(); // prevent default action of form

    //get values
    var name = getElementVal('name');
    var email = getElementVal('email');
    var phone = getElementVal('number');
    var message = getElementVal('message');

    saveMessage(name, email, phone, message);

    //alert the user what happened
    document.querySelector('.alert').style.display = "block";

    //remove alert after 3 seconds
    setTimeout(() => {
        document.querySelector(".alert").style.display = "none";
    }, 8000);

    //emptying out the form
    document.getElementById("contactForm").reset();
}

//helper function to get form values
const getElementVal = (id) => {
    return document.getElementById(id).value;
}

const saveMessage = (name, email, phone, message) => {
    var newContactForm = contactFormDB.push();
    newContactForm.set({
        name: name,
        email: email,
        phone: phone,
        message: message
    });
}
