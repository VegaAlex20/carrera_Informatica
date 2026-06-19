from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelos import Paciente, db

pacientes = Blueprint('pacientes', __name__)

@pacientes.route("/")
def index():
    pacientes = Paciente.query.all()
    return render_template('paciente.html', pacientes=pacientes)

@pacientes.route('/new', methods=['POST'])
def adicionarP():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    fecha_nac = request.form['fecha_nac']
    genero = request.form['genero']
    direccion = request.form['direccion']

    new_paciente = Paciente(
        nombre=nombre, 
        email=email, 
        telefono=telefono, 
        fecha_nac=fecha_nac, 
        genero=genero, 
        direccion=direccion
    )

    db.session.add(new_paciente)
    db.session.commit()
    flash("Paciente guardado", 'success')
    return redirect(url_for('pacientes.index'))

@pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.email = request.form['email']
        paciente.telefono = request.form['telefono']
        paciente.fecha_nac = request.form['fecha_nac']
        paciente.genero = request.form['genero']
        paciente.direccion = request.form['direccion']

        db.session.commit()
        flash("Paciente actualizado", 'success')
        return redirect(url_for('pacientes.index'))
    return render_template('editar_paciente.html', paciente=paciente)

@pacientes.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash("Paciente eliminado", 'success')
    return redirect(url_for('pacientes.index'))
