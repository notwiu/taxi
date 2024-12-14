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

def gerar_planilha(dados, arquivo)
    df = pd.DataFrame(dados)
    df.to_excel(arquivo,index=False)

def finalizar_dados():
    if not lista_corridas:
        messagebox.showwarning("Atenção", "Nenhuma corrida foi registrada, por favor coloque os dados e tente novamente!")
        return

gerar_planilha(lista_corridas, "planilha_corridas.xlsx")
messagebox.showinfo("Sucesso", "Planilha já foi gerada com sucesso")

def proxima_corrida():
    destino = entrada_destino.get()
    bairro = entrada_bairro.get()
    vouncher = entrada_vouncher.get()

    if not destino and not bairro and not vouncher:
        messagebox.showwarning("Aviso", "Por favor, coloque pelo menos um campo para conseguir prosseguir.")
        return

preco = calcular_preco(bairro)

dados = {
    "Vouncher": vouncher if vouncher else "Não informado",
    "Bairro": bairro if bairro else "Não informado",
    "Preço (R$)": preco,
    "Destino": destino if destino else "Não Informado",
}

lista_corridas.append(dados)



