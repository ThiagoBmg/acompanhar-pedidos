import requests
from decouple import config
from time import sleep
from datetime import datetime

INTERVAL = int(config("INTERVAL", default=60))


CPF = config("CPF", default="X")
NF = config("NF", default="X")

URL = f"https://apimovvi.meridionalcargas.com.br/api/rastrear-carga/{CPF}/{NF}"

print(
    f"Seviço de Acompanhamento Ativado\nRealizando buscas em cada {INTERVAL/60} minutos"
)
while True:
    session = requests.Session()
    response = session.get(URL)
    current = datetime.now()
    try:
        import os

        os.system("clear")
        print("*" * 60, end="\n")
        print(f"Iniciando pesquisa... {current}")
        data = response.json()
        print(f"Ultima Ocorrência: {data['ocorrencias'][0]}")
    except Exception as exc:
        data = exc
        print(f"Erro ao buscar informações {data}")
    print("*" * 60, end="\n")
    sleep(INTERVAL)
