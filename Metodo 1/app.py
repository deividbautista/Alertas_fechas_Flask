# El presente proyecto data de un modelo para alertar sobre la 
# proximidad por fechas implementado de proyectos que necesiten 
# de distintas formas de alertar o visualizar la progreción del tiempo

# Todos los derechos reservados.
# Copyright © 2023 Deivid Edwuar Bautista Ocampo - Jhonatan David Florez Useche

# Importar los distintos modulos que utilizaremos en este metodo número 1
from flask import Flask, render_template
from datetime import date, timedelta

app = Flask(__name__)

# Lista arbitraria de procesos con fechas límite
procesos = [
    {"nombre": "Proceso 1", "fecha_limite": date(2023, 9, 10)},
    {"nombre": "Proceso 2", "fecha_limite": date(2023, 9, 15)},
    {"nombre": "Proceso 3", "fecha_limite": date(2023, 9, 5)},
    {"nombre": "Proceso 4", "fecha_limite": date(2023, 9, 25)},
    {"nombre": "Proceso 4", "fecha_limite": date(2023, 9, 3)},
]

# Ruta para mostrar la lista de procesos
@app.route('/')
def lista_de_procesos():
    # Obtener la fecha actual
    hoy = date.today()

    # Calcular la fecha próxima (por ejemplo, 7 días después de hoy)
    proximo = hoy + timedelta(days=4)

    return render_template('index.html', procesos=procesos, hoy=hoy, proximo=proximo)

if __name__ == '__main__':
    app.run(debug=True, port=3030)

