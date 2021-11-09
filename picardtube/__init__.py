from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jsglue import JSGlue
from flask_migrate import Migrate
from config import Config
db = SQLAlchemy()
migrate = Migrate()
jsglue = JSGlue()

from picardtube.settings import bp as bp_settings
from picardtube.overview import bp as bp_overview
from picardtube.init import init as init_db

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    jsglue.init_app(app)
    app.register_blueprint(bp_overview)
    app.register_blueprint(bp_settings)
    init_db(app)
    return app

import picardtube.database