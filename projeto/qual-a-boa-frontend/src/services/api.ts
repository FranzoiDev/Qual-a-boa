import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api",
});

// JWT pras páginas pq o querido tem medo de roubo 💅
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("jwt_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Funções nomeadas, só ver o nome da função que ja da pra entender 🔎 se n sabe inglês vá estudar
export const getRestaurants = async () => {
  const response = await api.get("/restaurants");
  return response.data;
};

export const getRestaurantById = async (id: number) => {
  const response = await api.get(`/restaurants/${id}`);
  return response.data;
};

export const createRestaurant = async (restaurant: {
  cnpj: string;
  name: string;
  state: string;
  city: string;
  type: string;
  operating_hours: string;
  postal_code: string;
  street_number: string;
  endereco: string;
}) => {
  const response = await api.post("/restaurants", restaurant);
  return response.data;
};

export const updateRestaurant = async (
  id: number,
  restaurant: {
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
) => {
  const response = await api.put(`/restaurants/${id}`, restaurant);
  return response.data;
};


export const deleteRestaurant = async (id: number) => {
  const response = await api.delete(`/restaurants/${id}`);
  return response.data;
};

export default api;
