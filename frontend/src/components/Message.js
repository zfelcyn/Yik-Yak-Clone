import React from "react";
import { Card } from "react-bootstrap";
import {Link } from "react-router-dom";
import { Row, Col } from "react-bootstrap";
import MessageButton from "./MessageButton";





function Message({ message }) {
  return (
    <Card className="my-3 p-3 rounded" >
      <Row>
        <Col xs={2} sm={2} md={1} lg={1} xl={1} style={{ justifyContent: "center" }}>
          <Link to={"/message/${message._id}"}>
            <Card.Img src={message.image} className="rounded-circle" style={{ width: '50px', height: '50px'}}  />
          </Link>
        </Col>
        <Col>
          <Link to={"/message/${message._id}"}>
            <Card.Title as="div" style={{height: '5px'}}>
              <strong>{message.sender}</strong>
            </Card.Title>
            <Card.Text as="div">
              <div className="my-3 small text-muted">@{message.userName}</div>
            </Card.Text>
          </Link>
          <Card.Text as="div">
            <div className="my-3">{message.message} </div>
            
            <div className="my-3 small text-muted" style={{height: "10px"}}>{message.timeSent} | <Link className="my-3 text-muted"to={"/message/${message._id}"}>{message._id}</Link></div>
          </Card.Text>
          <MessageButton>
              <i class="fa-regular fa-comment"></i>
            </MessageButton>
        </Col>
      </Row>
    </Card>
  );
}

export default Message;
