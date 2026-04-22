from flask import Flask, request

app = Flask(__name__)

buques = [
    {"id":1,"nombre":"Ocean Star","descripcion":"Carga de maiz","categoria":"granelero","latitud":13.20,"longitud":-91.40},
    {"id":2,"nombre":"Blue Wave","descripcion":"Combustible","categoria":"tanquero","latitud":13.45,"longitud":-91.10},
    {"id":3,"nombre":"Pacific King","descripcion":"Contenedores","categoria":"portacontenedor","latitud":13.05,"longitud":-90.95},
    {"id":4,"nombre":"Sea Power","descripcion":"Asistencia portuaria","categoria":"remolcador","latitud":13.60,"longitud":-90.80},
    {"id":5,"nombre":"Atlantic Sun","descripcion":"Carga trigo","categoria":"granelero","latitud":13.30,"longitud":-91.70}
]

@app.route("/")
def inicio():
    return """
    <html>
    <head>
        <title>Sistema de Buques</title>
        <style>
            body{
                margin:0;
                font-family:Arial;
                background:linear-gradient(135deg,#0f172a,#1d4ed8);
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
            }

            .caja{
                background:white;
                width:480px;
                padding:40px;
                border-radius:20px;
                text-align:center;
                box-shadow:0 10px 30px rgba(0,0,0,0.25);
            }

            h1{color:#1e3a8a;}

            a{
                display:block;
                background:#2563eb;
                color:white;
                padding:14px;
                margin:10px 0;
                border-radius:12px;
                text-decoration:none;
                font-weight:bold;
            }

            a:hover{
                background:#1d4ed8;
            }
        </style>
    </head>

    <body>
        <div class="caja">
            <h1>🚢 Sistema de Buques</h1>
            <p>Monitoreo Geoespacial Marítimo</p>

            <a href="/buques">🚢 Ver Buques</a>
            <a href="/mapa">🗺️ Ver Mapa</a>
            <a href="/agregar">➕ Registrar Buque</a>
            <a href="/categoria/granelero">🌾 Graneleros</a>
            <a href="/categoria/tanquero">⛽ Tanqueros</a>
            <a href="/categoria/portacontenedor">📦 Portacontenedor</a>
            <a href="/cerca/13.20/-91.40/0.50">📍 Cercanos</a>
        </div>
    </body>
    </html>
    """


@app.route("/buques")
def ver_buques():

    html = """
    <html>
    <head>
    <style>
    body{font-family:Arial;background:#f1f5f9;padding:30px;}
    h1{text-align:center;color:#1e3a8a;}

    .card{
        background:white;
        padding:20px;
        margin:15px;
        border-radius:15px;
        box-shadow:0 5px 15px rgba(0,0,0,0.1);
    }

    a{
        display:block;
        width:180px;
        margin:auto;
        text-align:center;
        padding:12px;
        background:#2563eb;
        color:white;
        border-radius:10px;
        text-decoration:none;
    }
    </style>
    </head>

    <body>
    <h1>🚢 Buques Registrados</h1>
    """

    for x in buques:
        html += f"""
        <div class='card'>
            <h2>{x["nombre"]}</h2>
            <p>{x["descripcion"]}</p>
            <p><b>Tipo:</b> {x["categoria"]}</p>
            <p><b>Ubicación:</b> {x["latitud"]}, {x["longitud"]}</p>
        </div>
        """

    html += "<a href='/'>⬅ Volver</a></body></html>"

    return html


@app.route("/mapa")
def mapa():

    marcadores = ""

    for x in buques:
        marcadores += f"""
        L.marker([{x["latitud"]},{x["longitud"]}]).addTo(map)
        .bindPopup("<b>{x['nombre']}</b><br>{x['descripcion']}<br>{x['categoria']}");
        """

    return f"""
    <html>
    <head>
    <link rel="stylesheet"
    href="https://unpkg.com/leaflet/dist/leaflet.css"/>

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

    <style>
    body{{margin:0;}}
    #map{{height:100vh;}}
    </style>
    </head>

    <body>

    <div id="map"></div>

    <script>
    var map = L.map('map').setView([13.30,-91.10],8);

    L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png').addTo(map);

    {marcadores}
    </script>

    </body>
    </html>
    """


@app.route("/agregar", methods=["GET","POST"])
def agregar():

    if request.method == "POST":

        nuevo = {
            "id": len(buques)+1,
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "categoria": request.form["categoria"],
            "latitud": float(request.form["latitud"]),
            "longitud": float(request.form["longitud"])
        }

        buques.append(nuevo)

        return """
        <html><body style='font-family:Arial;text-align:center;padding:60px;background:#f1f5f9;'>
        <h1>✅ Buque agregado correctamente</h1>
        <a href='/buques'>Ver Buques</a>
        </body></html>
        """

    return """
    <html>
    <body style='font-family:Arial;background:#0f172a;
    display:flex;justify-content:center;align-items:center;height:100vh;'>

    <div style='background:white;padding:40px;border-radius:20px;width:420px;'>

    <h1 style='text-align:center;'>🚢 Registrar Buque</h1>

    <form method='post'>

    Nombre:<br><input name='nombre' style='width:100%;padding:10px'><br><br>

    Descripción:<br><input name='descripcion' style='width:100%;padding:10px'><br><br>

    Tipo:<br><input name='categoria' style='width:100%;padding:10px'><br><br>

    Latitud:<br><input name='latitud' style='width:100%;padding:10px'><br><br>

    Longitud:<br><input name='longitud' style='width:100%;padding:10px'><br><br>

    <button style='width:100%;padding:12px;background:#2563eb;
    color:white;border:none;border-radius:10px;'>Guardar</button>

    </form>

    <br><a href='/'>⬅ Volver</a>

    </div>
    </body>
    </html>
    """


@app.route("/categoria/<tipo>")
def categoria(tipo):

    resultado = [x for x in buques if x["categoria"] == tipo]

    html = f"""
    <html>
    <body style='font-family:Arial;background:#f1f5f9;padding:30px;'>

    <h1>🚢 Categoría: {tipo}</h1>
    """

    for x in resultado:
        html += f"""
        <div style='background:white;padding:20px;margin:15px;
        border-radius:15px;box-shadow:0 5px 15px rgba(0,0,0,0.1);'>

        <h2>{x["nombre"]}</h2>
        <p>{x["descripcion"]}</p>
        <p>{x["latitud"]}, {x["longitud"]}</p>

        </div>
        """

    html += "<a href='/'>⬅ Volver</a></body></html>"

    return html


@app.route("/cerca/<lat>/<lon>/<radio>")
def cerca(lat, lon, radio):

    lat = float(lat)
    lon = float(lon)
    radio = float(radio)

    resultado = []

    for x in buques:
        if abs(x["latitud"]-lat) <= radio and abs(x["longitud"]-lon) <= radio:
            resultado.append(x)

    html = """
    <html>
    <body style='font-family:Arial;background:#eef2ff;padding:30px;'>

    <h1>📍 Buques Cercanos</h1>
    """

    for x in resultado:
        html += f"""
        <div style='background:white;padding:20px;margin:15px;border-radius:15px;'>
            <h2>{x["nombre"]}</h2>
            <p>{x["descripcion"]}</p>
            <p>{x["categoria"]}</p>
            <p>{x["latitud"]}, {x["longitud"]}</p>
        </div>
        """

    if len(resultado) == 0:
        html += "<h2>No se encontraron buques cercanos</h2>"

    html += "<a href='/'>⬅ Volver</a></body></html>"

    return html


app.run(host="0.0.0.0", port=5000)
