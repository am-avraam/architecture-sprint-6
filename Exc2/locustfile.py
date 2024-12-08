from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(0.1, 0.5)  # Уменьшаем время ожидания между запросами
    
    @task
    def get_index(self):
        # Создаем большой payload для увеличения нагрузки на память
        payload = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=1000))
        headers = {'Content-Type': 'application/json', 'X-Large-Payload': payload}
        self.client.get("/", headers=headers)