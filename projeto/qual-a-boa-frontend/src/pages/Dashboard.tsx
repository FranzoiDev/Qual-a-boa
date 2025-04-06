import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  getRestaurants,
  createRestaurant,
  updateRestaurant,
  deleteRestaurant,
//} from "../services/api";
} from "../services/api.mock";

interface Restaurant {
  cnpj: string;
  nome: string;
  endereco: string;
}

const Dashboard = () => {
  const navigate = useNavigate();
  const [restaurants, setRestaurants] = useState<Restaurant[]>([]);
  const [form, setForm] = useState<Restaurant>({
    cnpj: "",
    nome: "",
    endereco: "",
  });
  const [editingCnpj, setEditingCnpj] = useState<string | null>(null);

  // a proteção que o querido está preocupado 💅
  useEffect(() => {
    const token = localStorage.getItem("jwt_token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  // a busca dos estabelecimentos, talvez não esteja funcionando 
  useEffect(() => {
    fetchRestaurants();
  }, []);

  const fetchRestaurants = async () => {
    try {
      const data = await getRestaurants();
      setRestaurants(data);
    } catch (error) {
      console.error("Erro ao buscar restaurantes:", error);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm((prevForm) => ({ ...prevForm, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      if (editingCnpj) {
        await updateRestaurant(editingCnpj, form);
      } else {
        await createRestaurant(form);
      }

      setForm({ cnpj: "", nome: "", endereco: "" });
      setEditingCnpj(null);
      fetchRestaurants();
    } catch (error) {
      console.error("Erro ao salvar restaurante:", error);
    }
  };

  const handleEdit = (restaurant: Restaurant) => {
    setForm(restaurant);
    setEditingCnpj(restaurant.cnpj);
  };

  const handleDelete = async (cnpj: string) => {
    try {
      await deleteRestaurant(cnpj);
      fetchRestaurants();
    } catch (error) {
      console.error("Erro ao deletar restaurante:", error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("jwt_token");
    navigate("/login");
  };

  return (
    <div style={{ padding: "20px" }}>
      <header style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h2>Gerenciar Restaurantes</h2>
        <button onClick={handleLogout}>Sair</button>
      </header>

      <form onSubmit={handleSubmit} style={{ marginTop: "20px" }}>
        <input
          type="text"
          name="cnpj"
          placeholder="CNPJ"
          value={form.cnpj}
          onChange={handleChange}
          required
          disabled={!!editingCnpj}
        />
        <input
          type="text"
          name="nome"
          placeholder="Nome"
          value={form.nome}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="endereco"
          placeholder="Endereço"
          value={form.endereco}
          onChange={handleChange}
          required
        />
        <button type="submit">{editingCnpj ? "Salvar" : "Cadastrar"}</button>

        {editingCnpj && (
          <button
            type="button"
            onClick={() => {
              setForm({ cnpj: "", nome: "", endereco: "" });
              setEditingCnpj(null);
            }}
          >
            Cancelar
          </button>
        )}
      </form>

      <ul style={{ marginTop: "20px" }}>
        {restaurants.map((r) => (
          <li key={r.cnpj} style={{ marginBottom: "10px" }}>
            <strong>{r.nome}</strong> - {r.endereco} ({r.cnpj}){" "}
            <button onClick={() => handleEdit(r)}>Editar</button>
            <button onClick={() => handleDelete(r.cnpj)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;