from flask import Flask
from routes import routes
from controllers import controllers
from services import services

app = Flask(__name__)
app.register_blueprint(routes.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
