import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

pacientes = []
medicos = []
consultas = []

_id_pac = 0
_id_med = 0
_id_con = 0

def novo_id_pac():
    global _id_pac
    _id_pac += 1
    return _id_pac

def novo_id_med():
    global _id_med
    _id_med += 1
    return _id_med

def novo_id_con():
    global _id_con
    _id_con += 1
    return _id_con

def atualizar_combos():
    combo_pac_con["values"] = [f'{p["id"]} - {p["nome"]}' for p in pacientes]
    combo_med_con["values"] = [f'{m["id"]} - {m["nome"]}' for m in medicos]

def cadastrar_paciente():
    nome  = entry_pac_nome.get().strip()
    cpf   = entry_pac_cpf.get().strip()
    nasc  = entry_pac_nasc.get().strip()
    tel   = entry_pac_tel.get().strip()
    email = entry_pac_email.get().strip()
    end   = entry_pac_end.get().strip()

    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome do paciente!")
        return
    if not cpf:
        messagebox.showwarning("Aviso", "Digite o CPF do paciente!")
        return

    pacientes.append({
        "id": novo_id_pac(),
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": nasc,
        "telefone": tel,
        "email": email,
        "endereco": end
    })
    atualizar_combos()
    atualizar_tabela_pacientes()
    messagebox.showinfo("Sucesso", f'Paciente "{nome}" cadastrado!')
    for e in [entry_pac_nome, entry_pac_cpf, entry_pac_nasc,
              entry_pac_tel, entry_pac_email, entry_pac_end]:
        e.delete(0, tk.END)

def editar_paciente():
    sel = tree_pac.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione um paciente para editar!")
        return
    item = tree_pac.item(sel[0])
    id_pac = int(item["values"][0])
    for p in pacientes:
        if p["id"] == id_pac:
            entry_pac_nome.delete(0, tk.END);  entry_pac_nome.insert(0, p["nome"])
            entry_pac_cpf.delete(0, tk.END);   entry_pac_cpf.insert(0, p["cpf"])
            entry_pac_nasc.delete(0, tk.END);  entry_pac_nasc.insert(0, p["data_nascimento"])
            entry_pac_tel.delete(0, tk.END);   entry_pac_tel.insert(0, p["telefone"])
            entry_pac_email.delete(0, tk.END); entry_pac_email.insert(0, p["email"])
            entry_pac_end.delete(0, tk.END);   entry_pac_end.insert(0, p["endereco"])
            pacientes.remove(p)
            atualizar_combos()
            atualizar_tabela_pacientes()
            break

def excluir_paciente():
    sel = tree_pac.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione um paciente para excluir!")
        return
    id_pac = int(tree_pac.item(sel[0])["values"][0])
    if any(c["paciente_id"] == id_pac for c in consultas):
        messagebox.showwarning("Aviso", "Paciente possui consultas vinculadas!")
        return
    global pacientes
    pacientes = [p for p in pacientes if p["id"] != id_pac]
    atualizar_combos()
    atualizar_tabela_pacientes()
    messagebox.showinfo("Sucesso", "Paciente excluído!")

def atualizar_tabela_pacientes():
    tree_pac.delete(*tree_pac.get_children())
    for p in pacientes:
        tree_pac.insert("", tk.END, values=(
            p["id"], p["nome"], p["cpf"],
            p["data_nascimento"], p["telefone"], p["email"], p["endereco"]
        ))

def cadastrar_medico():
    nome  = entry_med_nome.get().strip()
    crm   = entry_med_crm.get().strip()
    esp   = entry_med_esp.get().strip()
    tel   = entry_med_tel.get().strip()
    email = entry_med_email.get().strip()

    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome do médico!")
        return
    if not crm:
        messagebox.showwarning("Aviso", "Digite o CRM do médico!")
        return

    medicos.append({
        "id": novo_id_med(),
        "nome": nome,
        "crm": crm,
        "especialidade": esp,
        "telefone": tel,
        "email": email
    })
    atualizar_combos()
    atualizar_tabela_medicos()
    messagebox.showinfo("Sucesso", f'Médico "{nome}" cadastrado!')
    for e in [entry_med_nome, entry_med_crm, entry_med_esp,
              entry_med_tel, entry_med_email]:
        e.delete(0, tk.END)

def editar_medico():
    sel = tree_med.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione um médico para editar!")
        return
    id_med = int(tree_med.item(sel[0])["values"][0])
    for m in medicos:
        if m["id"] == id_med:
            entry_med_nome.delete(0, tk.END);  entry_med_nome.insert(0, m["nome"])
            entry_med_crm.delete(0, tk.END);   entry_med_crm.insert(0, m["crm"])
            entry_med_esp.delete(0, tk.END);   entry_med_esp.insert(0, m["especialidade"])
            entry_med_tel.delete(0, tk.END);   entry_med_tel.insert(0, m["telefone"])
            entry_med_email.delete(0, tk.END); entry_med_email.insert(0, m["email"])
            medicos.remove(m)
            atualizar_combos()
            atualizar_tabela_medicos()
            break

