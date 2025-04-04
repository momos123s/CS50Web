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
                <div class="col">
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
                  <div className="card">
                   
                      <div className="card-body">
                          <h5 className="card-title">{item.heading}</h5>
                          <p className="card-text text-start">{item.user}</p>
                          <p className="card-text">{item.description}</p>
                          <div className="likeboxArea">
                       
                              <p className="card-text small">{item.timestamp}</p>
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
