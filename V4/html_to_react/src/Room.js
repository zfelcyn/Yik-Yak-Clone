import React, { useState, useEffect } from "react";
import axios from "axios";

function Room() {
  const [messages, setMessages] = useState([]);
  const [messageInput, setMessageInput] = useState("");
  const roomName = window.location.pathname.split("/")[1];
  const username = new URLSearchParams(window.location.search).get("username");

  useEffect(() => {
    fetchMessages();
    const interval = setInterval(fetchMessages, 1000);
    return () => clearInterval(interval);
  }, []);

  const fetchMessages = async () => {
    try {
      const response = await axios.get(`/get_messages/${roomName}/`);
      setMessages(response.data.messages);
    } catch (error) {
      console.error("Error fetching messages:", error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/send_message/", {
        username: username,
        room_name: roomName,
        message: messageInput,
      });
      setMessageInput("");
      fetchMessages(); // Refresh messages after sending a new one
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  return (
    <div>
      <h2>{roomName} - DjChat</h2>
      <div id="display">
        {messages.map((msg, index) => (
          <div key={index} className="container darker">
            <b>{msg.user}</b>
            <p>{msg.value}</p>
          </div>
        ))}
      </div>
      <div className="container">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={messageInput}
            onChange={(e) => setMessageInput(e.target.value)}
          />
          <input type="submit" value="Send" />
        </form>
      </div>
    </div>
  );
}

export default Room;
