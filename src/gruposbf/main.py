import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from decouple import config
from datetime import datetime

NUMERO_PEDIDO = config("NF", default="96218810901")

# INTERVAL = 600 # 10 min
INTERVAL = 10
URL = f"https://gruposbf.brudam.com.br/tracking/Painel.php?cPed={NUMERO_PEDIDO}"


def teste(html):
    soup = BeautifulSoup(html, "html.parser")

    # Extrai o número do pedido
    pedido_numero = soup.find("div", class_="text-orange").text.split(": ")[1]

    # Extrai o status do pedido
    status_pedidos = []
    metrics = soup.find_all("div", class_="metric")
    for metric in metrics:
        status = metric.get("status")
        title = metric.find("div", class_="title").text
        if status == "true":
            status_pedidos.append(title)

    # Extrai informações sobre transporte, método de envio, origem e destino
    info_transportadora = (
        soup.find("span", text="Transportadora").find_next_sibling("span").text
    )
    info_metodo_envio = (
        soup.find("span", text="Método de envio").find_next_sibling("span").text
    )
    info_origem = soup.find("span", text="Origem").find_next_sibling("span").text
    info_destino = soup.find("span", text="Destino").find_next_sibling("span").text

    # Extrai informações da tabela de ocorrências
    ocorrencias = []
    table_rows = soup.select(".table tbody tr")
    for row in table_rows:
        data_hora = row.find_all("td")[0].text.strip()
        ocorrencia = row.find_all("td")[1].text.strip()
        obs = row.find_all("td")[2].text.strip()
        ocorrencias.append(
            {"data_hora": data_hora, "ocorrencia": ocorrencia, "obs": obs}
        )

    # Imprime as informações extraídas
    print(f"Número do Pedido: {pedido_numero}")
    print(f"Status do Pedido: {status_pedidos}")
    print(f"Transportadora: {info_transportadora}")
    print(f"Método de Envio: {info_metodo_envio}")
    print(f"Origem: {info_origem}")
    print(f"Destino: {info_destino}")

    print("\nOcorrências:")
    for ocorrencia in ocorrencias:
        print(
            f"Data/Hora: {ocorrencia['data_hora']}, Ocorrência: {ocorrencia['ocorrencia']}, Observação: {ocorrencia['obs']}"
        )


print(
    f"Seviço de Acompanhamento Ativado\nRealizando buscas em cada {INTERVAL/60} minutos"
)

while True:
    session = requests.Session()
    response = session.get(URL)
    current = datetime.now()
    try:
        os.system("clear")
        print("*" * 60, end="\n")
        print(f"Iniciando pesquisa... {current}")
        teste(response.text)
    except Exception as exc:
        print(f"Erro ao buscar informações {exc}")
    print("*" * 60, end="\n")
    sleep(INTERVAL)
