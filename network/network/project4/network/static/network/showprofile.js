function ShowProfile()
{
    
    const [profile, setProfile] = React.useState([]);
    React.useEffect(() => {
        get_api("/load_profiles").then(data => setProfile(data));
    },[]);
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
     
            </div>


        </div>
    );
}
ReactDOM.render(< ShowProfile/>, document.querySelector("#profile_view"));
