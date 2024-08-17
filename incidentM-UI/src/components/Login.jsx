// src/components/Login.js
import React, { useState } from 'react';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        // Add your login logic here
        alert(`Email: ${email}\nPassword: ${password}`);
    };

    return (
        <div className="login-container">
            <h3>USER LOGIN</h3>
            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    className="form-control mb-2"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                <input
                    type="password"
                    className="form-control mb-2"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <a href="/forgot-password" className="forgot-password">Forgot password?</a>
                <button type="submit" className="btn btn-primary">LOG ME IN</button>
            </form>
        </div>
    );
}

export default Login;
