import sys
sys.path.append('..')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from core.config_db import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

url_prefix = '/vntu'

config = {'DB_USERNAME': DB_USERNAME,
          'DB_PASSWORD': DB_PASSWORD,
          'DB_HOST': DB_HOST,
          'DB_NAME': DB_NAME}

app = Flask('vntuapp')
app.url_map.strict_slashes = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://' + config['DB_USERNAME'] + ':' + \
                                        config['DB_PASSWORD'] + '@' + \
                                        config['DB_HOST'] + '/'+ config['DB_NAME'] + '?charset=utf8mb4&binary_prefix=true'

app.config["SECRET_KEY"] = "appsecretkey_vntuapp"

app.config['IMG_DOMAIN_URL'] = ''
app.config['DOMAIN_URL'] = ''

app.config["USER_APP_NAME"] = "Proton"

cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
# db = SQLAlchemy(app=app, engine_options={'connect_args': {'connect_timeout': 36000}})
db = SQLAlchemy(app=app)