def excluir_medico():
    sel = tree_med.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione um médico para excluir!")
        return
    id_med = int(tree_med.item(sel[0])["values"][0])
    if any(c["medico_id"] == id_med for c in consultas):
        messagebox.showwarning("Aviso", "Médico possui consultas vinculadas!")
        return
    global medicos
    medicos = [m for m in medicos if m["id"] != id_med]
    atualizar_combos()
    atualizar_tabela_medicos()
    messagebox.showinfo("Sucesso", "Médico excluído!")

def atualizar_tabela_medicos():
    tree_med.delete(*tree_med.get_children())
    for m in medicos:
        tree_med.insert("", tk.END, values=(
            m["id"], m["nome"], m["crm"],
            m["especialidade"], m["telefone"], m["email"]
        ))

def agendar_consulta():
    if not combo_pac_con.get():
        messagebox.showwarning("Aviso", "Selecione um paciente!")
        return
    if not combo_med_con.get():
        messagebox.showwarning("Aviso", "Selecione um médico!")
        return
    data = entry_con_data.get().strip()
    hora = entry_con_hora.get().strip()
    obs  = entry_con_obs.get().strip()

    if not data:
        messagebox.showwarning("Aviso", "Digite a data da consulta!")
        return
    if not hora:
        messagebox.showwarning("Aviso", "Digite a hora da consulta!")
        return

    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        messagebox.showwarning("Aviso", "Data inválida! Use o formato DD/MM/AAAA.")
        return

    id_pac = int(combo_pac_con.get().split(" - ")[0])
    id_med = int(combo_med_con.get().split(" - ")[0])

    consultas.append({
        "id": novo_id_con(),
        "data": data,
        "hora": hora,
        "observacao": obs,
        "paciente_id": id_pac,
        "medico_id": id_med
    })
    atualizar_tabela_consultas()
    messagebox.showinfo("Sucesso", "Consulta agendada!")
    entry_con_data.delete(0, tk.END)
    entry_con_hora.delete(0, tk.END)
    entry_con_obs.delete(0, tk.END)
    combo_pac_con.set("")
    combo_med_con.set("")

def editar_consulta():
    sel = tree_con.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione uma consulta para editar!")
        return
    id_con = int(tree_con.item(sel[0])["values"][0])
    for c in consultas:
        if c["id"] == id_con:
            entry_con_data.delete(0, tk.END); entry_con_data.insert(0, c["data"])
            entry_con_hora.delete(0, tk.END); entry_con_hora.insert(0, c["hora"])
            entry_con_obs.delete(0, tk.END);  entry_con_obs.insert(0, c["observacao"])
            for i, p in enumerate(pacientes):
                if p["id"] == c["paciente_id"]:
                    combo_pac_con.current(i)
            for i, m in enumerate(medicos):
                if m["id"] == c["medico_id"]:
                    combo_med_con.current(i)
            consultas.remove(c)
            atualizar_tabela_consultas()
            break

def excluir_consulta():
    sel = tree_con.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione uma consulta para excluir!")
        return
    id_con = int(tree_con.item(sel[0])["values"][0])
    global consultas
    consultas = [c for c in consultas if c["id"] != id_con]
    atualizar_tabela_consultas()
    messagebox.showinfo("Sucesso", "Consulta excluída!")

def atualizar_tabela_consultas():
    tree_con.delete(*tree_con.get_children())
    for c in consultas:
        nome_pac = next((p["nome"] for p in pacientes if p["id"] == c["paciente_id"]), "—")
        nome_med = next((m["nome"] for m in medicos   if m["id"] == c["medico_id"]),   "—")
        tree_con.insert("", tk.END, values=(
            c["id"], c["data"], c["hora"],
            nome_pac, nome_med, c["observacao"]
        ))

VERMELHO = "#D71920"
BRANCO   = "white"
CINZA    = "#F5F5F5"

janela = tk.Tk()
janela.title("Sistema Clínico UNIESP")
janela.geometry("1000x700")
janela.configure(bg=CINZA)

tk.Label(janela, text="UNIESP — Sistema de Consultas",
         font=("Segoe UI", 15, "bold"), fg=VERMELHO, bg=CINZA
).pack(pady=(16, 4))

notebook = ttk.Notebook(janela)
notebook.pack(fill="both", expand=True, padx=16, pady=8)

def campo(frame, texto, row, col=0, width=30):
    tk.Label(frame, text=texto, bg=BRANCO).grid(row=row, column=col, sticky="e", padx=6, pady=3)
    e = tk.Entry(frame, width=width)
    e.grid(row=row, column=col+1, sticky="w", pady=3)
    return e

