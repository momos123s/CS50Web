function ShowProfile()
{
    
    const [profile, setProfile] = React.useState([]);
    React.useEffect(() => {
        get_api("load_profiles").then(data =>  setProfile(data));
    },[]);
    let post = profile.users_posts || [];
    console.log(profile);
  

    return(
        <div id ="showProfile">
            <h1 id="accInfo"> Account Information </h1>
            <div id="top-info"class="row" >
    
                <div class = "col-6">
                </div>
                <div class="col" id="profile-col">
                    <h1>User: {profile.username}</h1>
                    <h3>Email: {profile.email}</h3>
                    <h3>Followers:{profile.followers_count}</h3>

                </div>
         
            </div>
            <div class = "row" > 

            </div>
            <div class ="row" >
            
            <div className="main-content">  
                <h2>My Posts:</h2> 
          {post && post.map((item, index) => (
              <div className="individual-post" key={item.postid}>
                  {console.log(item)}
                  <div className="card " id="post-card">          
                      <div className="card-body">
                          <p className="card-text text-start" id = "username">{profile.username}</p>
                          <p className="card-text" id = "description">{item.description}</p>
                          <div className="likeboxArea">
                          <LikeButton PostID={item.id} amountofLikes={item.likes} />
                              <p className="card-text small" id="timestamp" >{item.timestamp}</p>
                          </div>
                      </div>
                  </div>
              </div>     
          ))}
  
      </div>






            </div>
        </div>
    );
}
ReactDOM.render(< ShowProfile/>, document.querySelector("#profile_view"));
