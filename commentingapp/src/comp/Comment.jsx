import React from 'react';

const Comment = ({ comment }) => {
 return (
    <div className="bg-gray-200 p-4 my-2">
      <p>{comment.text}</p>
      <div className="text-sm text-gray-600">{comment.user}</div>
    </div>
 );
};

export default Comment;