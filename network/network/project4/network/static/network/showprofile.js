function ShowProfile()
{
    const [profile, setProfile] = React.useState([]);
    React.useEffect(() => {
        get_api("/load_profiles").then(data => setProfile(data));
    },[]);
    console.log(profile);
    
    return(
        <div>
            <p>name: {profile.username}</p>
            <p>email: {profile.email}</p>
            {
            // profle picture goes here
            }
            <p>followers:</p>
            <p>following</p>
        </div>
    );
}
ReactDOM.render(< ShowProfile/>, document.querySelector("#profile_view"));
