
//gets either user information, follows or even posts
async function get_api(link, errorMessage,) {
    try {
        const response = await fetch(link)
        const information = await response.json();

        if (!response.ok) {
            throw new Error(errorMessage);
        } 
        
        return information;
    } catch (error) {
        console.error(error);
        return [];
    }
}

//updates likes, description 
function update_likes(id, liked,editContent,url) {
    //get checkbox and weather its liked or not
    let istrue = liked;
    console.log(istrue);
    //send to the server
    let response =  fetch(url,
    {
        method:"PUT",
        body : JSON.stringify({
            id:id,
            editContent:editContent,
            'Content-type':'application/json'
        })
    })
    .then(response => response.json())
    .then(result => console.log(result))
}
function update_follows(followid) {
    //get checkbox and weather its liked or not
    
    //send to the server
    let response =  fetch("/follow",
    {
        method:"PUT",
        body : JSON.stringify({
            followid:followid,
            'Content-type':'application/json'
        })
    })
    
   .then(response => response.json())
   .then( result => {console.log(result)})
}


    


//updates
function new_post (description,media)
{

    
    fetch(
    '/new',{
        method:"POST",
        headers: {
            "Content-Type":"Application/Json",
            "X-CSRFTOKEN":cookies
        },
        body: JSON.stringify({
            file:media,
            content:description,

        })
    }
    )
    .then(Response => Response.json())
    .then(result => {
        console.log(result)
    })
    console.log("successful post js");
}
window.new_post = new_post;
window.get_api = get_api;
window.update_likes = update_likes;