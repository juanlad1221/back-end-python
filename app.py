from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def api():
    if request.method == 'GET':
        return jsonify({'msg':'1'})

    


    
        
        


if __name__ =='__main__':
    app.run(debug=True, port=5000)