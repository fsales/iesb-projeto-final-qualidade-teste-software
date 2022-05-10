from locust import TaskSet, task


class UserRouteLoadTest(TaskSet):

    @task()
    def test_list_users(self):
        self.client.get("/usuarios", name="Listar usuários")

    @task()
    def test_create_users(self):
        payload = {
            "nome": "Teste Carga",
            "email": "testcaga55887@qa.com.br",
            "password": "teste123",
            "administrador": "true"
        }
        headers = {'content-type': 'application/json'}
        self.client.post("/usuarios",
                         name="Criar usuários",
                         json=payload,
                         headers=headers)
