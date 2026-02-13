import requests

headers = {"Authorization": "Token 6a893d034571fd76abf6101c24bf4914feaac90a"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

resultado = requests.get(url=url_base_cursos, headers=headers)
#print(resultado.json())
#print("STATUS:", resultado.status_code)
#print("BODY:", resultado.text)


# Testando se o endpoint está correto
assert resultado.status_code == 200
#assert resultado.json()["count"] == 2
assert resultado.json()["results"][0]["titulo"] == "Curso API"