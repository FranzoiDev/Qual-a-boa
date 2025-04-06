interface Restaurant {
  id: number;
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

let fakeData: Restaurant[] = [
  {
    id: 1,
    cnpj: "12345678000100",
    name: "Restaurante A",
    state: "SP",
    city: "São Paulo",
    type: "Comida Brasileira",
    operating_hours: "08:00 - 18:00",
    postal_code: "01000-000",
    street_number: "100",
    endereco: "Rua das Flores",
  },
  {
    id: 2,
    cnpj: "98765432000199",
    name: "Restaurante B",
    state: "RJ",
    city: "Rio de Janeiro",
    type: "Comida Italiana",
    operating_hours: "10:00 - 22:00",
    postal_code: "20000-000",
    street_number: "200",
    endereco: "Av. Atlântica",
  },
];

let idCounter = 3;

export const getRestaurants = async () => {
  return new Promise<Restaurant[]>((resolve) => {
    setTimeout(() => resolve(fakeData), 500);
  });
};

export const getRestaurantById = async (id: number) => {
  return new Promise<Restaurant | undefined>((resolve) => {
    setTimeout(() => {
      const found = fakeData.find((r) => r.id === id);
      resolve(found);
    }, 500);
  });
};

export const createRestaurant = async (restaurant: Omit<Restaurant, "id">) => {
  return new Promise<Restaurant>((resolve) => {
    setTimeout(() => {
      const newRestaurant: Restaurant = { ...restaurant, id: idCounter++ };
      fakeData.push(newRestaurant);
      resolve(newRestaurant);
    }, 500);
  });
};

export const updateRestaurant = async (id: number, updated: Omit<Restaurant, "id">) => {
  return new Promise<Restaurant | null>((resolve) => {
    setTimeout(() => {
      let updatedRestaurant: Restaurant | null = null;
      fakeData = fakeData.map((r) => {
        if (r.id === id) {
          updatedRestaurant = { ...updated, id };
          return updatedRestaurant;
        }
        return r;
      });
      resolve(updatedRestaurant);
    }, 500);
  });
};

export const deleteRestaurant = async (id: number) => {
  return new Promise<void>((resolve) => {
    setTimeout(() => {
      fakeData = fakeData.filter((r) => r.id !== id);
      resolve();
    }, 500);
  });
};

export const login = async (email: string, senha: string) => {
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
