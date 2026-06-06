import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    messagebox.showinfo("Cadastro", f"{nome} e {idade} cadastrado(a) com sucesso!")

janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("450x400")
janela.configure(bg="#F5F5F5") 

titulo = tk.Label(janela, text="UNIESP",font=("Segoe UI", 24, "bold"), fg="#D71920", bg="#F5F5F5")
titulo.pack(pady=(20, 5)) #20 a cima e 5 abaixo

subtitulo = tk.Label(janela,text="Sistema de Cadastro", font=("Segoe UI", 11), fg="#444444", bg="#F5F5F5")
subtitulo.pack()
frame = tk.Frame(janela, bg="white", bd=1,relief="solid")
frame.pack(padx=20, pady=20, fill="both", expand=True)
tk.Label(frame, text="Nome:", font=("Segoe UI", 11), bg="white", fg="#333333").grid(row=0, column=0, padx=15, pady=20)
tk.Label(frame, text="Idade:", font=("Segoe UI", 11), bg="white", fg="#333333").grid(row=1, column=0, padx=15, pady=20)
entry_nome = tk.Entry(frame,width=30,font=("Segoe UI", 11))
entry_nome.grid(row=0, column=1, padx=15, pady=20)
entry_idade = tk.Entry(frame,width=30,font=("Segoe UI", 11))
entry_idade.grid(row=1, column=1, padx=15, pady=20)

btn_cadastrar = tk.Button(frame,text="Cadastrar",command=cadastrar,font=("Segoe UI", 11, "bold"), bg="#D71920",fg="white",
width=20,cursor="hand2").grid(row=2, column=0, columnspan=2, pady=10, sticky=)
resultado = tk.Label( frame, text="Aguardando cadastro...", font=("Segoe UI", 10), bg="white", fg="#666666")
resultado.grid(row=3, column=0, columnspan=2, pady=10)
janela.mainloop()