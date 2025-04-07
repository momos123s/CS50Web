
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
async function update_likes(id, liked, editContent, url) {
    try {
        let response = await fetch(url, {
            method: "PUT",
            headers: { "Content-Type": "application/json" }, 
            body: JSON.stringify({ id: id, editContent: editContent })
        });

        let data = await response.json();
        console.log(data); 
        return data; 
    } catch (error) {
        console.error("Failed to update likes:", error);
    }
}

function update_follows(followid) {
    
    
    //send to the server
    let response =  fetch("/followOrUnfollow",
    {
        method:"PUT",
        body : JSON.stringify({
            followid:followid,
            'Content-type':'application/json'
        })
    })
    
   .then(response => response.json())
   .then( result => {alert(result.status)})

}


    


//updates
function new_post (description)
{

try{
    fetch(
    '/new',{
        method:"POST",
        headers: {
            "Content-Type":"Application/Json",
            "X-CSRFTOKEN":cookies
        },
        body: JSON.stringify({
            content:description,

        })
    }
    )
        alert("your post was successful");
        
}
catch(error){
    return alert("something went wrong whilst trying to upload")
}
   
}
window.new_post = new_post;
window.update_follows = update_follows;
window.get_api = get_api;
window.update_likes = update_likes;