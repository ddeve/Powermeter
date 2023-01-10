# Powermeter Challenge


### Instalación

En un entorno con Python 3.8 

Descargar el repositorio en una carpeta

```bash
git clone https://github.com/ddeve/Powermeter.git
```

Entrar a la carpeta Powermeter, crear y activar el entorno virtual

```bash
cd Powermeter
python3 -m venv venv
source venv/bin/activate
```

Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Ejecución

Ejecutar el proyecto de django

```bash
python3 powermeterChallenge/manage.py runserver
```

Con esto ya estara corriendo el servidor en  http://127.0.0.1:8000/

##### Se creó el proyecto *core* con todo lo solicitado el ejercicio 1.

Los endpoints son los siguientes:

* Obtener todos los medidores : GET http://127.0.0.1:8000/api/meter/
* Obtener un medidor por id : GET http://127.0.0.1:8000/api/meter/{meter_id}
* Crear un nuevo medidor POST http://127.0.0.1:8000/api/meter/

	dentro del Body pasar el json:

```json
{
	"code": "a1234",
	"name": "Medidor N°"
}
```

* Obtener todas las mediciones: GET http://127.0.0.1:8000/api/measurement/
* Obtener una medición por id: GET http://127.0.0.1:8000/api/measurement/{measurement_id}
* Crear una nueva medición POST http://127.0.0.1:8000/api/measurement/

	Dentro del body pasar el json:

```json
{
	"meter": "1",
	"consumption": "23",
	"timestamp": "2023-01-10T12:55:04Z"
}
```

* Obtener la medición de máximo consumo de un medidor: 
	GET http://127.0.0.1:8000/api/meter/{meter_id}/get_max_consumption/

* Obtener la medición de mínimo consumo de un medidor: 
	GET http://127.0.0.1:8000/api/meter/{meter_id}/get_min_consumption/

* Obtener el total de consumo de un medidor: 
	GET http://127.0.0.1:8000/api/meter/{meter_id}/get_total_consumption/

* Obtener el promedio de consumo de un medidor: GET 
	GET http://127.0.0.1:8000/api/meter/{meter_id}/get_avg_consumption/



##### El ejercicio 2 está resuelto dentro del proyecto en el archivo ejercicio2.py


```python
import json


repetidos = [1, 2, 3, "1", "2", "3", 3, 4, 5]
r = [1, "5", 2, "3"]
d_str = '{"valor":125.3,"codigo":123}'

# 1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.
no_repetidos = [valor for valor in repetidos if repetidos.count(valor) == 1]

# 2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
valores_comunes = [valor for valor in repetidos if valor in r]

# 3. Transforme ‘d_str’ en un diccionario.
dict_d_str = json.loads(d_str)
```
