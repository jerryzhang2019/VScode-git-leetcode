/* Global Variables */
let baseURL = 'https://api.openweathermap.org/data/2.5/weather?'
let apiKey = '67f1f036f1d0204f97f507300d65c902';

// Create a new date instance dynamically with JS
let d = new Date();
let newDate = d.getMonth()+'.'+ d.getDate()+'.'+ d.getFullYear();

/* Function called by event listener */
document.getElementById('generate').addEventListener('click', performAction);

function performAction(e){
    const newzip = document.getElementById('zip').value;

    getzip('/addWeatherData')
    .then(function(data){
        console.log(data)
        postData('/addWeatherData',{weather:data.zipcode, weather:data.countryCode,weather:data.apiKey })
    })
    .then(
        updateUI()
    )
    // getzip(baseURL,newzip,apiKey)
}
const updateUI = async() =>{
    const request = await fetch('/all');
    try{
        const allData = await request.json();
        document.getElementById('zip').innerHTML = allData[0].zip;
        document.getElementById('feeling').innerHTML = allData[0].feeling;

    }catch(error){
        console.log("error", error);
    }
}

const getzip = async (baseURL, zip,key)=>{
    const res = await fetch(baseURL+zip+key)
    try{
        const data = await res.json();
        console.log(data)
        return data;
    }catch (error){
        console.log("error",error);
    }
}

// import { response } from "express";
// import { allowedNodeEnvironmentFlags } from "process";



// Personal API Key for OpenWeatherMap API
/* Function to POST data */
const postData = async (url = '', data={}) => {
    const respone = await fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'content-type':'application/jsion',
        },
        body:JSON.stringify(data),
    });

    try{
        const newData = await response.json();
        return newData
    }catch(error){
        console.log("error", error);
    }
}
// postData('/addInformation',{temp:'temperature'});
// postData('/addInformation',{date:'date'});
// postData('/addInformation',{input:'user input'});
const retrieveData = async(url='') =>{
    const request = await fetch(url);
    try{
        const newData = await request.json();
    }
    catch(error){
        console.log("error", error)
    }
}
/* Function to GET Project Data */
function postGet(){
    postData('/information',{temp:'temperature'},{date:'date'},{input:'user input'})
    .then(function(data){
        retrieveData('/all')
    })
}
postGet()
// Event listener to add function to existing HTML DOM element








