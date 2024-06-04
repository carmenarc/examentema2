# EXAMEN MODULO 2
Este es el Readme del examen teórico del módulo 2.
Acontinuación intentaré guiarte para que puedas explorar mis actividades.



### 1.: CONFIGURACIÓN DEL ENTORNO DE DESARROLLO.

1. **Crea una instancia EC2**:
   - Ve a `Servicios > EC2` y selecciona `Lanzar instancia`.
   - Elige la AMI de `Amazon Linux 2`.
   - Selecciona el tipo de instancia, `t3.small`
   - Crea un nuevo par de claves o usa uno existente y guarda el archivo `.pem`.
   - Configura el almacenamiento predeterminado y haz clic en `Revisar y lanzar`.

2. **Configura los grupos de seguridad**:
   - En `EC2 > Grupos de seguridad`.
   - Selecciona el grupo de seguridad asociado a tu instancia.
   - Añade una regla de entrada para permitir el tráfico puerto 5000 y el puerto 8080.
   - RDS Puerto: 3306, Motor MySQL

3. **Conéctate a la instancia EC2**:
   - Desde un Cloud9 nos conectamos a nuestro EC2
   - Tenemos que tener el `archivo.pem` de nuestro EC2 en Cloud9. Lo puedes encontrar en descargas, abres un archivo y lo pegas y lo nombras. Ej. Claves.pem
     
     ```sh
     chmod 600 archivo.pem
     ssh -i claves.pem ec2-user@54.175.69.68
     ```

### 2. INSTALA Y CONFIGURA PYTHON

1. **Actualiza el sistema**:
   ```sh
   sudo yum update 
   ```

2. **Instala Python**:
   ```sh
   sudo yum install python3 -y
   ```

3. **Instala pip**:
   ```sh
   sudo yum install python3-pip -y
   ```

## DESARROLLO DE UNA APLICACIÓN WEB

### 1. CREA UNA APLICACIÓN WEB CON FLASK EN PYTHON

1. **Instala Flask**:
   ```sh
   pip3 install Flask
   ```

2. **Crea la estructura del proyecto**:
   ```sh
   mkdir my_flask_app
   cd my_flask_app
   ```

3. **Crea los archivos**
Debe quedar como abajo:

```
.
├── app.py
└── templates
    ├── formulario.html
    └── presentacion.html
```

### Código de `app.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def presentacion():
    return render_template('presentacion.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        altura = request.form['altura']
        return f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Altura: {altura}'
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

### Código de `presentacion.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Examen del Modulo 2</title>
    <style>
        body {
            text-align: center;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>Bienvenido</h1>
    <p>Para este examen 04/06/2024 es para mostrar el uso de Flask.</p>
    <p>Haga clic en el botón para ir al formulario:</p>
    <a href="/formulario"><button>Ir al Formulario</button></a>
</body>
</html>
```

### Código de `formulario.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Formulario 002</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            font-family: Arial, sans-serif;
        }
        form {
            text-align: center;
            margin-top: 20px;
        }
        label {
            margin-bottom: 10px;
            display: block;
        }
        input {
            margin-bottom: 10px;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <form method="POST" action="/formulario">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br>
        <label for="apellido">Apellido:</label>
        <input type="text" id="apellido" name="apellido" required><br>
        <label for="edad">Edad:</label>
        <input type="number" id="edad" name="edad" required><br>
        <label for="altura">Altura:</label>
        <input type="number" id="altura" name="altura" required><br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>

```



5. **Ejecutar la aplicación**:
   ```sh
   sudo python3 app.py
   ```

   ```sh
   http://localhost:8080/
   ```

## 3: PRUEBAS Y DEPURACIÓN

### Paso 1: Desarrollo de Casos de Prueba

1. **Crear el archivo `test_app.py`**:
   ```python
   import unittest
   from app import app

   class TestApp(unittest.TestCase):

    def setUp(self):
        # Configurar la aplicación antes de cada prueba
        self.app = app.test_client()
        self.app.testing = True

    def test_presentacion(self):
        # Probar la página de presentación
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenido', response.data)

    def test_formulario(self):
        # Probar el formulario
        response = self.app.post('/formulario', data=dict(nombre='John', apellido='Doe', edad='30', altura='180'))
        self.assertIn(b'Nombre: John, Apellido: Doe, Edad: 30, Altura: 180', response.data)

    def test_ruta_invalida(self):
        # Probar una ruta no válida
        response = self.app.get('/ruta_invalida')
        self.assertEqual(response.status_code, 404)

   if __name__ == '__main__':
    unittest.main()

   ```

### Paso 2: Ejecución de Pruebas

1. **Ejecutar las pruebas**:
   ```sh
   python3 test_app.py
   ```
