import requests
import json

# Função para obter dados históricos da WeatherAPI
def get_weatherapi_data(lat, lon, key, start_date):
    url = f"http://api.weatherapi.com/v1/history.json?key={key}&q={lat},{lon}&dt={start_date}"
    response = requests.get(url)
    
    # Adicionando prints para debugging
    print(f"URL chamada: {url}")  # Mostra a URL chamada
    print(f"Código de Status: {response.status_code}")  # Mostra o status da requisição
    
    if response.status_code == 200:
        return response.json()  # Retorna o JSON de dados
    else:
        print(f"Erro na requisição: {response.status_code} - {response.text}")  # Mensagem detalhada
        return None

# Função para obter dados atuais da Windy API
def get_windy_data(lat, lon, model, parameters, levels, key):
    url = "https://api.windy.com/api/point-forecast/v2"
    payload = {
        "lat": lat,
        "lon": lon,
        "model": model,
        "parameters": parameters,
        "levels": levels,
        "key": key
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)  # Alterado para usar json=payload
    
    # Adicionando prints para debugging
    print(f"URL chamada: {url}")  # Mostra a URL chamada
    print(f"Código de Status: {response.status_code}")  # Mostra o status da requisição
    
    if response.status_code == 200:
        return response.json()  # Retorna o JSON de dados
    else:
        print(f"Erro na requisição: {response.status_code} - {response.text}")  # Mensagem detalhada
        return None
