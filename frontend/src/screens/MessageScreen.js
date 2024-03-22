import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { Container, Row, Col, Image, Button } from "react-bootstrap";
import messages from "../messages"; // Assuming messages.js is in the same directory

const MessageScreen = () => {
  const { messageId } = useParams(); // Assuming the URL parameter is messageId
  const [selectedMessage, setSelectedMessage] = useState(null);

  // Find the selected message by ID
  const message = messages.find((msg) => msg._id === messageId);

  // Function to handle profile display
  const showProfile = () => {
    setSelectedMessage(message);
  };

  return (
    <Container>
      <h1>Message Details</h1>
      {message && (
        <Row>
          <Col md={6}>
            <Image src={message.image} alt={message.sender} fluid />
            <Button onClick={showProfile} className="mt-3" variant="primary">
              Show Profile
            </Button>
          </Col>
          <Col md={6}>
            <h3>{message.sender}</h3>
            <p>Message: {message.message}</p>
            <p>Time Sent: {message.timeSent}</p>
            {selectedMessage && (
              <div>
                <h4>Contact Information</h4>
                <p>Device Name: {selectedMessage.deviceName}</p>
              </div>
            )}
          </Col>
        </Row>
      )}
    </Container>
  );
};

export default MessageScreen;
