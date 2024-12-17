      
      function handlelikeButton(postID,buttonClicked, heart,likes){
        
        if(buttonClicked == null){
            return(
                <div>
                      "🤍 "+ {likes};
                </div>
            )
              
        }
        else if(buttonClicked && heart == "❤️" ){
            update_likes(postID,null,"","/update_likes");           
            return(
                <div>
                      "❤️ "+ {likes+1};
                </div>)
        }
        else if(buttonClicked && heart == "🤍"){
            update_likes(postID,null,"","/update_likes");
            return(
                <div>
                      "🤍"+ {likes-1};
                </div>
            )
        }
        else{
            return "something went wrong";
        }
      }



//display posts
function ShowPost() {
  const [posts, setPosts] = React.useState([]);

  React.useEffect(() => {
      get_api(`/get_posts/${"1"}`,"error loading posts").then(data => setPosts(data));
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
ReactDOM.render( <ShowPost/>, document.querySelector('#viewPosts'));




console.log(typeof null);
//check if file type is a video or image
function mediaDector(fileUrl)
{
    let media = fileUrl 
    media = media.split('.').pop().toLowerCase();

  if (["jpg", "jpeg", "png", "gif"].includes(media)) {
      // It's an image
      console.log("this is an image");
      return(
        <img src={fileUrl} alt="Description" width="600" />
      )

  } else if (["mp4", "avi", "mov"].includes(media)) {
      // It's a video
      console.log("its a video");
      return(
      <video width="600" controls>
      <source src={fileUrl} type="video/mp4" />
      Your browser does not support the video tag.
       </video>
      )
  } else{
      return console.log("no file dectected");
  }
    }





