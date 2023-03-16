from flask import *
import json
import requests




app = Flask(__name__) 

app.static_folder = 'static'
app.config['SECRET_KEY'] = 'hello123'   


@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/result", methods=['POST'])
def handle_data():
    if request.method == 'POST':
        string = request.form['string']
        j_string = {'result':string}
        string_ready = json.dumps(j_string)
        result = requests.post("http://names_detector_2:3000/processed-result", json=string_ready)
        return Response(result , status=200)
    

if __name__ == '__main__':  

    app.run(host= '0.0.0.0', debug = True) 



