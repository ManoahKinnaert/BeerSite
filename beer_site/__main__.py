from flask import Flask 
import os

from frontend import front_bp
from backend import backend_bp

server = Flask(__name__)
server.register_blueprint(backend_bp)
server.register_blueprint(front_bp)

if __name__ == "__main__":
    env = os.environ
    debug = env.get("DEBUG", "False").lower() in ("true", "1", "yes") 
    server.run(debug=debug, port=5050, host="0.0.0.0" if not debug else "127.0.0.1")