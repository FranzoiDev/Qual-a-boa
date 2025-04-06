import requests
import json
from datetime import datetime

BASE_URL = 'http://localhost:5000/api'
HEADERS = {'Content-Type': 'application/json'}

def test_login():
    print("\n=== Testando Login ===")
    data = {
        'email': 'email@example.com',
        'password': '1234'
    }
    response = requests.post(f'{BASE_URL}/auth/login', json=data, headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json().get('access_token')

def test_get_restaurants(token):
    print("\n=== Testando Listagem de Restaurantes ===")
    headers = {**HEADERS, 'Authorization': f'Bearer {token}'}
    response = requests.get(f'{BASE_URL}/restaurants', headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_create_restaurant(token):
    print("\n=== Testando Criação de Restaurante ===")
    headers = {**HEADERS, 'Authorization': f'Bearer {token}'}
    data = {
        'name': 'Restaurante Teste 2',
        'type': 'Pizza',
        'cnpj': '12345678901235',
        'street_number': '456',
        'city': 'São Paulo',
        'state': 'SP',
        'postal_code': '01234-568',
        'operating_hours': '11:00-23:00'
    }
    response = requests.post(f'{BASE_URL}/restaurants', json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json().get('id')

def test_search_restaurants(token):
    print("\n=== Testando Busca de Restaurantes ===")
    headers = {**HEADERS, 'Authorization': f'Bearer {token}'}
    params = {
        'name': 'Teste',
        'type': 'Pizza',
        'city': 'São Paulo'
    }
    response = requests.get(f'{BASE_URL}/restaurants/search', params=params, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_get_current_user(token):
    print("\n=== Testando Obter Usuário Atual ===")
    headers = {**HEADERS, 'Authorization': f'Bearer {token}'}
    response = requests.get(f'{BASE_URL}/auth/me', headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def main():
    print("Iniciando testes da API...")
    
    # Teste de login
    token = test_login()
    if not token:
        print("Falha no login. Encerrando testes.")
        return
    
    # Teste das rotas protegidas
    test_get_restaurants(token)
    restaurant_id = test_create_restaurant(token)
    test_search_restaurants(token)
    test_get_current_user(token)

if __name__ == '__main__':
    main() 