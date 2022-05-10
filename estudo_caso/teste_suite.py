from locust import HttpUser, between

from estudo_caso.rota_usuarios import UsuarioRouteLoadTest
from estudo_caso.rota_produtos import ProdutosRouteLoadTest

class WebSiteUser(HttpUser):
    tasks = [
        UsuarioRouteLoadTest,
        ProdutosRouteLoadTest
    ]

    wait_time = between(5, 15)

