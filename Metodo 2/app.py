from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import date, timedelta
from random import sample
from flask_mysqldb import MySQL
from database import config
import os

app = Flask(__name__)

mysql = MySQL(app)

# def datosUsuarios():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM users")
#     myresult = cursor.fetchall()
#     #Convertir los datos a diccionario
#     insertObject = []
#     columnNames = [column[0] for column in cursor.description]
#     for record in myresult:
#         insertObject.append(dict(zip(columnNames, record)))
#     cursor.close()  

#     dataUser=insertObject  
#     return dataUser

# # -------------------------------------------------------------------
# # Función para obtener los datos de los usuarios.
# def datos_proceso():
#     cursor = mysql.connection.cursor()
#     query = """
#     SELECT p.*, GROUP_CONCAT(u.id) AS id_usuario, GROUP_CONCAT(u.fullname) AS nombre_usuario
#     FROM procesos p
#     LEFT JOIN asignaciones a ON p.id_proceso = a.id_proceso
#     LEFT JOIN users u ON a.id = u.id
#     GROUP BY p.id_proceso;
#     """
#     cursor.execute(query)
#     data = cursor.fetchall()
#     dataUser = datosUsuarios()

#     # Procesa los resultados para formar una estructura de datos más adecuada
#     processed_data = []
#     for row in data:
#         proceso = {
#             "id_proceso": row[0],  # Usar el índice numérico correspondiente
#             "Titulo": row[1],      # Usar el índice numérico correspondiente
#             "Descripcion": row[2], # Usar el índice numérico correspondiente
#             "fecha_inicio": row[3], # Usar el índice numérico correspondiente
#             "fecha_limite": row[4], # Usar el índice numérico correspondiente
#             "nombre_usuario": row[6].split(",") if row[6] is not None else [],
#             "id_usuario": row[5].split(",") if row[5] is not None else [],
#         }
#         processed_data.append(proceso)

#     cursor.close()  # Cierra el cursor aquí
#     hoy = date.today()

#     return processed_data, hoy, dataUser

# # -------------------------------------------------------------------
# # Lista arbitraria de procesos con fechas de inicio y fecha límite
# procesos = [
#     {"nombre": "Proceso 1", "fecha_inicio": date(2023, 9, 1), "fecha_limite": date(2023, 9, 10)},
#     {"nombre": "Proceso 2", "fecha_inicio": date(2023, 8, 25), "fecha_limite": date(2023, 9, 15)},
#     {"nombre": "Proceso 3", "fecha_inicio": date(2023, 9, 3), "fecha_limite": date(2023, 9, 5)},
#     {"nombre": "Proceso 4", "fecha_inicio": date(2023, 8, 28), "fecha_limite": date(2023, 10, 25)},
# ]

# umbral_maximo_dias = 30

# for proceso in procesos:
#     diferencia = proceso["fecha_limite"] - proceso["fecha_inicio"]
    
#     progreso = 1.0 - min(diferencia.days / umbral_maximo_dias, 1.0)

#     if progreso <= 0:
#         progreso = 0.03
#     # Redondear el valor de progreso a un número entero
#     proceso["diferencia_dias"] = diferencia.days
#     proceso["progreso"] = round(progreso * 100)


# @app.route("/")
# def home():
#     hoy = date.today()
#     procesosM = datos_proceso()
#     return render_template('index.html', procesos=procesos, hoy=hoy, procesosM = procesosM )

def datosUsuarios():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()  

    dataUser=insertObject  
    return dataUser


def datos_proceso():
    cursor = mysql.connection.cursor()
    query = """
    SELECT p.*, GROUP_CONCAT(u.id) AS id_usuario, GROUP_CONCAT(u.fullname) AS nombre_usuario
    FROM procesos p
    LEFT JOIN asignaciones a ON p.id_proceso = a.id_proceso
    LEFT JOIN users u ON a.id = u.id
    GROUP BY p.id_proceso;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    # Procesa los resultados para formar una estructura de datos más adecuada
    processed_data = []
    for row in data:
        proceso = {
            "id_proceso": row[0],  # Usar el índice numérico correspondiente
            "Titulo": row[1],      # Usar el índice numérico correspondiente
            "Descripcion": row[2], # Usar el índice numérico correspondiente
            "fecha_inicio": row[3], # Usar el índice numérico correspondiente
            "fecha_limite": row[4], # Usar el índice numérico correspondiente
            "nombre_usuario": row[6].split(",") if row[6] is not None else [],
            "id_usuario": row[5].split(",") if row[5] is not None else [],
        }
        processed_data.append(proceso)

    cursor.close()  # Cierra el cursor aquí
    return processed_data


# Lista arbitraria de procesos con fechas de inicio y fecha límite
procesos = [
    {"nombre": "Proceso 1", "fecha_inicio": date(2023, 9, 1), "fecha_limite": date(2023, 9, 10)},
    {"nombre": "Proceso 2", "fecha_inicio": date(2023, 8, 25), "fecha_limite": date(2023, 9, 15)},
    {"nombre": "Proceso 3", "fecha_inicio": date(2023, 9, 3), "fecha_limite": date(2023, 9, 5)},
    {"nombre": "Proceso 4", "fecha_inicio": date(2023, 8, 28), "fecha_limite": date(2023, 10, 25)},
]

umbral_maximo_dias = 30

# ---------------------------------------------------------------------
for proceso in procesos:
    diferencia = proceso["fecha_limite"] - proceso["fecha_inicio"]
    
    progreso = 1.0 - min(diferencia.days / umbral_maximo_dias, 1.0)

    if progreso <= 0:
        progreso = 0.03
    # Redondear el valor de progreso a un número entero
    proceso["diferencia_dias"] = diferencia.days
    proceso["progreso"] = round(progreso * 100)
# -------------------------------------------------------------------

@app.route("/")
def home():
    hoy = date.today()
    dataUser = datosUsuarios()
    processed_data = datos_proceso()

    for processed in processed_data:
        diferencia = processed["fecha_limite"] - processed["fecha_inicio"]
            
        progreso = 1.0 - min(diferencia.days / umbral_maximo_dias, 1.0)

        if progreso <= 0:
            progreso = 0.03
            # Redondear el valor de progreso a un número entero
        processed["diferencia_dias"] = diferencia.days
        processed["progreso"] = round(progreso * 100)
        
    return render_template('index.html', procesos=procesos, hoy=hoy, data=processed_data)


# Condicional para dar inicialización al proyecto.
if __name__ == '__main__':  
    app.config.from_object(config["development"]) 
    app.run(debug=True, port=4040)
