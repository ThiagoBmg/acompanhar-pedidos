import os
from time import sleep
from decouple import config
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


CPF = config("GFL_CPF", default="X")
INTERVAL = int(config("INTERVAL", default=60))
URL = config("GFL_URL", default="https://cademinhaentrega.com.br/gfl")

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,5000")

def run(cpf=CPF):
    driver = webdriver.Chrome(options=chrome_options)
    # Abrir o site
    driver.get(URL)

    # Aguardar até que o formulário e os elementos estejam carregados
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "native-input.sc-ion-input-md"))
    )

    # Preencher o campo com a classe "native-input sc-ion-input-md"
    driver.find_element(By.CLASS_NAME, "native-input.sc-ion-input-md").send_keys(cpf)
    button_xpath = "#main-content > ion-content > shipment-search-form > ion-grid > form > ion-row:nth-child(4) > ion-col > ion-button"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_xpath))
    ).click()

    # Clicar no primeiro item da classe shipment-item
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shipment-item"))
    ).click()

    # Clicar no primeiro item da classe shipment-item
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "tracking-details-title.item.md.item-fill-none")
        )
    ).click()

    elementos = driver.find_elements(By.TAG_NAME, "p")
    for elemento in elementos:
        if (
            "PEDIDO" in elemento.text
            or "NOTA FISCAL" in elemento.text
            or "Previsão de entrega" in elemento.text
            or "ETIQUETA" in elemento.text
        ):
            # Imprime as informações extraídas
            print(elemento.text)
    print("\n")
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Obter os elementos diretamente do navegador
    elementos = driver.find_elements(
        By.CLASS_NAME,
        "ion-no-padding.item.md.item-fill-none.in-list.hydrated.item-label",
    )
    # Exibir as informações
    for elemento in elementos:
        data = elemento.find_elements(By.TAG_NAME, "H5")[0].text
        hora = elemento.find_elements(By.TAG_NAME, "H6")[0].text
        mensagem_pedido = elemento.find_elements(By.TAG_NAME, "H4")[0].text

        if mensagem_pedido:
            print(f"Data: {data}, Hora: {hora}, Mensagem: {mensagem_pedido}")
    driver.quit()


print(
    f"Seviço de Acompanhamento Ativado\nRealizando buscas em cada {INTERVAL/60} minutos"
)

while True:
    current = datetime.now()
    try:
        os.system("clear")
        print("*" * 60, end="\n")
        print(f"Iniciando pesquisa... {current}")
        run()
    except Exception as exc:
        print(f"Erro ao buscar informações {exc}")
    print("*" * 60, end="\n")
    sleep(INTERVAL)
