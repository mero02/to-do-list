from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Extensiones
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    login_manager.init_app(app)

    # Importar modelos y definir el user_loader
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar los blueprints
    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app
