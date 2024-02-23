import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage/HomePage";
import Background from "./components/Background/Background";
import "bootstrap/dist/css/bootstrap.min.css";


function App() {
  return (
    <Background>
      <BrowserRouter>
        <Routes>
          <Route path="" element={<HomePage />} />
        </Routes>
      </BrowserRouter>
    </Background>
  );
}

export default App;
