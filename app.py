from flask import Flask, render_template, request, redirect, session, send_file
from werkzeug.security import check_password_hash
from database import (
    criar_tabela_clientes,
    criar_tabela_usuarios,
    criar_admin_padrao,
    cadastrar_cliente,
    listar_clientes,
    criar_usuario,
    buscar_usuario,
    metricas_dashboard,
    metricas_dashboard_mes
)
import pandas as pd
import io

app = Flask(__name__, template_folder="templates")
app.secret_key = "SUA_CHAVE_SECRETA_AQUI"

criar_tabela_usuarios()
criar_tabela_clientes()
criar_admin_padrao()  

@app.route("/")
def home():
    return redirect("/login")  

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]
        usuario = buscar_usuario(username)
        if usuario and check_password_hash(usuario[1], senha):
            session["usuario_id"] = usuario[0]
            session["username"] = username
            session["nivel"] = usuario[2]
            return redirect("/dashboard")
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if "usuario_id" not in session:
        return redirect("/login")
    if session["nivel"] != "admin":
        return "Acesso negado"

    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]
        nivel = request.form["nivel"]
        criar_usuario(username, senha, nivel)
        return redirect("/dashboard")
    return render_template("registrar.html")

@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect("/login")
    
    mes = request.args.get("mes")
    if mes:
        total, fechados, faturamento, taxa = metricas_dashboard_mes(session["usuario_id"], session["nivel"], mes)
    else:
        total, fechados, faturamento, taxa = metricas_dashboard(session["usuario_id"], session["nivel"])

    labels = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    data = [5, 8, 3, 7, 2, 6, 4, 9, 5, 3, 6, 7]

    return render_template("dashboard.html",
                           total=total,
                           fechados=fechados,
                           faturamento=faturamento,
                           taxa=taxa,
                           mes=mes or "",
                           labels=labels,
                           data=data)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if "usuario_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        dados = (
            request.form["nome"],
            request.form["telefone"],
            request.form["email"],
            request.form["servico"],
            request.form["origem"],
            int(request.form["fechou"]),
            request.form["data_contato"],
            float(request.form["valor"] or 0)
        )
        cadastrar_cliente(dados, session["usuario_id"])
        return redirect("/listar")
    
    return render_template("cadastrar.html")

@app.route("/listar")
def listar():
    if "usuario_id" not in session:
        return redirect("/login")
    
    clientes = listar_clientes(session["usuario_id"], session["nivel"])
    return render_template("listar.html", clientes=clientes)

@app.route("/relatorio")
def relatorio():
    if "usuario_id" not in session:
        return redirect("/login")
   
    clientes = listar_clientes(session["usuario_id"], session["nivel"])

    df = pd.DataFrame(clientes, columns=[
        "ID", "Nome", "Telefone", "Email", "Serviço", "Origem", "Fechou", "Data Contato", "Valor", "Usuário"
    ])
    
    output = io.BytesIO()
    df.to_excel(output, index=False, sheet_name="Clientes")
    output.seek(0) 
    
    return send_file(
        output,
        as_attachment=True,
        download_name="relatorio_clientes.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
