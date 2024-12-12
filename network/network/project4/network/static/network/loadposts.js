      
      function handlelikeButton(postID,buttonClicked, heart,likes){
        
        if(buttonClicked == null){
            return "❤️"+likes;
        }
        else if(buttonClicked && heart == "❤️" ){
            response = update_likes(postID,true,null,"/update_likes");
            console.log(response)
            return "❤️"+likes+1;
        }
        else if(buttonClicked && heart == "🤍"){
            response = update_likes(postID,false,null,"/update_likes");
            console.log(response)
            return"🤍" + likes-1;
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
            <div className="individual-post" key={post.fields.postid}>
                {console.log(post.fields.id)}
                <div class="card">
                 
                    <div class="card-body">
                        <h5 class="card-title">{post.fields.heading}</h5>
                        <p class="card-text">{post.fields.description}</p>
                        <p>{post.fields.timestamp}</p>
                        <div className="likeboxArea">
                            <button className="like_button" onClick={() => handlelikeButton(posts.pk,true,heart,posts.p) }>
                                {handlelikeButton(posts.pk,null)}
                            </button>
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





