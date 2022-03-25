from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json

import secretmanager

app = Flask(__name__)


@app.route('/liststudents')
def hello_world():  # put application's code here
    # DBsecret = secretmanager.get_secret()
    # print(DBsecret)
    return render_template('test.html', data=DBsecret)


@app.route('/storedata', methods=['POST'])
def storedata():
    studentobj = {
        "first_name": None,
        "last_name":None,
        "banner": None
    }
    cursor = mysql.connection.cursor()
    students = request.json
    for student in students:
        studentobj = student
        cursor.execute('''insert into students ('first_name', 'last_name', 'banner') value (studentobj.first_name,
        studentobj.last_name, studentobj.banner)''')
    cursor.commit()
    cursor.close
    cursor.close()
    print(student)
    return student

if __name__ == '__main__':
    app.run()

# app = Flask(__name__)
DBsecret = secretmanager.get_secret()
app.config['MYSQL_HOST'] = 'database-2-a3.cluster-cgdwyds2xr5r.us-east-1.rds.amazonaws.com'
# app.config['MYSQL_HOST'] = 'database-1test.cluster-cgdwyds2xr5r.us-east-1.rds.amazonaws.com:3306'
app.config['MYSQL_USER'] = json.loads(DBsecret.get('SecretString'))['DBusername']
app.config['MYSQL_PASSWORD'] = json.loads(DBsecret.get('SecretString'))['DBpassword']
# app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'database-2-a3'

mysql = MySQL(app)

