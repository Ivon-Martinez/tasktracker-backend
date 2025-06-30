from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from application.routes import main_bp
from application.errors import register_error_handlers


mysql = MySQL()

def create_app():
	app = Flask(__name__)

	app.config['MYSQL_HOST'] = 'tasktracker-mysql'
	app.config['MYSQL_USER'] = 'taskuser'
	app.config['MYSQL_PASSWORD'] = 'taskpass'
	app.config['MYSQL_DB'] = 'tasktrackerdb'

	mysql.init_app(app)
	CORS(app)


	app.register_blueprint(main_bp)
	register_error_handlers(app)

	return app

