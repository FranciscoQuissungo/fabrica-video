from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "API de Vídeo Online!"

@app.route("/health")
def health():
    return {"status": "ok"}

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8000)
