import requests

headers = {"Authorization": "Token 6a893d034571fd76abf6101c24bf4914feaac90a"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"


resultado = requests.get(url=f"{url_base_cursos}2/", headers=headers)

# Testando o código HTTP 204
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.json()) == 0