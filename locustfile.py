from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
         self.client.get("/")
        self.client.get("/other?page=1")
        self.client.get("/exp?value=1")
