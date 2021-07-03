from flask import Flask, jsonify
from flask import request, Response
from flask_pymongo import PyMongo
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://juanlad1221:yonome1221@clustershool-widaw.mongodb.net/db_app_profes_iar?retryWrites=true"
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def api():
    if request.method  == 'GET':
        materias = mongo.db.materias.find({})
        result = json_util.dumps(materias)
        return Response(result, mimetype='application/json')

    






#Not found
@app.errorhandler(404)
def not_found(error = None):
    response = jsonify({
        'message':'Recourse not found: ' + request.url,
        'status':404
    }) 
    response.status_code = 404  
    return response 
        


if __name__ =='__main__':
    app.run(debug=True, port=5000)