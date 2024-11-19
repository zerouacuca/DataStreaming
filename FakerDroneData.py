from faker import Faker
import random
import time

fake = Faker()

def generate_drone_data():
    return {
        "drone_id": fake.uuid4(),
        "timestamp": fake.iso8601(),
        "latitude": round(random.uniform(-90.0, 90.0), 6),
        "longitude": round(random.uniform(-180.0, 180.0), 6),
        "altitude": round(random.uniform(0, 5000), 2),  # em metros
        "speed": round(random.uniform(0, 200), 2),  # em km/h
        "temperature": round(random.uniform(-20, 50), 2)  # em graus Celsius
    }

if __name__ == "__main__":
    print("Iniciando o streaming de dados dos sensores do drone...\n")
    while True:
        data = generate_drone_data()
        print(data)
        time.sleep(1)  # Simula 1 segundo entre as leituras
