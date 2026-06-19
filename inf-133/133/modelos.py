from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_p = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    fecha_nac = db.Column(db.Date, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)

    def __init__(self, nombre, email, telefono, fecha_nac, genero, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_nac = fecha_nac
        self.genero = genero
        self.direccion = direccion
