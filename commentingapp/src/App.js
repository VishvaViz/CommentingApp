import React from "react";
import Comment from "./comp/Comment";
import CommentForm from "./comp/CommentForm";

const App = () => {
  const [comments, setComments] = React.useState([
    { user: "John", text: "Nice blog" },
    { user: "Sarah", text: "Learned something" },
  ]);

  const addComment = (text) => {
    const newComment = { user: "Current User", text };
    setComments([...comments, newComment]);
  };

  return (
    <div className="flex justify-center mt-10 ">

      <div className="w-[600px]">
        <h1 className="flex justify-center text-xl font-sans font-bold">Commmenting App</h1>
        {comments.map((comment, index) => (
          <Comment key={index} comment={comment} />
        ))}
        <CommentForm addComment={addComment} />
      </div>
    </div>
  );
};

export default App;