def botoes_crud(frame, row, cmd_salvar, cmd_editar, cmd_excluir):
    f = tk.Frame(frame, bg=BRANCO)
    f.grid(row=row, column=0, columnspan=4, pady=8)
    for txt, cmd in [("💾 Salvar", cmd_salvar), ("✏️ Editar", cmd_editar), ("🗑️ Excluir", cmd_excluir)]:
        tk.Button(f, text=txt, bg=VERMELHO, fg=BRANCO, width=14, command=cmd).pack(side="left", padx=4)

def tabela(parent, colunas, larguras):
    frame = tk.Frame(parent, bg=BRANCO)
    frame.pack(fill="both", expand=True, padx=10, pady=6)
    sb = ttk.Scrollbar(frame, orient="vertical")
    sb.pack(side="right", fill="y")
    tv = ttk.Treeview(frame, columns=colunas, show="headings",
                      height=8, yscrollcommand=sb.set)
    sb.config(command=tv.yview)
    for col, larg in zip(colunas, larguras):
        tv.heading(col, text=col)
        tv.column(col, width=larg, anchor="center")
    tv.pack(fill="both", expand=True)
    return tv

aba_pac = tk.Frame(notebook, bg=BRANCO)
notebook.add(aba_pac, text="  👤 Pacientes  ")

form_pac = tk.LabelFrame(aba_pac, text="Dados do Paciente", bg=BRANCO, padx=10, pady=8)
form_pac.pack(fill="x", padx=10, pady=8)

entry_pac_nome  = campo(form_pac, "Nome:",             0)
entry_pac_cpf   = campo(form_pac, "CPF:",              1)
entry_pac_nasc  = campo(form_pac, "Nascimento:",       2)
entry_pac_tel   = campo(form_pac, "Telefone:",         3)
entry_pac_email = campo(form_pac, "Email:",            0, col=2)
entry_pac_end   = campo(form_pac, "Endereço:",         1, col=2, width=35)

botoes_crud(form_pac, 4, cadastrar_paciente, editar_paciente, excluir_paciente)

tree_pac = tabela(aba_pac,
    ("ID", "Nome", "CPF", "Nascimento", "Telefone", "Email", "Endereço"),
    (40, 160, 110, 90, 100, 160, 180))

aba_med = tk.Frame(notebook, bg=BRANCO)
notebook.add(aba_med, text="  🩺 Médicos  ")

form_med = tk.LabelFrame(aba_med, text="Dados do Médico", bg=BRANCO, padx=10, pady=8)
form_med.pack(fill="x", padx=10, pady=8)

entry_med_nome  = campo(form_med, "Nome:",          0)
entry_med_crm   = campo(form_med, "CRM:",           1)
entry_med_esp   = campo(form_med, "Especialidade:", 2)
entry_med_tel   = campo(form_med, "Telefone:",      0, col=2)
entry_med_email = campo(form_med, "Email:",         1, col=2)

botoes_crud(form_med, 3, cadastrar_medico, editar_medico, excluir_medico)

tree_med = tabela(aba_med,
    ("ID", "Nome", "CRM", "Especialidade", "Telefone", "Email"),
    (40, 180, 100, 150, 110, 180))

aba_con = tk.Frame(notebook, bg=BRANCO)
notebook.add(aba_con, text="  📋 Consultas  ")

form_con = tk.LabelFrame(aba_con, text="Agendamento de Consulta", bg=BRANCO, padx=10, pady=8)
form_con.pack(fill="x", padx=10, pady=8)

tk.Label(form_con, text="Paciente:", bg=BRANCO).grid(row=0, column=0, sticky="e", padx=6, pady=3)
combo_pac_con = ttk.Combobox(form_con, width=28, state="readonly")
combo_pac_con.grid(row=0, column=1, sticky="w", pady=3)

tk.Label(form_con, text="Médico:", bg=BRANCO).grid(row=0, column=2, sticky="e", padx=6)
combo_med_con = ttk.Combobox(form_con, width=28, state="readonly")
combo_med_con.grid(row=0, column=3, sticky="w", pady=3)

entry_con_data = campo(form_con, "Data (DD/MM/AAAA):", 1, width=15)
entry_con_hora = campo(form_con, "Hora (HH:MM):",      2, width=10)

tk.Label(form_con, text="Observação:", bg=BRANCO).grid(row=1, column=2, sticky="e", padx=6)
entry_con_obs = tk.Entry(form_con, width=32)
entry_con_obs.grid(row=1, column=3, sticky="w", pady=3)

f_btn_con = tk.Frame(form_con, bg=BRANCO)
f_btn_con.grid(row=3, column=0, columnspan=4, pady=8)
for txt, cmd in [("💾 Agendar", agendar_consulta),
                 ("✏️ Editar",  editar_consulta),
                 ("🗑️ Excluir", excluir_consulta)]:
    tk.Button(f_btn_con, text=txt, bg=VERMELHO, fg=BRANCO, width=14, command=cmd).pack(side="left", padx=4)

tree_con = tabela(aba_con,
    ("ID", "Data", "Hora", "Paciente", "Médico", "Observação"),
    (40, 90, 70, 180, 180, 220))

janela.mainloop()