from locust import TaskSet, task
from faker import Faker


class UsuarioRouteLoadTest(TaskSet):
    @task()
    def test_list_usuarios(self):
        self.client.get("/usuarios", name="Usuários - listar")

    @task()
    def test_create_usuarios(self):
        faker = Faker()

        payload = {
            "nome": faker.name(),
            "email": faker.email(),
            "password": "teste123",
            "administrador": "true",
        }
        headers = {"content-type": "application/json"}
        self.client.post(
            "/usuarios", name="Usuários - criar", json=payload, headers=headers
        )
