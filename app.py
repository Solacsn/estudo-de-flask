from flask import Flask, render_template, request, url_for, redirect
from database import jogos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", jogos=jogos)


@app.route("/listar-jogos/")
def listar_jogos():
    return render_template("listar_jogos.html", jogos=jogos)

@app.route("/criar/jogo/", methods=["GET", "POST"])
def cadastrar_jogo():
    if request.method == "POST":
        nome = request.form["nome"]
        ano = request.form["ano"]
        jogos.append({"nome": nome, "ano": int(ano)})
        return redirect(url_for("listar_jogos"))
    else:
        return render_template("cadastrar_jogo.html")
