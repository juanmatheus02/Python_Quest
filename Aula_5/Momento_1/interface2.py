import tkinter as tk
from tkinter import messagebox, ttk

alunos = []
professores = []
disciplinas = []
matriculas = []

# Contadores de ID independentes (evita duplicação ao deletar itens)
_id_prof = 0
_id_disc = 0
_id_aluno = 0
_id_mat = 0


def novo_id_prof():
    global _id_prof
    _id_prof += 1
    return _id_prof


def novo_id_disc():
    global _id_disc
    _id_disc += 1
    return _id_disc


def novo_id_aluno():
    global _id_aluno
    _id_aluno += 1
    return _id_aluno


def novo_id_mat():
    global _id_mat
    _id_mat += 1
    return _id_mat


def atualizar_combos():
    combo_prof_disc["values"] = [
        f'{p["id"]} - {p["nome"]}' for p in professores
    ]
    combo_aluno_mat["values"] = [
        f'{a["id"]} - {a["nome"]}' for a in alunos
    ]
    combo_disc_mat["values"] = [
        f'{d["id"]} - {d["nome"]}' for d in disciplinas
    ]


def cadastrar_professor():
    nome = entry_prof_nome.get().strip()
    email = entry_prof_email.get().strip()

    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome do professor!")
        return

    professor = {
        "id": novo_id_prof(),
        "nome": nome,
        "email": email
    }
    professores.append(professor)
    atualizar_combos()
    messagebox.showinfo("Sucesso", f'Professor "{nome}" cadastrado!')
    entry_prof_nome.delete(0, tk.END)
    entry_prof_email.delete(0, tk.END)


def cadastrar_disciplina():
    nome = entry_disc_nome.get().strip()
    descricao = entry_disc_desc.get().strip()

    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome da disciplina!")
        return
    if not combo_prof_disc.get():
        messagebox.showwarning("Aviso", "Selecione um professor!")
        return

    id_professor = int(combo_prof_disc.get().split(" - ")[0])
    disciplina = {
        "id": novo_id_disc(),
        "nome": nome,
        "descricao": descricao,
        "professor_id": id_professor
    }
    disciplinas.append(disciplina)
    atualizar_combos()
    messagebox.showinfo("Sucesso", f'Disciplina "{nome}" cadastrada!')
    entry_disc_nome.delete(0, tk.END)
    entry_disc_desc.delete(0, tk.END)
    combo_prof_disc.set("")


def cadastrar_aluno():
    nome = entry_aluno_nome.get().strip()
    matricula = entry_aluno_mat.get().strip()
    email = entry_aluno_email.get().strip()

    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome do aluno!")
        return

    aluno = {
        "id": novo_id_aluno(),
        "nome": nome,
        "matricula": matricula,
        "email": email
    }
    alunos.append(aluno)
    atualizar_combos()
    messagebox.showinfo("Sucesso", f'Aluno "{nome}" cadastrado!')
    entry_aluno_nome.delete(0, tk.END)
    entry_aluno_mat.delete(0, tk.END)
    entry_aluno_email.delete(0, tk.END)


def matricular():
    if not combo_aluno_mat.get():
        messagebox.showwarning("Aviso", "Selecione um aluno!")
        return
    if not combo_disc_mat.get():
        messagebox.showwarning("Aviso", "Selecione uma disciplina!")
        return

    try:
        nota1 = float(entry_nota1.get().replace(",", "."))
        nota2 = float(entry_nota2.get().replace(",", "."))
    except ValueError:
        messagebox.showwarning("Aviso", "Digite notas válidas (ex: 7.5)!")
        return

    # Validação do intervalo das notas
    if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
        messagebox.showwarning("Aviso", "As notas devem estar entre 0 e 10!")
        return

    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 6.0 else "Reprovado"

    id_aluno = int(combo_aluno_mat.get().split(" - ")[0])
    id_disciplina = int(combo_disc_mat.get().split(" - ")[0])

    # Verifica matrícula duplicada
    for m in matriculas:
        if m["aluno_id"] == id_aluno and m["disciplina_id"] == id_disciplina:
            messagebox.showwarning(
                "Aviso",
                "Este aluno já está matriculado nesta disciplina!"
            )
            return

    matricula = {
        "id": novo_id_mat(),
        "aluno_id": id_aluno,
        "disciplina_id": id_disciplina,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "situacao": situacao
    }
    matriculas.append(matricula)
    messagebox.showinfo(
        "Sucesso",
        f"Matrícula realizada! Média: {media:.2f} — {situacao}"
    )
    exibir_relatorio()
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)
    combo_aluno_mat.set("")
    combo_disc_mat.set("")


