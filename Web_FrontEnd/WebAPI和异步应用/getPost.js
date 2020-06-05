// TODO
const postData = async (url = '', data={}) =>{
    const response = await fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        header:{
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
const retrieveData = async(url = '') =>{
    const request = await fetch(url);
    try{
        const allData = await request.json()
    }
    catch(error){
        console.log("error", error)
    }
}

function postGet(){
    postData('/animal', {fav: 'lion'})
    .then(function(data){
        retrieveData('/all')
    })
}
postGet()