import React, { useState, useEffect } from "react";
import { Row } from "react-bootstrap";
import Message from "../components/Message";
import axios from "axios";

function HomeScreen() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    async function fetchMessages() {
      try {
        const response = await axios.get("http://localhost:3000/api/messages/");
        setMessages(response.data);
      } catch (error) {
        console.error("Error fetching messages:", error);
      }
    }
    fetchMessages();
  }, []);

  return (
    <div>
      {messages.map((message) => (
        <Row key={message._id} xs={1} sm={1} md={1} lg={1} xl={1}>
          <Message message={message} />
        </Row>
      ))}
    </div>
  );
}

export default HomeScreen;
