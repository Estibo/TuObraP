from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.exceptions import MethodNotAllowed
from flask_mysqldb import MySQL 
import bcrypt

app= Flask(__name__)
app.secret_key="lor"
mysql =MySQL(app)

origen = bcrypt.gensalt()

@app.route("/")
def main():
    if 'nombre' in session:
        return render_template('inicio.html')
    else:
        return render_template('lor.html')

@app.route("/inicio")
def inicio():
    if 'nombre' in session:
        return render_template('inicio.html')
    else:
        return render_template('lor.html')

@app.route("/registrar",methos=["GET","POST"])
def registrar():
    if(request.method=="GET"):
        if 'nombre' in session:
            return render_template('inicio.html')
        else:
            return render_template('lor.html')
    else:
        nombre = request.form['nmNombreRegistro']
        correo = request.form['nmCorreoRegistro']
        password = request.form['nmPassWordRegistro']
        password_encode = password.encode("utf-8")
        password_encrip =bcrypt.hashpw(password_encode, origen)

        sQuery = "INSERT into Login (correo, password, nombre) VALUES ( %s, %s, %s)"
        
        cursor =mysql.connection.cursor()
        cursor.execute(sQuery,(correo,password_encrip,nombre))

        mysql.connection.commit()

        session['nombre']=nombre
        session['correo']=correo

        return redirect(url_for('inicio'))

@app.route ("/ingresar",methods=["GET","POST"])
def ingresar():
    if(request.method=="GET"):
        if 'nombre' in session:
            return render_template('inicio.html')
        else:
            return render_template('lor.html')
    else:
        correo = request.form['nmCorreoLogin']
        password = request.form['nmPassWordLogin']
        password_encode = password.encode("utf-8")

        cursor=mysql.connection.cursor()

        sQuery = "SELECT correo, password, nombre FROM Login WHERE correo =%s"

        cursor.execute(Squery,[correo])

        usuario = cursor.fetchone()

        cursor.close()

        if(usuario !=None):
            password_encrip_encode=usuario[1].encode()
            if(bcrypt.checkpw(password_encode,password_encrip_encode)):
                session['nombre']=usuario[2]
                return redirect(url_for('inicio'))
            else:
                flash("El password no es correcto", "alert-warning")
                return render_template('lor.html')
        else:
            flash("El correo no existe", "alert-warning")
            return render_template('lor.html')

@app.route("/salir")
def salir():
    session.clear()
    return redirect(url_for('ingresar'))

if __name__ == '__lor__':
    app.run(debug=True)