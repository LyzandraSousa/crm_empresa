import tkinter as tk
from tkinter import messagebox
import database

def cadastrar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    valor = entry_valor.get()
    data = entry_data.get()
    fechou = var_fechou.get()

    if nome == "" or telefone == "" or valor == "" or data == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    database.adicionar_cliente(
        nome,
        telefone,
        float(valor),
        data,
        fechou
    )

    messagebox.showinfo("Sucesso", "Cliente cadastrado!")

    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_data.delete(0, tk.END)

def listar():
    clientes = database.listar_clientes()
    lista_clientes.delete(0, tk.END)

    for cliente in clientes:
        texto = f"{cliente[1]} | R${cliente[3]} | {cliente[4]}"
        lista_clientes.insert(tk.END, texto)

def relatorio():
    resultado = database.gerar_relatorio()

    total_vendas = resultado[0] if resultado[0] else 0
    faturamento = resultado[1] if resultado[1] else 0

    messagebox.showinfo(
        "Relatório Geral",
        f"Vendas fechadas: {total_vendas}\nFaturamento: R${faturamento}"
    )

def relatorio_mensal():
    mes = entry_mes.get()

    if mes == "":
        messagebox.showwarning("Erro", "Digite o mês no formato YYYY-MM")
        return

    resultado = database.gerar_relatorio_mensal(mes)

    total_vendas = resultado[0] if resultado[0] else 0
    faturamento = resultado[1] if resultado[1] else 0

    messagebox.showinfo(
        "Relatório Mensal",
        f"Mês: {mes}\nVendas: {total_vendas}\nFaturamento: R${faturamento}"
    )

janela = tk.Tk()
janela.title("CRM de Vendas")
janela.geometry("500x600")

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Telefone").pack()
entry_telefone = tk.Entry(janela)
entry_telefone.pack()

tk.Label(janela, text="Valor").pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()

tk.Label(janela, text="Data (YYYY-MM-DD)").pack()
entry_data = tk.Entry(janela)
entry_data.pack()

var_fechou = tk.IntVar()
tk.Checkbutton(janela, text="Venda Fechada", variable=var_fechou).pack()

tk.Button(janela, text="Cadastrar Cliente", command=cadastrar).pack(pady=5)
tk.Button(janela, text="Listar Clientes", command=listar).pack(pady=5)
tk.Button(janela, text="Relatório Geral", command=relatorio).pack(pady=5)

tk.Label(janela, text="Relatório Mensal (YYYY-MM)").pack(pady=5)
entry_mes = tk.Entry(janela)
entry_mes.pack()

tk.Button(janela, text="Gerar Relatório Mensal", command=relatorio_mensal).pack(pady=5)

lista_clientes = tk.Listbox(janela, width=60)
lista_clientes.pack(pady=10)

database.criar_tabela()
janela.mainloop()
