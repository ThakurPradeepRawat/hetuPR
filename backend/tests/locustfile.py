from locust import HttpUser, between, task


class HetuPRUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def health_check(self):
        self.client.get("/health")

    @task(1)
    def get_metrics(self):
        self.client.get("/api/v1/metrics/")
