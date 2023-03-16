from flask import *
import json
from flask_mysqldb import MySQL





app = Flask(__name__) 

app.static_folder = 'static'
app.config['SECRET_KEY'] = 'hello123'  
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pandapanda'
app.config['MYSQL_DB'] = 'names'
 
mysql = MySQL(app) 


@app.route('/processed-result', methods=['POST'])
def events():    
    event_data = request.json
    data = json.loads(event_data)
    name = data['result']
    cur = mysql.connection.cursor()
    cur.execute(f"""SELECT * FROM names WHERE Muslim_Male_baby_names_A_to_Z = '{str(name.strip())}' """)
    apple = cur.fetchone()
    if apple:
        print(apple)
        return str(apple)
    elif str(apple)=='None':
        return 'Not Found'
    



if __name__ == '__main__':  

    app.run(host= '0.0.0.0', debug = True, port=3000) 