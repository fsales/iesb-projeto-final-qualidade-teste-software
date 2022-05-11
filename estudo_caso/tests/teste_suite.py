from locust import HttpUser, between

from estudo_caso.tests.carrinhos.rota_carrinhos import CarrinhosRouteLoadTest
from estudo_caso.tests.usuarios.rota_usuarios import UsuarioRouteLoadTest
from estudo_caso.tests.produtos.rota_produtos import ProdutosRouteLoadTest


class WebSiteUser(HttpUser):
    tasks = [UsuarioRouteLoadTest, ProdutosRouteLoadTest, CarrinhosRouteLoadTest]

    wait_time = between(5, 15)
