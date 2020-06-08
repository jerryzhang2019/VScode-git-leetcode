/* Global Variables */
/* Function to GET Web API Data*/
let baseURL = 'https://openweathermap.org/data/2.5/weather?zip='
let apiKey = '';
/* Function called by event listener */
document.getElementById('generate').addEventListener('click', performAction);

function performAction(e){
    const newzip = document.getElementById('zip').value;
    getzip(baseURL,newzip,apiKey)
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

import { response } from "express";

// Create a new date instance dynamically with JS
let d = new Date();
let newDate = d.getMonth()+'.'+ d.getDate()+'.'+ d.getFullYear();

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
postData('/addInformation',{temp:'temperature'});
postData('/addInformation',{date:'date'});
postData('/addInformation',{input:'user input'});
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








