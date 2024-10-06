import pandas as pd
import numpy as np
import requests

# Função para pré-processar os dados históricos
def preprocess_weather_data(weather_data):
    # Exemplo de como processar os dados da WeatherAPI
    data = weather_data['forecast']['forecastday'][0]['hour']
    df = pd.DataFrame(data)
    
    # Selecionar apenas as colunas importantes para o modelo
    df = df[['time_epoch', 'temp_c', 'precip_mm', 'humidity']]
    
    # Normalizar os dados (opcional)
    df['temp_c'] = (df['temp_c'] - df['temp_c'].min()) / (df['temp_c'].max() - df['temp_c'].min())
    
    return df

# Função para processar dados da Windy API
def preprocess_windy_data(windy_data):
    # Exemplo simples de como converter os dados da Windy em DataFrame
    df = pd.DataFrame(windy_data['ts'], columns=['timestamp'])
    
    # Adicionar temperatura
    if 'temp-surface' in windy_data and isinstance(windy_data['temp-surface'], list):
        df['temp_c'] = [temp - 273.15 for temp in windy_data['temp-surface']]  # Converter de Kelvin para Celsius
    else:
        print("Chave 'temp-surface' não encontrada ou não é uma lista nos dados da Windy API.")
        df['temp_c'] = np.nan
    
    # Adicionar umidade relativa
    if 'rh-surface' in windy_data:
        df['humidity'] = windy_data['rh-surface']
    else:
        print("Chave 'rh-surface' não encontrada nos dados da Windy API.")
        df['humidity'] = np.nan
    
    # Adicionar precipitação
    if 'precip-surface' in windy_data:
        df['precip'] = windy_data['precip-surface']
    else:
        print("Chave 'precip-surface' não encontrada nos dados da Windy API.")
        df['precip'] = np.nan
    
    # Remover linhas com valores ausentes
    df = df.dropna()
    
    return df


def get_weatherapi_data(lat, lon, key, start_date):
    url = f"http://api.weatherapi.com/v1/history.json?key={key}&q={lat},{lon}&dt={start_date}"
    response = requests.get(url)
    
    # Adicionando prints para debugging
    print(f"URL: {url}")  # Mostra a URL chamada
    print(f"Status Code: {response.status_code}")  # Mostra o status da requisição
    
    if response.status_code == 200:
        return response.json()  # Retorna o JSON de dados
    else:
        print(f"Erro na requisição: {response.status_code} - {response.text}")  # Mensagem detalhada
        return None
