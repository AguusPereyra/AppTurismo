from flask import Flask
app = Flask(__name__)
app.secret_key = "turismo_secret_key"

from routes.auth import auth_bp
app.register_blueprint(auth_bp)

from routes.provincias import provincias_bp
app.register_blueprint(provincias_bp)

if __name__ == "__main__":
    app.run(debug=True)

    