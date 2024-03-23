import React from "react";
import { Row, Col } from "react-bootstrap";

import Message from "../components/Message";
import messages from "../messages";

function HomeScreen() {
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
