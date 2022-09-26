from crypt import methods
from __init__ import app
from flask import Flask,render_template,redirect,request,session,flash
from models.dojo import Dojo
from models.ninja import Ninja

@app.route('/home')
def home():
    dojos = Dojo.get_all()
    return render_template('home.html',dojos=dojos)

@app.route('/show/<dojo_id>')
def get_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    dojo = Dojo.get_dojo_by_id(data)
    ninjas = Dojo.get_ninjas_from_dojo(data)
    return render_template('dojo_show.html',dojo=dojo,ninjas=ninjas)

@app.route('/agregar_dojo')
def agregar_dojo():
    return render_template('agregar_dojo.html')

@app.route('/nuevo_dojo',methods=['POST'])
def nuevo_dojo():
    nombre_nuevo_dojo = request.form['nombre_nuevo_dojo']
    data = {
        "nombre": nombre_nuevo_dojo
    }
    Dojo.guardar(data)
    return redirect('/home')

@app.route('/agregar_ninja')
def agregar_ninja():
    dojos = Dojo.get_all()
    return render_template('agregar_ninja.html',dojos=dojos)

@app.route('/nuevo_ninja',methods=['POST'])
def nuevo_ninja():
    data = {
        "dojo_id": request.form['dojo_id'],
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad']
    }
    Ninja.guardar(data)
    return redirect('/home')
    