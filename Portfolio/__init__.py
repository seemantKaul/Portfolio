from flask import Flask


app = Flask(__name__)
app.secret_key = "cihfjsehrw3ho39e3pojn"

from Portfolio import routes
