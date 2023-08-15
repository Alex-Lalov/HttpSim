from flask import Flask, jsonify, request
from client import Client
import datetime, random

class App:
    def __init__(self):
        self.users = [Client("7124", "some1"), Client("user152", "word085"), Client("0123456", "pass123")]
        self.tokens = []
        self.timeout = datetime.timedelta(seconds=180)

        self.app = Flask("API")
        self.setup_routes()
    
    def setup_routes(self):
        # Sim Authorization Server
        @self.app.route('/auth', methods=['POST'])
        def authenticate():
            client = Client(request.json.get('client_id'), request.json.get('client_pass'))
            for i in range(len(self.users)):
                if client == self.users[i]:
                    token = random.randint(0,10000)
                    time = datetime.datetime.now()
                    self.tokens.append((token, time))
                    return jsonify(access_token = token)
            
            return jsonify(error='Authentication failed'), 401

        # Sim Resource API
        @self.app.route('/resource', methods=['GET'])
        def resource():
            auth_header = request.headers.get('Authorization')
            for i in range(len(self.tokens)):
                if auth_header and int(auth_header) == self.tokens[i][0]:
                    if datetime.datetime.now() <= self.timeout + self.tokens[i][1]:
                        return jsonify(data="This is API info you requested!") 
            return jsonify(error="Unauthorized"), 403
    
    def run(self):
        self.app.run(port=5000)
        
if __name__ == "__main__":
    App().run()