import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  getRestaurants,
  createRestaurant,
  updateRestaurant,
  deleteRestaurant,
} from "../services/api.mock";

const stateOptions = [
  "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES",
  "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
  "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
  "SP", "SE", "TO"
];

const typeOptions = [
  "balada",
  "bar",
  "restaurante",
  "conveniencia",
  "tabacaria",
];

interface Restaurant {
  id?: number;
  cnpj: string;
  name: string;
  state: string;
  city: string;
  type: string;
  operating_hours: string;
  postal_code: string;
  street_number: string;
  endereco: string;
}

const Dashboard = () => {
  const navigate = useNavigate();
  const [restaurants, setRestaurants] = useState<Restaurant[]>([]);
  const [form, setForm] = useState<Restaurant>({
    cnpj: "",
    name: "",
    state: "",
    city: "",
    type: "",
    operating_hours: "",
    postal_code: "",
    street_number: "",
    endereco: "",
  });
  const [editingId, setEditingId] = useState<number | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("jwt_token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

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

  // 🔧 Corrigido: agora aceita <input> e <select>
  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setForm((prevForm) => ({ ...prevForm, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      if (editingId) {
        await updateRestaurant(editingId, form);
      } else {
        await createRestaurant(form);
      }

      setForm({
        cnpj: "",
        name: "",
        state: "",
        city: "",
        type: "",
        operating_hours: "",
        postal_code: "",
        street_number: "",
        endereco: "",
      });
      setEditingId(null);
      fetchRestaurants();
    } catch (error) {
      console.error("Erro ao salvar restaurante:", error);
    }
  };

  const handleEdit = (restaurant: Restaurant) => {
    setForm(restaurant);
    setEditingId(restaurant.id || null);
  };

  const handleDelete = async (id: number) => {
    try {
      await deleteRestaurant(Number(id));
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

      <form onSubmit={handleSubmit} style={{ marginTop: "20px", display: "grid", gap: "8px" }}>
        <input name="cnpj" placeholder="CNPJ" value={form.cnpj} onChange={handleChange} required disabled={!!editingId} />
        <input name="name" placeholder="Nome" value={form.name} onChange={handleChange} required />
        <select name="state" value={form.state} onChange={handleChange} required>
          <option value="">Selecione o estado (UF)</option>
          {stateOptions.map((uf) => (
            <option key={uf} value={uf}>{uf}</option>
          ))}
        </select>
        <input name="city" placeholder="Cidade" value={form.city} onChange={handleChange} required />
        <select name="type" value={form.type} onChange={handleChange} required>
          <option value="">Selecione o tipo</option>
          {typeOptions.map((type) => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>
        <input name="operating_hours" placeholder="Horário de Funcionamento" value={form.operating_hours} onChange={handleChange} required />
        <input name="postal_code" placeholder="CEP" value={form.postal_code} onChange={handleChange} required />
        <input name="street_number" placeholder="Número" value={form.street_number} onChange={handleChange} required />
        <input name="endereco" placeholder="Endereço" value={form.endereco} onChange={handleChange} required />

        <button type="submit">{editingId ? "Salvar" : "Cadastrar"}</button>
        {editingId && (
          <button
            type="button"
            onClick={() => {
              setForm({
                cnpj: "",
                name: "",
                state: "",
                city: "",
                type: "",
                operating_hours: "",
                postal_code: "",
                street_number: "",
                endereco: "",
              });
              setEditingId(null);
            }}
          >
            Cancelar
          </button>
        )}
      </form>

      <ul style={{ marginTop: "20px" }}>
        {restaurants.map((r) => (
          <li key={r.id} style={{ marginBottom: "10px" }}>
            <strong>{r.name}</strong> - {r.type} ({r.cnpj})<br />
            {r.city}/{r.state} - {r.postal_code}, nº {r.street_number}<br />
            {r.endereco && <span>Endereço: {r.endereco}<br /></span>}
            <em>{r.operating_hours}</em>
            <br />
            <button onClick={() => handleEdit(r)}>Editar</button>
            <button onClick={() => handleDelete(r.id!)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
