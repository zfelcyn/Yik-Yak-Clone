import React from "react";
import { Row, Col } from "react-bootstrap";

import Message from "../components/Message";
import messages from "../messages";

function HomeScreen() {
  return (
    <div>
      <h1>Hot Singles in Your Area</h1>

      <Row>
        {messages.map((message) => (
          <Col key={message._id} sm={12} md={6} lg={4} xl={3}>
            <Message message={message} />
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default HomeScreen;
