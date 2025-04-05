function LikeButton({ PostID, amountofLikes }) {
    const [amount, setAmount] = React.useState(amountofLikes);
    const [likes, setLike] = React.useState();

//
   async function Clicklike(){
    try{
        //call and wait for response from server
        const update = await update_likes(PostID,null,null,"/update_likes")
        //stores server data 
        setLike(update)
        console.log(update)
        return likes;
    }
    catch(error){
        console.error("issues handling the click of like button")
        return null;
    }
    
}
//check if resposse has data and updae values
React.useEffect(() => {
    if (likes !== null) {
        console.log("Updated likes from server:", likes);
    }
}, [likes]);

    
    return (
        <div>
            <p onClick={ () => 
                {setAmount(prev => prev + 1);
                Clicklike().then(updatedLikes => console.log("Updated like data:", updatedLikes));

                 }}> ❤️{amount} </p>
        </div>
    );
}




function ShowPost() {
    const [posts, setPosts] = React.useState([]);
    const [currentPage, setCurrentPage] = React.useState(1);
  
    // Function to fetch posts from the Django API
    const fetchPosts = (page) => {
      get_api(`/get_posts/${page}`, "error loading posts").then(data => setPosts(data));
    };
  
    React.useEffect(() => {
      fetchPosts(currentPage);
    }, [currentPage]);  // Fetch posts whenever currentPage changes
  
    return (
      <div className="main-content">
        {posts.posts && posts.posts.map(post => (
          <div className="individual-post" key={post.id}>
            <div className="card" id="post-card">
              <div className="card-body">
                <h5 className="card-title">{post.heading}</h5>
                <p className="card-text text-start" id="username">{post.user}</p>
                <p className="card-text" id="description">{post.description}</p>
                <div className="likeboxArea">
                  <LikeButton PostID={post.id} amountofLikes={post.likes} />
                  <p className="card-text small" id="timestamp">{post.timestamp}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
  
        {/* Pagination */}
        <div className="pagination justify-content-center " >
          <nav aria-label="Page navigation">
            <ul className="pagination justify-content-center">
              {/* Previous Button */}
              <li className={`page-item ${posts.page === 1 ? "disabled" : ""}`}>
                <button className="page-link" onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}>
                  Previous
                </button>
              </li>
  
              {/* Page Numbers */}
              {Array.from({ length: posts.total_pages }, (_, i) => (
                <li key={i} className={`page-item ${posts.page === i + 1 ? "active" : ""}`}>
                  <button className="page-link" onClick={() => setCurrentPage(i + 1)}>
                    {i + 1}
                  </button>
                </li>
              ))}
  
              {/* Next Button */}
              <li className={`page-item ${posts.page === posts.total_pages ? "disabled" : ""}`}>
                <button className="page-link" onClick={() => setCurrentPage(prev => Math.min(prev + 1, posts.total_pages))}>
                  Next
                </button>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    );
  }
  
  ReactDOM.render(<ShowPost />, document.querySelector("#viewPosts"));
  




