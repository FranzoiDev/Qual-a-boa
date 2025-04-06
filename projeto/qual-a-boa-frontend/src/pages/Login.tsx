import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
//import { login } from '../services/api.mock';

const Login = () => {
  const [email, setEmail] = useState("admin@admin.com");
  const [password, setPassword] = useState("123456");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await api.post("/auth/login", { email, password });
      localStorage.setItem("jwt_token", response.data.access_token);
      navigate("/dashboard");
    } catch (err) {
      setError("E-mail ou senha inválidos");
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="E-mail"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Entrar</button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default Login;