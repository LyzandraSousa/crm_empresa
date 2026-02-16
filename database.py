import sqlite3
from werkzeug.security import generate_password_hash

def conectar():
    return sqlite3.connect("crm.db")

def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            senha TEXT,
            nivel TEXT
        )
    """)
    conn.commit()
    conn.close()

def criar_usuario(username, senha, nivel="vendedor"):
    conn = conectar()
    cursor = conn.cursor()
    senha_hash = generate_password_hash(senha)
    try:
        cursor.execute("INSERT INTO usuarios (username, senha, nivel) VALUES (?, ?, ?)",
                       (username, senha_hash, nivel))
    except sqlite3.IntegrityError:
        pass
    conn.commit()
    conn.close()

def criar_admin_padrao():
    criar_usuario("admin", "1234", "admin")

def buscar_usuario(username):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, senha, nivel FROM usuarios WHERE username=?", (username,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def criar_tabela_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            servico TEXT,
            origem TEXT,
            fechou INTEGER,
            data_contato TEXT,
            valor REAL,
            usuario_id INTEGER,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_cliente(dados, usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes
        (nome, telefone, email, servico, origem, fechou, data_contato, valor, usuario_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (*dados, usuario_id))
    conn.commit()
    conn.close()

def listar_clientes(usuario_id, nivel):
    conn = conectar()
    cursor = conn.cursor()
    if nivel == "admin":
        cursor.execute("SELECT * FROM clientes")
    else:
        cursor.execute("SELECT * FROM clientes WHERE usuario_id=?", (usuario_id,))
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def metricas_dashboard(usuario_id, nivel):
    conn = conectar()
    cursor = conn.cursor()
    if nivel == "admin":
        cursor.execute("SELECT COUNT(*) FROM clientes")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE fechou=1")
        fechados = cursor.fetchone()[0]
        cursor.execute("SELECT SUM(valor) FROM clientes WHERE fechou=1")
        faturamento = cursor.fetchone()[0]
    else:
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE usuario_id=?", (usuario_id,))
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE fechou=1 AND usuario_id=?", (usuario_id,))
        fechados = cursor.fetchone()[0]
        cursor.execute("SELECT SUM(valor) FROM clientes WHERE fechou=1 AND usuario_id=?", (usuario_id,))
        faturamento = cursor.fetchone()[0]
    conn.close()
    faturamento = faturamento if faturamento else 0
    taxa = (fechados / total * 100) if total > 0 else 0
    return total, fechados, faturamento, round(taxa,2)

def metricas_dashboard_mes(usuario_id, nivel, mes):
    conn = conectar()
    cursor = conn.cursor()
    like_mes = mes + "%"
    if nivel == "admin":
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE data_contato LIKE ?", (like_mes,))
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE fechou=1 AND data_contato LIKE ?", (like_mes,))
        fechados = cursor.fetchone()[0]
        cursor.execute("SELECT SUM(valor) FROM clientes WHERE fechou=1 AND data_contato LIKE ?", (like_mes,))
        faturamento = cursor.fetchone()[0]
    else:
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE usuario_id=? AND data_contato LIKE ?", (usuario_id, like_mes))
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE fechou=1 AND usuario_id=? AND data_contato LIKE ?", (usuario_id, like_mes))
        fechados = cursor.fetchone()[0]
        cursor.execute("SELECT SUM(valor) FROM clientes WHERE fechou=1 AND usuario_id=? AND data_contato LIKE ?", (usuario_id, like_mes))
        faturamento = cursor.fetchone()[0]
    conn.close()
    faturamento = faturamento if faturamento else 0
    taxa = (fechados / total * 100) if total > 0 else 0
    return total, fechados, faturamento, round(taxa,2)
