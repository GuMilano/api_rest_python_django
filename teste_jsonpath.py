import requests
from jsonpath_ng import parse

avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")
data = avaliacoes.json()

expr = parse("$.results[0].avaliacao")
print(expr)
resultados = [match.value for match in expr.find(data)]

print(resultados)
