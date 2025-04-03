function LikeButton(PostID,amountofLikes ){

    const [amount, setAmount] = React.useState([amountofLikes])

    return(
        <div>
            <p onlick={ () => setAmount(amount+1) }>❤️ </p>
        </div>
    );

}



//display posts
function ShowPost(link) {
  const [posts, setPosts] = React.useState([]);

    let pagelink = "" ? link : "get_posts/1";
    console.log(pagelink)
  React.useEffect(() => {
      get_api(pagelink,"error loading posts").then(data => setPosts(data));
  }, []);
        //updates and increments the likes when likes is pressed


  
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
                          <LikeButton postID={post.postID}></LikeButton>
                            <p className="card-text small">{post.timestamp}</p>
                        </div>
                    </div>
                </div>
            </div>       
        ))}
        <div className = "pagination">
            {console.log(posts)}
            <nav aria-label="Page navigation example">
                <ul class="pagination justify-content-center">
                    <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                    </li>
                    { Array.from({length: posts.total_pages} ,(_,i) => {
                        return(
                           <li class="page-item" key={i}>
                           <a class="page-link" href="">{i + 1}</a>
                       </li>)})}

                    <li class="page-item">
                    <a class="page-link" href="">Next</a>
                    </li>
                </ul>
            </nav>
        </div>

    </div>
  );
}

ReactDOM.render(<ShowPost/>, document.querySelector("#viewPosts"));







