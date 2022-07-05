import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app

# Ak bude problem s DB:
# sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) unable to open database file
# treba dat 4x slash miesto 3x -> sqlite:////
db_path = 'sqlite:///' + os.path.join(basedir, 'data.db')

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)