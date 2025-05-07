from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Bienvenido a PsicoConecta!</h1><p>Plataforma digital de salud mental en Colombia.</p>"

if __name__ == '__main__':
    app.run(debug=True)
