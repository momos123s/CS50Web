


function PostForm()
{

    const [file, setFile] = React.useState("");
    const [description, setDescription] = React.useState("");

    return(
        <div className="post-form">
            <form >
                <div className="main-post-div">

                    <div className="mb-3">
                        <label className="post-label">media:</label>
                        <input type="file" className=" post-text form-control" placeholder="media" value ={file} onChange={f => setFile(f.target.value)}></input>
                    </div>
                    <div className = "mb-3"> 
                        <label className="post-label">descritption:</label>
                        <textarea class=" description form-control" id="" rows="3" value={description} onChange={d=>setDescription(d.target.value)}></textarea>
                    </div>
         
                    <button type="button" id="sub-Button"className="btn btn-warning" onClick={s => new_post(description,file)}>create post</button>
                </div>
            </form>
        </div>
);
}


ReactDOM.render(< PostForm/>,document.querySelector("#newPostD"));



const cookies = window.csrfToken;

//post request for form 
