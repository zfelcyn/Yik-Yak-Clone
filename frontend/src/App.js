import { Routes, Route, HashRouter as Router } from "react-router-dom";
import { Container } from "react-bootstrap";
import React, { Component } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from "./Screens/HomeScreen";
import MessageScreen from "./Screens/MessageScreen";

class App extends Component {
  render() {
    return (
      <Router>
        <Header />
        <main className="py-3">
          <Container>
            <Routes>
              <Route path="/" element={<HomeScreen />} exact />
              <Route path="/message/:id" element={<MessageScreen />} />
            </Routes>
          </Container>
        </main>
        <Footer />
      </Router>
    );
  }
}

export default App;
