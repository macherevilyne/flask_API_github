# импортируем библиотеки
from flask import Flask
import requests
from flask_restful import Api, Resource


app = Flask(__name__) # создание приложения
api = Api()          #



class Main(Resource):

    def get(self):

        github_username = 'macherevilyne'
        repo = 'ilmax'
        api_url = f"https://api.github.com/repos/{github_username}/{repo}"
        response = requests.get(api_url).json()
        return response



class Main2(Resource):
    def get(self):
        github_username = 'macherevilyne'
        repo = 'ilmax'
        api_url = f"https://api.github.com/repos/{github_username}/{repo}/forks"
        response = requests.get(api_url).json()
        return response

class Main3(Resource):
    def get(self):
        github_username = 'macherevilyne'
        repo = 'ilmax'
        api_url = f"https://api.github.com/repos/{github_username}/{repo}/issues"
        response = requests.get(api_url).json()

        return response

class Main4(Resource):
    def get(self):
        github_username = 'HowProgrammingWorks'
        repo = 'NodejsStarterKit'
        api_url = f"https://api.github.com/repos/{github_username}/{repo}/pulls"
        response = requests.get(api_url).json()
        return response



class Main5(Resource):
    def get(self):
        github_username = 'bors-ng'
        repo = 'bors-ng'
        api_url = f"https://api.github.com/repos/{github_username}/{repo}/pulls"
        response = requests.get(api_url).json()
        return response



api.add_resource(Main,'/api/main')
api.add_resource(Main2, '/api/main/forks')
api.add_resource(Main3, '/api/main/issues')
api.add_resource(Main4, '/api/main/all_pull_requests')
api.add_resource(Main5, '/api/main/pull_requests/days')


api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')
