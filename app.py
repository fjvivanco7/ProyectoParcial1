#Importar la biblioteca de flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
#1. nombre por defecto
#2. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='templates')

usuarios =[]

#Clave secreta de la aplicacion
app.secret_key = '123456789'

#Controlador de la ruta por defecto
@app.route('/')
def index():
    return render_template('login.html',usuarios=usuarios)

@app.route('/enviar',methods=["GET","POST"])
def enviarDatos():
    
    email=request.form.get("email")
    password=request.form.get("password")
    

    if request.method =="GET":
        return render_template("agregar.html")
    else:   
            data=[
                    email,
                    password
                 ]
            
            usuarios.append(data)
            return redirect("/")

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/acerca-nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/snacks')
def snacks():
    return render_template('snacks.html')
@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')
@app.route('/postres')
def postres():
    return render_template('postres.html')
@app.route('/comidas')
def comidas():
    return render_template('comidas.html')


#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)