import React from 'react';

const CommentForm = ({ addComment }) => {
 const handleSubmit = (e) => {
    e.preventDefault();
    const inputText = e.target.elements.text.value;
    addComment(inputText);
    e.target.elements.text.value = '';
 };

 return (
    <form onSubmit={handleSubmit} className="flex flex-col justify-between">
      <textarea
        name="text"
        placeholder="Enter your comment"
        className="block my-2 p-2"
      ></textarea>
      <button type="submit" className="bg-blue-500 text-white px-2 py-1">
        Add Comment
      </button>
    </form>
 );
};

export default CommentForm;