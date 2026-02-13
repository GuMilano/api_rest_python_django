import requests

headers = {"Authorization": "Token 6a893d034571fd76abf6101c24bf4914feaac90a"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

novo_curso = {
    "titulo" : "Curso Agil",
    "url" : "http://www.teste.com.br/scrum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando a criação codigo HTTP 201
assert resultado.status_code == 201

# Testando se o titulo retornado é o mesmo do informado
assert resultado.json()["titulo"] == novo_curso["titulo"]