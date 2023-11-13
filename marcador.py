from flask import Flask
from flask import request, Response
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


venezuela = '0'
ecuador = '0'

@app.route('/puntaje', methods = ['POST', 'GET'])
def actualizarPuntaje():
    if request.method == 'POST':
        global venezuela
        venezuela = request.form['venezuela']
        global ecuador
        ecuador = request.form['ecuador']
        print('post')
        return 'test'
    else:
        marcador = json.dumps(
            {
                "ecuador": ecuador,
                "venezuela": venezuela
            }
        )
        return marcador

if __name__ == '__main__':
    app.run(debug = False)
