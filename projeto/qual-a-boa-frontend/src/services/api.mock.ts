interface Restaurant {
    cnpj: string;
    nome: string;
    endereco: string;
  }
  
  let fakeData: Restaurant[] = [
    { cnpj: "12345678000100", nome: "Restaurante A", endereco: "Rua X, 100" },
    { cnpj: "98765432000199", nome: "Restaurante B", endereco: "Av. Y, 200" },
  ];
  
  export const getRestaurants = async () => {
    return new Promise<Restaurant[]>((resolve) => {
      setTimeout(() => resolve(fakeData), 500);
    });
  };
  
  export const createRestaurant = async (restaurant: Restaurant) => {
    return new Promise<void>((resolve) => {
      setTimeout(() => {
        fakeData.push(restaurant);
        resolve();
      }, 500);
    });
  };
  
  export const updateRestaurant = async (cnpj: string, updated: Restaurant) => {
    return new Promise<void>((resolve) => {
      setTimeout(() => {
        fakeData = fakeData.map((r) => (r.cnpj === cnpj ? updated : r));
        resolve();
      }, 500);
    });
  };
  
  export const deleteRestaurant = async (cnpj: string) => {
    return new Promise<void>((resolve) => {
      setTimeout(() => {
        fakeData = fakeData.filter((r) => r.cnpj !== cnpj);
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
  