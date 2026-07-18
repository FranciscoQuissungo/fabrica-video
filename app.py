from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "API de Vídeo Online!"

@app.route("/health")
def health():
    return {"status": "ok"}

if name == "main":
    app.run(host="0.0.0.0", port=8000)
