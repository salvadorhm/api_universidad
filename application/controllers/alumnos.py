import web # pip install web.py
import app # app.py
import csv
import json

class Alumnos:

    def __init__(self):
        pass

    '''
    http://localhost:8080/alumnos?action=get&token=1234
    '''
    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234":
                result = {} # crear diccionario vacio
                result['status'] = "200 Ok"
                return json.dumps(result) # Parsea el diccionario a json
            else:
                result = {} # crear diccionario vacio
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            result = {} # crear diccionario vacio
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)
