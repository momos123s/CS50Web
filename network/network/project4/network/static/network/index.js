function alertPost()
{
    return(<div class="alert alert-light" role="alert">
        A simple light alert—check it out!
      </div>)
}


function PostForm(isedit, desc,postID, userID)
{
    const [description, setDescription] = React.useState("");
    if(isedit === true){
        setDescription(desc)
    }   

    return(
        <div className="post-form">
            <form enctype="multipart/form-data" method="post">
                <div className="main-post-div">
                    <div className = "mb-3"> 
                        <label className="post-label">descritption:</label>
                       
                        <textarea class=" description form-control" id="" rows="3" value={description} onChange={d=>setDescription(d.target.value)}></textarea>
                    </div>
            
                    <button type="button" id="sub-Button"className="btn btn-warning" onClick={isedit ? s=> update_likes(postID,null,description,"/update_descr") : s => new_post(description)}>create post</button>
                </div>
            </form>
        </div>
);
}


ReactDOM.render(< PostForm/>,document.querySelector("#newPostD"));



const cookies = window.csrfToken;

//post request for form 
