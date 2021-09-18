from logging import NullHandler
from flask import Flask, render_template,request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='tuobra'
mysql =MySQL(app)

@app.route('/')
def inicio():
    return render_template('inicio.html')
    
@app.route('/editarI')
def editarI():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM items WERE id= %s',(id))
    data=cur.fetchall()
    return render_template('editarI.html', item=data[0])

@app.route('/editarP')
def editarI():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM proyectos WERE id= %s',(id))
    data=cur.fetchall()
    return render_template('editarP.html', proyecto=data[0])   
    
@app.route('/eliminarI/<int:id>')
def eliminarI(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM items WHERE id= {0}', format(id))
    mysql.connection.commit()
    return redirect(url_for('Items'))

@app.route('/eliminarP/<int:id>')
def eliminarI(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM proyectos WHERE id= {0}', format(id))
    mysql.connection.commit()
    return redirect(url_for('Proyectos'))

@app.route('/proyectos')
def proyectos():
    """cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM proyectos')
    data=cur.fetchall()"""""
    return render_template('proyectos.html')#, proyectos=data)

@app.route('/addP',methods=['POST'])
def addProyectos():
    if request.method == 'POST':
        codigoP=request.form['codigoP']
        nombreP=request.form['nombreP'] 
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO xxx (codigoP, nombreP) VALUES (%s, %s)', (codigoP, nombreP))
        mysql.connection.comit()

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/db')
def db():
    return render_template('db.html')

@app.route('/items')
def items():
    """cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM items')
    data=cur.fetchall()"""
    return render_template('items.html')#, items=data)



if __name__=='__main__':
    app.run(debug=True)