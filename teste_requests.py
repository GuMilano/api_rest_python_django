import requests

# GET Avaliacoes
avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

#Acessando o código de status HTTP
#print(avaliacoes.status_code)

# Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando a quantidade de registros
#print(avaliacoes.json() ["count"])

# Acessando a próxima página de resultados
#print(avaliacoes.json()["next"])

# Acessando os resultados desta página
#print(avaliacoes.json()["results"])
#print(type(avaliacoes.json()["results"]))

#Acessando o primeiro elemento da lista de resuldados
#print(avaliacoes.json()["results"][0])

#Acessando o último elemento da lista de resultados
#print(avaliacoes.json()["results"][-1])

#Acessando somente o nome da pessoa que fez a última avaliação
#print(avaliacoes.json()["results"][-1]["nome"])

# GET Avaliacao
#avaliacao = requests.get("http://localhost:8000/api/v2/avaliacoes/1")
#print(avaliacao.json())

#GET Cursos
headers = {"Authorization": "Token 6a893d034571fd76abf6101c24bf4914feaac90a"}
cursos = requests.get("http://localhost:8000/api/v2/cursos/")
print(cursos.status_code)
print(cursos.json())




