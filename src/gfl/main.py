# import requests


# def obter_access_token():
#     url = "https://public-tracking.sinclog.app.br/v1/auth/token"
#     # Enviar uma requisição GET para obter o token
#     response = requests.get(url)
#     # Verificar se a requisição foi bem-sucedida (código de status 200)
#     if response.status_code == 200:
#         # Extrair o access token do payload JSON
#         payload = response.json()
#         access_token = payload.get("access_token")
#         # Retornar o access token
#         return access_token
#     else:
#         print(f"A requisição falhou com o código de status: {response.status_code}")
#         return None


# def obter_detalhes_do_pedido(numero_documento, token):
#     url = f"https://public-tracking.sinclog.app.br/v1/shipments/destination-doc-number/{numero_documento}\
#         ?infoPager.pageSize=50&infoPager.currentPage=1&dtRegisterStart=2023-12-02T21:04:16.731Z&dtRegisterEnd=2024-01-02T21:04:16.731Z"

#     # Configurar o cabeçalho com o token de autorização
#     headers = {
#         "Authorization": f"Bearer {token}",
#     }

#     # Enviar uma requisição GET para obter os detalhes do pedido
#     response = requests.get(url, headers=headers)

#     # Verificar se a requisição foi bem-sucedida (código de status 200)
#     if response.status_code == 200:
#         # Extrair os detalhes do pedido do payload JSON
#         detalhes_do_pedido = response.json()

#         # Retornar os detalhes do pedido
#         return detalhes_do_pedido
#     else:
#         print(f"A requisição falhou com o código de status: {response.status_code}")
#         return None


# # Chamar o método para obter o access token
# token = obter_access_token()
# # Substitua 'SEU_NUMERO_DE_DOCUMENTO' pelo número do documento desejado
# numero_documento = ""
# # Chamar o método para obter os detalhes do pedido
# detalhes_pedido = obter_detalhes_do_pedido(numero_documento, token)

# # Imprimir os detalhes do pedido, se estiverem disponíveis
# if detalhes_pedido:
#     print(f"Detalhes do Pedido: {detalhes_pedido}")
