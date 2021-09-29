from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
import psycopg2

app = Flask(__name__)

conexion=psycopg2.connect(
    host="ec2-54-156-60-12.compute-1.amazonaws.com",
    database="dbbh6hacp3drg3",
    user="fwqjjvpnqunvzw",
    password="03dabfeee95631e9892033ee74fbae1d2b40bba01235d4e1579e2c13aed5621d"
)
app.secret_key='TuObra'


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/actp/<id>', methods=['POST'])
def actp(id):
    if request.method == 'POST':
        idp=request.form['idp']
        nombrep=request.form['nombrep']
        cur=conexion.cursor()
        cur.execute("""
            UPDATE proyectos
            SET idp= %s, nombrep= %s
            WHERE id=%s
        """,(idp,nombrep,id))
        conexion.commit()
    flash('Proyect updated Successfully')
    cur.close()
    return redirect(url_for('proyectos'))

@app.route('/acti/<id>', methods=['POST'])
def acti(id):
    if request.method == 'POST':
        idi=request.form['idi']
        nombrei=request.form['nombrei']
        titulo=request.form['titulo']
        unidad=request.form['unidad']
        valoru=request.form['valoru']
        cur=conexion.cursor()
        cur.execute("""
            UPDATE items
            SET idi= %s, nombrei= %s, titulo=%s, unidad=%s, valoru=%s
            WHERE id=%s
        """,(idi,nombrei,titulo,unidad,valoru,id))
        conexion.commit()
    flash('Proyect updated Successfully')
    cur.close()
    return redirect(url_for('items'))

@app.route('/actu/<id>', methods=['POST'])
def actu(id):
    if request.method == 'POST':
        idu=request.form['idu']
        nombreu=request.form['nombreu']
        emailu=request.form['emailu']
        idp=request.form['idp']
        nombrep=request.form['nombrep']
        cur=conexion.cursor()
        cur.execute("""
            UPDATE usuarios
            SET idu= %s, nombreu= %s, emailu=%s, idp=%s, nombrep=%s
            WHERE id=%s
        """,(idu,nombreu,emailu,idp,nombrep,id))
        conexion.commit()
    flash('User updated Successfully')
    cur.close()
    return redirect(url_for('usuarios'))

@app.route('/editarp/<id>')
def editarp(id):
    cur=conexion.cursor()
    cur.execute("SELECT * FROM proyectos WHERE id = %s;", [id])
    data=cur.fetchall()
    cur.close()
    return render_template('editarp.html', proyecto=data[0])
    
@app.route('/editari/<id>')
def editari(id):
    cur=conexion.cursor()
    cur.execute('SELECT * FROM items WHERE id= %s',[id])
    data=cur.fetchall()
    cur.close()
    return render_template('editari.html', item=data[0])

@app.route('/editaru/<id>')
def editaru(id):
    cur=conexion.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id= %s',[id])
    data=cur.fetchall()
    cur.close()
    return render_template('editaru.html', usuario=data[0])

@app.route('/eliminarp/<idp>')
def eliminarp(idp):
    cur=conexion.cursor()
    cur.execute("DELETE FROM proyectos WHERE id= %s;", [idp])
    conexion.commit()
    cur.close()
    return redirect(url_for('proyectos'))

@app.route('/eliminari/<idi>')
def eliminari(idi):
    cur=conexion.cursor()
    cur.execute("DELETE FROM items WHERE id = %s;", [idi])
    conexion.commit()
    cur.close()
    return redirect(url_for('items'))

@app.route('/eliminaru/<idi>')
def eliminaru(idi):
    cur=conexion.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s;", [idi])
    conexion.commit()
    cur.close()
    return redirect(url_for('usuarios'))

@app.route('/addp',methods=['POST'])
def addProyectos():
    if request.method == 'POST':
        codigoP=request.form['idp']
        nombreP=request.form['nombrep']
        cur=conexion.cursor()
        cur.execute('INSERT INTO proyectos (idp, nombrep) VALUES (%s, %s)', (codigoP, nombreP))
        conexion.commit()
        flash('Proyect added successfully')
        cur.close()
        return redirect(url_for('proyectos'))

@app.route('/addi',methods=['POST'])
def addItems():
    if request.method == 'POST':
        codigoI=request.form['idi']
        nombreI=request.form['nombrei'] 
        titulo=request.form['titulo'] 
        unidad=request.form['unidad'] 
        valoru=request.form['valoru'] 
        cur=conexion.cursor()
        cur.execute('INSERT INTO items (idi, nombrei, titulo, unidad, valoru) VALUES (%s, %s, %s, %s, %s)', (codigoI, nombreI,titulo,unidad,valoru))
        conexion.commit()
        flash('Item added successfully')
        cur.close()
        return redirect(url_for('items'))

@app.route('/addu',methods=['POST'])
def addUsuarios():
    if request.method == 'POST':
        idu=request.form['idu']
        nombreu=request.form['nombreu'] 
        emailu=request.form['emailu'] 
        idp=request.form['idp'] 
        nombrep=request.form['nombrep'] 
        cur=conexion.cursor()
        cur.execute('INSERT INTO usuarios (idu, nombreu, emailu, idp, nombrep) VALUES (%s, %s, %s, %s, %s)', (idu, nombreu,emailu,idp,nombrep))
        conexion.commit()
        flash('User added successfully')
        cur.close()
        return redirect(url_for('usuarios'))

@app.route('/proyectos')
def proyectos():
    cur=conexion.cursor()
    cur.execute('SELECT * FROM proyectos')
    data=cur.fetchall()
    cur.close()
    return render_template('proyectos.html', proyectos=data)

@app.route('/items')
def items():
    cur=conexion.cursor()
    cur.execute('SELECT * FROM items')
    data=cur.fetchall()
    cur.close()
    return render_template('items.html', items=data)

@app.route('/usuarios')
def usuarios():
    cur=conexion.cursor()
    cur.execute('SELECT * FROM usuarios')
    data=cur.fetchall()
    cur.close()
    return render_template('usuarios.html', usuarios=data)

@app.route('/db')
def db():
    return render_template('db.html')

if __name__=='__main__':
    app.run(debug=True)