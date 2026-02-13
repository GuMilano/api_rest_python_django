import requests


class TestCursos:
    headers = {"Authorization": "Token 6a893d034571fd76abf6101c24bf4914feaac90a"}
    url_base_cursos = "http://localhost:8000/api/v2/cursos/"

# Todo método de test deve começar com test no pytest
    def test_get_cursps(self):
        cursos = requests.get(url = self.url_base_cursos, headers = self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        cursos = requests.get(url = f"{self.url_base_cursos}1/", headers = self.headers)
        assert cursos.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "curso": "Curso API 5",
            "url" : "http://teste.com/API5",
        }
        resultado = requests.post(url = self.url_base_cursos, data = novo_curso)
        assert resultado.status_code == 201
        assert resultado.json()["titulo"] == novo_curso["titulo"]

    def test_put_curso(self):
        atualiza_curso = {
            "curso" : "Novo curso API",
            "url" : "http://teste.com/NovoApi"
        }
        resultado = requests.put(url = f"{self.url_base_cursos}2/", headers=self.headers, data = atualiza_curso)
        assert resultado.status_code == 200
        #assert resultado.json()["titulo"] == atualiza_curso["titulo"]

    def test_put_titulo_curso(self):
            atualiza_curso = {
                "titulo" : "Novo titulo API2",
                "url" : "http://teste.com/NovoApi2"
            }
            resultado = requests.put(url=f"{self.url_base_cursos}1/", headers=self.headers, data=atualiza_curso)
            assert resultado.json()["titulo"] == atualiza_curso["titulo"]

    def test_delete_curso(self):
        resultado = requests.put(url=f"{self.url_base_cursos}3/", headers=self.headers)
        assert resultado.status_code == 204 and len(resultado.text) == 0

# Executado via comando: pytest teste_pytest.py
