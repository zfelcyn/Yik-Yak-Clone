import React, { useState, useEffect } from "react";
import axios from "axios";
import Room from "./Room"; // Import your Room component

function App() {
  const [location, setLocation] = useState("");
  const [username, setUsername] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    fetchLocation();
  }, []);

  const fetchLocation = async () => {
    try {
      const response = await axios.get("https://ipapi.co/json/");
      setLocation(response.data.city);
    } catch (error) {
      console.error("Error fetching location:", error);
    }
  };

  const joinRoom = (roomName, user) => {
    setUsername(user);
    setLoggedIn(true);
  };

  return (
    <div className="App">
      {!loggedIn ? (
        <div className="container">
          <h2 style={{ textAlign: "left" }}>Login</h2>
          <form
            id="post-form"
            method="POST"
            action="checkview"
            onSubmit={(e) => {
              e.preventDefault();
              const roomName = location; // Use location as roomName
              const username = e.target.username.value;
              joinRoom(roomName, username);
            }}
          >
            <label htmlFor="location">Location</label>
            <input
              type="text"
              name="location"
              id="location"
              value={location}
              readOnly
            />
            <label htmlFor="username">Username</label>
            <input type="text" name="username" id="username" />
            <input type="submit" value="Login" className="login-btn" />
          </form>
        </div>
      ) : (
        <Room roomName={location} username={username} />
      )}
    </div>
  );
}

export default App;
