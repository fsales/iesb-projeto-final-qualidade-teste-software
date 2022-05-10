from locust import TaskSet, task
from faker import Faker


class UsuarioRouteLoadTest(TaskSet):

    @task()
    def test_list_usuarios(self):
        self.client.get("/usuarios", name="Listar usuários")

    @task()
    def test_create_usuarios(self):
        fake = Faker()

        payload = {
            "nome": fake.name(),
            "email": "testcaga55887@qa.com.br",
            "password": "teste123",
            "administrador": "true"
        }
        headers = {'content-type': 'application/json'}
        self.client.post("/usuarios",
                         name="Criar usuários",
                         json=payload,
                         headers=headers)
