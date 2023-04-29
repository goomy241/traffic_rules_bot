import React, { useState, useRef } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [conversation, setConversation] = useState([]);
  const questionRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const currentQuestion = questionRef.current.value.trim();

    fetch('http://127.0.0.1:5000/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: currentQuestion })
    })
    .then(response => response.json())
    .then(data => {
      setResponse(data.response);
      setConversation(prevConversation => [...prevConversation, { speaker: "user", message: currentQuestion }, { speaker: "bot", message: data.response }]);
      setQuestion("");
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  const handleClearConversation = () => {
    setConversation([]);
  }

  return (
    <div className="chat-container">
      <div className="chat-header">
        <div className="chat-title">California DMV Q&amp;A</div>
      </div>
      <div className="chat-window">
        <div className="chat-messages">
          {conversation.map((item, index) => (
            <div key={index} className={`message ${item.speaker}`}>
              <div className="avatar">{item.speaker === "user" ? "You" : "Bot"}</div>
              <div className="text">{item.message}</div>
            </div>
          ))}
        </div>
        <form className="chat-form" onSubmit={handleSubmit}>
          <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} ref={questionRef} placeholder="Ask a question" />
          <button type="submit">Ask</button>
        </form>
        {conversation.length > 0 && (
          <button className="clear-button" onClick={handleClearConversation}>Clear conversation</button>
        )}
      </div>
    </div>
  );
}

export default App;
