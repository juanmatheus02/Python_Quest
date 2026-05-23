alunos = []
matriculas = []
professores = []
disciplinas = []

# Cadastro de professores
qtd_prof = int(input("Quantidade de professores: "))

for i in range(qtd_prof):
    professor = {
        "id": i + 1,
        "nome": input("Nome do professor: "),
        "email": input("Email: "),
        "telefone": input("Telefone: ")
    }
    professores.append(professor)

# Cadastro de disciplinas, associando professor
qtd_disc = int(input("Quantidade de disciplinas: "))

for i in range(qtd_disc):
    print("Professores Disponíveis:")
    for professor in professores:
        print(professor["id"], "-", professor["nome"])

    id_professor = int(input("Escolha o ID do professor: "))

    disciplina = {
        "id": i + 1,
        "nome": input("Nome da disciplina: "),
        "descricao": input("Descrição: "),
        "professor_id": id_professor
    }
    disciplinas.append(disciplina)

# Cadastro de alunos
qtd_alunos = int(input("Quantidade de alunos: "))

for i in range(qtd_alunos):
    aluno = {
        "id": i + 1,
        "nome": input("Nome do aluno: "),
        "matricula": input("Matrícula: "),
        "email": input("Email: ")
    }
    alunos.append(aluno)  # ← parêntese solto removido

# Cadastro de matrículas
qtd_matriculas = int(input("Quantidade de matrículas: "))

for _ in range(qtd_matriculas):
    print("Alunos disponíveis:")
    for aluno in alunos:
        print(aluno["id"], "-", aluno["nome"])
    id_aluno = int(input("Escolha o ID do aluno: "))

    print("Disciplinas disponíveis:")
    for disciplina in disciplinas:
        print(disciplina["id"], "-", disciplina["nome"])
    id_disciplina = int(input("Escolha o ID da disciplina: "))

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    matricula = {
        "id": len(matriculas) + 1,
        "aluno_id": id_aluno,
        "disciplina_id": id_disciplina,
        "nota1": nota1,
        "nota2": nota2,
        "media": media
    }
    matriculas.append(matricula)