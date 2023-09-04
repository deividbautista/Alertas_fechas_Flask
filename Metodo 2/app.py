from flask import Flask, render_template
from datetime import date, timedelta

app = Flask(__name__)

# Lista arbitraria de procesos con fechas de inicio y fecha límite
procesos = [
    {"nombre": "Proceso 1", "fecha_inicio": date(2023, 9, 1), "fecha_limite": date(2023, 9, 10)},
    {"nombre": "Proceso 2", "fecha_inicio": date(2023, 8, 25), "fecha_limite": date(2023, 9, 15)},
    {"nombre": "Proceso 3", "fecha_inicio": date(2023, 9, 3), "fecha_limite": date(2023, 9, 5)},
    {"nombre": "Proceso 4", "fecha_inicio": date(2023, 8, 28), "fecha_limite": date(2023, 9, 25)},
]

umbral_maximo_dias = 30

for proceso in procesos:
    diferencia = proceso["fecha_limite"] - proceso["fecha_inicio"]
    
    progreso = 1.0 - min(diferencia.days / umbral_maximo_dias, 1.0)
    
    # Redondear el valor de progreso a un número entero
    proceso["diferencia_dias"] = diferencia.days
    proceso["progreso"] = round(progreso * 100)

    
# Ruta para mostrar la lista de procesos
@app.route('/')
def lista_de_procesos():
    # Obtener la fecha actual
    hoy = date.today()

    return render_template('index.html', procesos=procesos, hoy=hoy)

if __name__ == '__main__':
    app.run(debug=True, port=3040)
