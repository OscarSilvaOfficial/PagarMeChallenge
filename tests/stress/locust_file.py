from locust import HttpUser , between, task

class ApiUser(HttpUser): 

  @task
  def profile(self): 
    self.client.get('/transactions/')
