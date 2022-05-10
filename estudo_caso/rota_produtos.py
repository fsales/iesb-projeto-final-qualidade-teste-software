from locust import TaskSet, task

class ProdutosRouteLoadTest(TaskSet):

    @task()
    def test_list_produtos(self):
        self.client.get("/produtos", name="Listar produtos")