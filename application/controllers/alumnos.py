import web # pip install web.py
import app # app.py
import csv # CSV parser
import json # json parser

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
                if data['action'] == 'get':
                    # call action_get()
                    result = self.actionGet()
                    return json.dumps(result)
                else:
                    result = {} # crear diccionario vacio
                    result['status'] = "Command not found"
                    return json.dumps(result) # Parsea el diccionario a json
            else:
                result = {} # crear diccionario vacio
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            result = {} # crear diccionario vacio
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)

    @staticmethod
    def actionGet():
        print("action_get init")
        try:
            result = {} # crear diccionario vacio
            result['status'] = "200 Ok"
            with open('static/csv/alumnos.csv','r') as csvfile:
                reader = csv.DictReader(csvfile) # toma la 1er fila para los nombres
                alumnos = []
                for row in reader:
                    fila = {}
                    fila['matricula']=(row['matricula'])
                    fila['nombre']=(row['nombre'])
                    fila['primer_apellido']=(row['primer_apellido'])
                    fila['segundo_apellido']=(row['segundo_apellido'])
                    fila['carrera']=(row['carrera'])
                    alumnos.append(fila)
                result['alumnos'] = alumnos
            return result # Parsea el diccionario a json
        except  Exception as e:
            result = {}
            result['status'] = "Error"
            return result
