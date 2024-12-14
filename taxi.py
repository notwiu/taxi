import tkinter as tk
from tkinter import messagebox
import pandas as pd

def calcular_preco(bairro):
    preços = {
        'Bayeux' : 150,
        'Altiplano' : 100,
        'Centro' : 50,
        'Valentina' : 20,
    }
    return preços.get(bairro, 50)

def gerar_planilha(dados, arquivo):
    df = pd.DataFrame(dados)
    df.to_excel(arquivo, index=False)

def finalizar_dados():
    if not lista_corridas:
        messagebox.showwarning("Atenção", "Nenhuma corrida foi registrada, por favor coloque os dados e tente novamente!")
        return
    gerar_planilha(lista_corridas, "planilha_corridas.xlsx")
    messagebox.showinfo("Sucesso", "Planilha já foi gerada com sucesso")

def proxima_corrida():
    destino = entrada_destino.get()
    bairro = entrada_bairro.get()
    voucher = entrada_voucher.get()

    if not destino and not bairro and not voucher:
        messagebox.showwarning("Aviso", "Por favor, coloque pelo menos um campo para conseguir prosseguir.")
        return

    preco = calcular_preco(bairro)

    dados = {
        "Voucher": voucher if voucher else "Não informado",
        "Bairro": bairro if bairro else "Não informado",
        "Preço (R$)": preco,
        "Destino": destino if destino else "Não Informado",
    }

    lista_corridas.append(dados)

    entrada_destino.delete(0, tk.END)
    entrada_bairro.delete(0, tk.END)
    entrada_voucher.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Corrida adicionada! Pode adicionar outra.")

root = tk.Tk()
root.title("Planilhas de Corridas")

lista_corridas = []

tk.Label(root, text="Destino (Rua)").grid(row=0, column=0, padx=10, pady=5)
entrada_destino = tk.Entry(root, width=30)
entrada_destino.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Bairro").grid(row=2, column=0, padx=10, pady=5)
entrada_bairro = tk.Entry(root, width=30)
entrada_bairro.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Número do Voucher").grid(row=3, column=0, padx=10, pady=5)
entrada_voucher = tk.Entry(root, width=30)
entrada_voucher.grid(row=3, column=1, padx=10, pady=5)

botao_proxima = tk.Button(root, text="Próxima", command=proxima_corrida)
botao_proxima.grid(row=4, column=0, pady=20)

botao_finalizar = tk.Button(root, text="Finalizar", command=finalizar_dados)
botao_finalizar.grid(row=4, column=1, pady=20)

root.mainloop()
