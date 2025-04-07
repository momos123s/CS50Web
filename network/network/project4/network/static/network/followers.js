
function FollowersPosts() {

    const [posts, setPosts] = React.useState([]);
  
    React.useEffect(() => {
        get_api("/follow_posts/1","error loading posts").then(data => setPosts(data));
    }, []);
          //updates and increments the likes when likes is pressed
  
    posts.posts && posts.posts.map((posts,index) => ( console.log(posts.fields)));
    
    return (
      <div className="main-content">   
          {posts.posts && posts.posts.map((post, index) => (
              <div className="individual-post" key={post.postid}>
                  {console.log(post)}
                  <div className="card " id="post-card">          
                      <div className="card-body">
                      <p className="card-text text-start" id="username" onClick={() => FollowClick({username:post.user})}>{post.user}</p>
                          <p className="card-text" id = "description">{post.description}</p>
                          <div className="likeboxArea">
                          <LikeButton PostID={post.id} amountofLikes={post.likes} />
                              <p className="card-text small" id="timestamp" >{post.timestamp}</p>
                          </div>
                      </div>
                  </div>
              </div>       
          ))}
  
      </div>
    );
  }
  ReactDOM.render(<FollowersPosts/>, document.querySelector("#followingPost"));