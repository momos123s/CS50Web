//gets the followers and displays them
function Followers(){

    const [posts, setPosts] = React.useState([]);

    React.useEffect(() => {
        get_api(`/follow`,"error loading post").then(data => setPosts(data));
    }, []);
          //updates and increments the likes when likes is pressed
  
    posts.posts && posts.posts.map((posts,index) => ( console.log(posts.fields)));
    
    return (
      <div className="main-content">   
          {posts.posts && posts.posts.map((post, index) => (
              <div className="individual-post" key={post.fields.postid}>
                  {console.log(post.fields.id)}
                  <div className="top-section">
                  <div className="heading">
                      <h3 className="header">{post.fields.heading}</h3>
                  </div>
  
                  <div className="follow-section">
                      <a onClick={() => update_follows(post.fields.userID)}>follow</a>
                  </div>
                  </div>
  
                  <div className="mid-section">
                      <div className="media">how to make the like 
                              {post.fields.mediaUpload && mediaDector(post.fields.mediaUpload)}
                      </div>
  
                      <div className="description">
                          <p>{post.fields.description}</p> <a href="/edit">edit button</a>
                      </div>
                  </div>
  
                  <div className="bottom-section">           
                      <div className="likeboxArea">
                          <button className="like_button" onClick={() => handlelikeButton(posts.pk,true,heart,posts.p) }>
                              {handlelikeButton(posts.pk,false,)}
                          </button>
                      </div>
                      <div className="timestamp">
                          <p>{post.fields.timestamp}</p>
                      </div>
                  </div>
  
  
              </div>       
          ))}
  
      </div>
    );
  }



ReactDOM.render( < Followers/>, document.querySelector("#following"));