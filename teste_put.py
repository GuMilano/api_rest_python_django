import requests

headers = {"Authorization": "Token 6a893d034571fd76abf6101c24bf4914feaac90a"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

curso_atualizado = {
    "titulo" : "Curso Agil 2",
    "url" : "http://www.teste.com.br/scrum2"
}

# Buscando o curso com ID 2
curso = requests.get(url=f"{url_base_cursos}2/", headers=headers)
print(curso.json())

# Concatenação com o curso de ID 2
resultado = requests.put(url=f"{url_base_cursos}2/", headers=headers, data=curso_atualizado)

# Testando a criação codigo HTTP 200
assert resultado.status_code == 200

# Testando se o titulo retornado é o mesmo do informado
assert resultado.json()["titulo"] == curso_atualizado["titulo"]