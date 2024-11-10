import paho.mqtt.client as mqtt
import random
import time

# Configurações do broker MQTT
broker_address = "localhost"  # Usando localhost, já que Mosquitto está na mesma máquina
port = 1883
# Tópicos para os sensores
topics = {
    "sensores/temperatura": (15, 30),  # Sensor 1: Temperatura (15°C a 30°C)
    "sensores/ph": (3, 9),             # Sensor 2: pH (3 a 9)
    "sensores/oxigenio": (0, 15),     # Sensor 3: Oxigênio dissolvido (0 a 15 mg/L)
}

# Função callback quando a conexão é estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de status: " + str(rc))

# Função callback para quando uma mensagem é recebida (não será usada aqui)
def on_message(client, userdata, msg):
    print(f"Mensagem recebida: {msg.topic} -> {msg.payload.decode()}")

# Criar cliente MQTT
client = mqtt.Client()

# Definir as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conectar ao broker MQTT
client.connect(broker_address, port, 60)

# Iniciar o loop de conexão
client.loop_start()

# Função para gerar valores aleatórios dentro de um intervalo
def gerar_valor(sensor):
    return round(random.uniform(sensor[0], sensor[1]), 2)

# Simular a leitura de dados e publicar a cada 10 segundos
try:
    while True:
        for topic, range_ in topics.items():
            valor = gerar_valor(range_)
            print(f"Publicando {topic}: {valor}")
            client.publish(topic, str(valor))  # Publica o valor no tópico correspondente
        time.sleep(10)  # Espera 10 segundos para a próxima publicação
except KeyboardInterrupt:
    print("Simulação interrompida")
    client.loop_stop()
    client.disconnect()