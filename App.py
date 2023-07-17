from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
mysql = MySQL(app)
cors = CORS(app)

# CORS settings
app.config['CORS_HEADERS'] = 'Content-Type'

# Database connection configuration (MySQL)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'usersdetails'


@app.route('/api', methods=['GET'])
@cross_origin()
def Api():
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT username, password, email FROM usercredentials"
        cur.execute(sql)
        datos = cur.fetchall()
        credentials = []
        for fila in datos:
            credential = {'username': fila[0], 'password': fila[1], 'email': fila[2]}
            credentials.append(credential)
        return jsonify({'credentials': credentials, 'message': "Credentials found"})
    except Exception as ex:
        return jsonify({'mensaje': "Credentials not found"})


@app.route('/api/<username>', methods=['GET'])
@cross_origin()
def ApiId(username):
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT username, password, email FROM usercredentials WHERE username = '{0}'".format(
            username)
        cur.execute(sql)
        datos = cur.fetchone()
        if datos != None:
            credentials = {'username': datos[0], 'password': datos[1], 'email': datos[2]}
            return jsonify({'username': credentials, 'message': "User found"})
        else:
            return jsonify({'message': "User not found"})
    except Exception as ex:
        return "Error"


@app.route('/api', methods=['POST'])
@cross_origin()
def registerDates():
    try:
        cur = mysql.connection.cursor()
        sql = "INSERT INTO usercredentials (username, password, email) VALUES ('{0}', '{1}', '{2}')".format(
            request.json['username'], request.json['password'], request.json['email'])
        cur.execute(sql)
        mysql.connection.commit()
        return jsonify({"mensaje": "Usuario Registrado"})
    except Exception as ex:
        return jsonify({"mensaje": "Error"})
    
@app.route('/api/<username>', methods = ['PUT'])
@cross_origin()
def putUser(username):
    try:
        cur = mysql.connection.cursor()
        sql = """UPDATE usercredentials SET email = '{0}', password = {1} 
        WHERE username = '{2}'""".format(request.json['email'], request.json['password'], username)
        cur.execute(sql)
        mysql.connection.commit()
        return jsonify({"message": "Updated user"})
    except Exception as ex:
        return jsonify({"message": "impossible to update user"})

@app.route('/api/<username>', methods = ['DELETE'])
@cross_origin()
def deleteUser(username):
    try:
        cur = mysql.connection.cursor()
        sql = "DELETE FROM usercredentials WHERE username = '{0}'".format(username)
        cur.execute(sql)
        mysql.connection.commit()
        return jsonify({"message": "User delete"})
    except Exception as ex:
        return jsonify({"message": "User not delete"})

def pageNotFound(error):
    return "<h3>La pagina solicitada no existe</h3>", 404

if __name__ == '__main__':
    app.register_error_handler(404, pageNotFound)
    app.run(port=3000, debug=True)
