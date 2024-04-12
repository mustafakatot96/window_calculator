from flask import Flask

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Optional: Reload templates on every request
from app import routes