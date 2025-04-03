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
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{post.heading}</h5>
                <p className="card-text text-start">{post.user}</p>
                <p className="card-text">{post.description}</p>
                <div className="likeboxArea">
                  <LikeButton postID={post.id} amountofLikes={post.likes} />
                  <p className="card-text small">{post.timestamp}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
  
        {/* Pagination */}
        <div className="pagination">
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
  
