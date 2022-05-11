from locust import TaskSet, task


class CarrinhosRouteLoadTest(TaskSet):
    @task()
    def test_list_carrinhos(self):
        self.client.get("/carrinhos", name="Carrinhos - listar")
