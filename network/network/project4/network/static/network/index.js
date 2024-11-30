

function PostForm()
{
    
    const [heading, setHeading] = React.useState("");
    const [file, setFile] = React.useState("");
    const [description, setDescription] = React.useState("");
    const [tags, setTags]= React.useState("");
    return(
        <div className="post-form">
            <form >
                <div className="main-post-div">
                    <div className="mb-3">
                        <label className="post-label" >heading:</label>
                        <input type="text" class=" post-text form-control" id="" placeholder="heading"value={heading} onChange={e => setHeading(e.target.value)} ></input>
                    </div>

                    <div className="mb-3">
                        <label className="post-label">media:</label>
                        <input type="file" className=" post-text form-control" placeholder="media" value ={file} onChange={f => setFile(f.target.value)}></input>
                    </div>
                    <div className = "mb-3"> 
                        <label className="post-label">descritption:</label>
                        <input type="text" className="description form-control" value={description} onChange={d => setDescription(d.target.value)}></input>
                    </div>
                    <div className = "mb-3">
                        <label className="post-label">tags:</label>
                        <input type="text" className="tags form-control" value={tags} onChange={t => setTags(t.target.value)}></input>
                    </div>
                    <button type="button" id="sub-Button"className="btn btn-warning" onClick={s => new_post(heading,description,file,tags)}>create post</button>
                </div>
            </form>
        </div>
);
}

function NewPostForm()
{
    const [showform, setShowForm] = React.useState(false);

    const handleClick = () =>
    {

         setShowForm(!showform);
         
    }
    
    return (
    <div>
        <button className="btn btn-light" onClick = {handleClick}>new post</button>
   
        {showform && <PostForm/>}
    </div>
    );
        

}

ReactDOM.render(< NewPostForm/>,document.querySelector("#newPostD"));



const cookies = window.csrfToken;

//post request for form 
