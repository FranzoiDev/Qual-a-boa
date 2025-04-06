import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

// Simula a resposta de login
const login = async (email: string, senha: string) => {
  return new Promise<{ token: string }>((resolve, reject) => {
    setTimeout(() => {
      if (email === "teste@admin.com" && senha === "123456") {
        resolve({ token: "mocked-jwt-token" });
      } else {
        reject(new Error("Credenciais inválidas"));
      }
    }, 500);
  });
};

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErro("");

    try {
      const response = await login(email, senha);
      localStorage.setItem("jwt_token", response.token);
      navigate("/dashboard");
    } catch (err) {
      setErro("E-mail ou senha inválidos.");
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
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
          value={senha}
          onChange={(e) => setSenha(e.target.value)}
          required
        />
        <button type="submit">Entrar</button>
      </form>
      {erro && <p style={{ color: "red" }}>{erro}</p>}
    </div>
  );
};

export default Login;
