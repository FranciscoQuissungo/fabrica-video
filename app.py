from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "Fábrica de Vídeos Online!"

if name == "main":
    app.run(host="0.0.0.0", port=5000)
