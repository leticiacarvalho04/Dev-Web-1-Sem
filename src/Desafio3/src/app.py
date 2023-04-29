from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec23'
app.config['MYSQL_DB'] = 'Faculdade'

mysql = MySQL(app)

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/quemsomos") 
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contato", methods=['POST','GET']) 
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email,assunto,descricao))

        mysql.connection.commit()

        cur.close()

        return 'sucesso'
    return render_template("contato.html")

if __name__ == '__main__':
    app.run()