import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd

# Função para criar e treinar o modelo
def train_model(data):
    # Dividir os dados em recursos (X) e rótulos (y)
    X = data[['temp_c', 'precip_mm', 'humidity']]
    y = data['precip_mm']  # Exemplo: tentando prever a precipitação
    
    # Dividir os dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Definir o modelo
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    
    # Compilar o modelo
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    
    # Treinar o modelo
    model.fit(X_train, y_train, epochs=10)
    
    # Avaliar o modelo
    loss, mae = model.evaluate(X_test, y_test)
    print(f"Mean Absolute Error: {mae}")
    
    return model
