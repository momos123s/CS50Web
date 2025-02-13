function ShowPost() {
    const [posts, setPosts] = React.useState([]);
  
    React.useEffect(() => {
        get_api(`/follow_posts/${"1"}`,"error loading posts").then(data => setPosts(data));
    }, []);
          //updates and increments the likes when likes is pressed
  
    posts.posts && posts.posts.map((posts,index) => ( console.log(posts.fields)));
    
    return (
      <div className="main-content">   
          {posts.posts && posts.posts.map((post, index) => (
              <div className="individual-post" key={post.postid}>
                  {console.log(post)}
                  <div className="card">
                   
                      <div className="card-body">
                          <h5 className="card-title">{post.heading}</h5>
                          <p className="card-text text-start">{post.user}</p>
                          <p className="card-text">{post.description}</p>
                          <div className="likeboxArea">
                              <p className="like_button" onClick={() => handlelikeButton(post.id,true,"❤️",post.like_count) }>
                                     {`🤍 ${post.likes}`}
                              </p>
                              <p className="card-text small">{post.timestamp}</p>
                          </div>
                      </div>
                  </div>
              </div>       
          ))}
  
      </div>
    );
  }
  ReactDOM.render( <ShowPost/>, document.querySelector('#followingPost'));
  
  
