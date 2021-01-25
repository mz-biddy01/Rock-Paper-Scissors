from flask import Flask

app = Flask(__name__)
app.secret_key = "secret"

# from app.controllers import controller
from app import controller
