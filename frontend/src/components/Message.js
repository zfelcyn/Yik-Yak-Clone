import React from "react";
import { Card } from "react-bootstrap";
import {Link } from "react-router-dom";

function Message({ message }) {
  return (
    <Card className="my-3 p-3 rounded">
      Message
      <Link to={"/message/${message._id}"}>
        <Card.Img src={message.image} />
      </Link>
      <Card.Body>
        <Link to={"/message/${message._id}"}>
          <Card.Title as="div">
            <strong>{message.sender}</strong>
          </Card.Title>
        </Link>

        <Card.Text as="div">
          <div className="my-3">{message.message} </div>
          <div className="my-3 small text-muted">{message.timeSent}</div>
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Message;