def exibir_relatorio():
    txt_relatorio.delete(1.0, tk.END)

    if not matriculas:
        txt_relatorio.insert(tk.END, "Nenhuma matrícula registrada.\n")
        return

    for matricula in matriculas:
        # Busca nome do aluno
        nome_aluno = next(
            (a["nome"] for a in alunos if a["id"] == matricula["aluno_id"]),
            "Desconhecido"
        )

        # Busca disciplina e professor (bug corrigido: loops estavam fora do escopo)
        nome_disciplina = "Desconhecida"
        nome_professor = "Desconhecido"
        for disciplina in disciplinas:
            if disciplina["id"] == matricula["disciplina_id"]:
                nome_disciplina = disciplina["nome"]
                for professor in professores:
                    if professor["id"] == disciplina["professor_id"]:
                        nome_professor = professor["nome"]
                break

        situacao = matricula.get("situacao", "N/A")
        cor_tag = "aprovado" if situacao == "Aprovado" else "reprovado"

        linha = (
            f"Aluno:      {nome_aluno}\n"
            f"Disciplina: {nome_disciplina}\n"
            f"Professor:  {nome_professor}\n"
            f"Nota 1:     {matricula['nota1']:.2f}\n"
            f"Nota 2:     {matricula['nota2']:.2f}\n"
            f"Média:      {matricula['media']:.2f}  —  {situacao}\n"
            f"{'-' * 50}\n"
        )
        txt_relatorio.insert(tk.END, linha, cor_tag)

    txt_relatorio.tag_config("aprovado", foreground="green")
    txt_relatorio.tag_config("reprovado", foreground="red")


# ── Interface ──────────────────────────────────────────────────────────────────

janela = tk.Tk()
janela.title("Sistema Acadêmico UNIESP")
janela.geometry("900x820")
janela.configure(bg="#F5F5F5")

tk.Label(
    janela,
    text="UNIESP — Sistema Acadêmico",
    font=("Segoe UI", 15, "bold"),
    fg="#D71920",
    bg="#F5F5F5"
).pack(pady=(20, 4))

# ── Professor ─────────────────────────────────────────────────────────────────
frame_prof = tk.LabelFrame(janela, text="Professor", bg="white", padx=10, pady=10)
frame_prof.pack(fill="x", padx=20, pady=8)

tk.Label(frame_prof, text="Nome:", bg="white").grid(row=0, column=0, sticky="e", padx=4)
entry_prof_nome = tk.Entry(frame_prof, width=40)
entry_prof_nome.grid(row=0, column=1, pady=2)

tk.Label(frame_prof, text="Email:", bg="white").grid(row=1, column=0, sticky="e", padx=4)
entry_prof_email = tk.Entry(frame_prof, width=40)
entry_prof_email.grid(row=1, column=1, pady=2)

tk.Button(
    frame_prof, text="Cadastrar Professor",
    bg="#D71920", fg="white", command=cadastrar_professor
).grid(row=2, column=0, columnspan=2, pady=8)

# ── Disciplina ────────────────────────────────────────────────────────────────
frame_disc = tk.LabelFrame(janela, text="Disciplina", bg="white", padx=10, pady=10)
frame_disc.pack(fill="x", padx=20, pady=8)

