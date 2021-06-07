from flask import Flask
from flask import request
from data import data as data
import json

app = Flask(__name__)

@app.route('/api', methods=['GET', 'PUT'])
def api():
    if request.method == 'GET':
        return 'json.dumps(data)'

    if request.method == 'PUT':
        data_to_update = request.form['data']

        return str(data_to_update)


    
        
        


if __name__ =='__main__':
    app.run(debug=True)