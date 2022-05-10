from locust import HttpUser, between

from estudo_caso.rota_usuarios import UserRouteLoadTest


class WebSiteUser(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]

    wait_time = between(5, 15)
