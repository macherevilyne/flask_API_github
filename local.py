import requests

res = requests.get("http://127.0.0.1:5000/api/main") # запрос получение информации
forks = requests.get("http://127.0.0.1:5000/api/main/forks")
issues = requests.get("http://127.0.0.1:5000/api/main/issues")
all_pull_requests = requests.get("http://127.0.0.1:5000/api/main/all_pull_requests")
pull_requests_days = requests.get("http://127.0.0.1:5000/api/main/pull_requests/days")

