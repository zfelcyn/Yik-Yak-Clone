import React, { useState } from 'react';
import { Button } from 'react-bootstrap';

const MessageButton = () => {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <Button
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      variant="light"
      size="xs"
      style={{
        display: "flex", 
        justifyContent: "right",
        alignItems: "center", 
        height: "10px", 
        width: "15px", 
        backgroundColor: "transparent"
      }}
    >
      <i class={isHovered ? "fa-solid fa-comment fa-2x" : "fa-regular fa-comment fa-2x"}></i>
    </Button>
  );
};

export default MessageButton;
