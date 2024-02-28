import { Container } from "react-bootstrap";

import React, { Component } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";

import HomeScreen from "./Screens/HomeScreen";

class App extends Component {
  render() {
    return (
      <div>
        <Header />
        <main>
          <Container>
            <h1> I love Haskell</h1>
          </Container>
        </main>

        <Footer />
      </div>
    );
  }
}

export default App;