tk.Label(frame_disc, text="Nome:", bg="white").grid(row=0, column=0, sticky="e", padx=4)
entry_disc_nome = tk.Entry(frame_disc, width=40)
entry_disc_nome.grid(row=0, column=1, pady=2)

tk.Label(frame_disc, text="Descrição:", bg="white").grid(row=1, column=0, sticky="e", padx=4)
entry_disc_desc = tk.Entry(frame_disc, width=40)
entry_disc_desc.grid(row=1, column=1, pady=2)

tk.Label(frame_disc, text="Professor:", bg="white").grid(row=2, column=0, sticky="e", padx=4)
combo_prof_disc = ttk.Combobox(frame_disc, width=37, state="readonly")
combo_prof_disc.grid(row=2, column=1, pady=2)

tk.Button(
    frame_disc, text="Cadastrar Disciplina",
    bg="#D71920", fg="white", command=cadastrar_disciplina
).grid(row=3, column=0, columnspan=2, pady=8)

# ── Aluno ─────────────────────────────────────────────────────────────────────
frame_aluno = tk.LabelFrame(janela, text="Aluno", bg="white", padx=10, pady=10)
frame_aluno.pack(fill="x", padx=20, pady=8)

tk.Label(frame_aluno, text="Nome:", bg="white").grid(row=0, column=0, sticky="e", padx=4)
entry_aluno_nome = tk.Entry(frame_aluno, width=40)
entry_aluno_nome.grid(row=0, column=1, pady=2)

tk.Label(frame_aluno, text="Matrícula:", bg="white").grid(row=1, column=0, sticky="e", padx=4)
entry_aluno_mat = tk.Entry(frame_aluno, width=40)
entry_aluno_mat.grid(row=1, column=1, pady=2)

tk.Label(frame_aluno, text="Email:", bg="white").grid(row=2, column=0, sticky="e", padx=4)
entry_aluno_email = tk.Entry(frame_aluno, width=40)
entry_aluno_email.grid(row=2, column=1, pady=2)

tk.Button(
    frame_aluno, text="Cadastrar Aluno",
    bg="#D71920", fg="white", command=cadastrar_aluno
).grid(row=3, column=0, columnspan=2, pady=8)

# ── Matrícula ─────────────────────────────────────────────────────────────────
frame_mat = tk.LabelFrame(janela, text="Matrícula", bg="white", padx=10, pady=10)
frame_mat.pack(fill="x", padx=20, pady=8)

tk.Label(frame_mat, text="Aluno:", bg="white").grid(row=0, column=0, sticky="e", padx=4)
combo_aluno_mat = ttk.Combobox(frame_mat, width=37, state="readonly")
combo_aluno_mat.grid(row=0, column=1, pady=2)

tk.Label(frame_mat, text="Disciplina:", bg="white").grid(row=1, column=0, sticky="e", padx=4)
combo_disc_mat = ttk.Combobox(frame_mat, width=37, state="readonly")
combo_disc_mat.grid(row=1, column=1, pady=2)

tk.Label(frame_mat, text="Nota 1:", bg="white").grid(row=2, column=0, sticky="e", padx=4)
entry_nota1 = tk.Entry(frame_mat, width=20)
entry_nota1.grid(row=2, column=1, sticky="w", pady=2)

tk.Label(frame_mat, text="Nota 2:", bg="white").grid(row=3, column=0, sticky="e", padx=4)
entry_nota2 = tk.Entry(frame_mat, width=20)
entry_nota2.grid(row=3, column=1, sticky="w", pady=2)

tk.Button(
    frame_mat, text="Matricular",
    bg="#D71920", fg="white", command=matricular
).grid(row=4, column=0, columnspan=2, pady=10)

# ── Relatório ─────────────────────────────────────────────────────────────────
frame_rel = tk.LabelFrame(janela, text="Relatório", bg="white", padx=10, pady=10)
frame_rel.pack(fill="both", expand=True, padx=20, pady=10)

txt_relatorio = tk.Text(frame_rel, font=("Consolas", 10), height=10)
txt_relatorio.pack(fill="both", expand=True)

janela.mainloop()