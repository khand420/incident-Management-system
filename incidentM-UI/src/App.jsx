// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';

function App() {
  const [justifyActive, setJustifyActive] = useState('tab1');

  const handleJustifyClick = (value) => {
    if (value === justifyActive) {
      return;
    }
    setJustifyActive(value);
  };

  return (
    <Router>
      <div className="container text-center mt-1">
        <ul className="nav nav-tabs justify-content-center">
          <li className="nav-item">
            <Link 
              className={`nav-link ${justifyActive === 'tab1' ? 'active' : ''}`} 
              onClick={() => handleJustifyClick('tab1')}
              to="/login"
            >
              Login
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              className={`nav-link ${justifyActive === 'tab2' ? 'active' : ''}`} 
              onClick={() => handleJustifyClick('tab2')}
              to="/register"
            >
              Register
            </Link>
          </li>
        </ul>

        <h1 className="mt-1">Incident Management System</h1>
        <div className="container mt-1 p-3">
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
