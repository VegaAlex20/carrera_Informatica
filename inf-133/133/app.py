from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.paciente import pacientes
from modelos import db, Paciente

app = Flask(__name__)
app.secret_key = "secret_key"  # Es mejor almacenar esta clave en una variable de entorno para mayor seguridad
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:123456@localhost/5?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(pacientes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
