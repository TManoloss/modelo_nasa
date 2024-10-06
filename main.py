from get_data import get_weatherapi_data, get_windy_data
from process_data import preprocess_weather_data, preprocess_windy_data
from train_model import train_model

# API keys e parâmetros
weatherapi_key = "d81a0513b98040018ef195410240510"
windy_key = "NnPS6iWdFhK4grNjYDzELL8BD0ZifNgR"
lat, lon = -24.046, -52.3838  # Campo mourao
start_date = "2023-11-08"

# Coletar dados atuais da WeatherAPI
current_weather_data = get_weatherapi_data(lat, lon, weatherapi_key, start_date)  # Adicionado o parâmetro de data

# Verificar se os dados foram obtidos com sucesso
if current_weather_data is not None:
    processed_weather_data = preprocess_weather_data(current_weather_data)
else:
    print("Erro ao obter dados da WeatherAPI. Verifique a chave da API e os parâmetros.")
    # Você pode optar por encerrar o programa ou lidar com o erro de outra forma
    exit(1)  # Encerra o programa se os dados não forem obtidos

# Treinar o modelo com os dados históricos
model = train_model(processed_weather_data)

# Usar dados da Windy API para previsão
windy_data = get_windy_data(lat, lon, "gfs", ["temp", "precip"], ["surface"], windy_key)
processed_windy_data = preprocess_windy_data(windy_data)

# Verificar se as colunas necessárias existem antes de realizar a previsão
required_columns = ['temp_c', 'precip']
missing_columns = [col for col in required_columns if col not in processed_windy_data.columns]

if not missing_columns:
    prediction = model.predict(processed_windy_data[required_columns])
    print(f"Previsão de precipitação: {prediction}")
else:
    print(f"As colunas ausentes são: {missing_columns}. Verifique os dados processados da Windy API.")
    print("Dados disponíveis:", processed_windy_data.columns.tolist())
    # Adicionando um retorno ou tratamento de erro se as colunas estiverem ausentes
    exit(1)  # Encerra o programa se as colunas necessárias não estiverem presentes
