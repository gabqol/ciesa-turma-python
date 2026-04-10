
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Jorge", "email": "jorgeben@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Rogerio", "email": "rogerioceni@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "cleiton", "email": "cleitonrasta@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

def validar_alunos(alunos):
    alunos_validos = []
    alunos_invalidos = []

    for aluno in alunos:
        motivos = []

        if len(aluno['nome']) < 3:
            motivos.append('Nome com menos de 3 caracteres')
        if "@" not in aluno['email'] or "." not in aluno['email'].split("@")[-1]:
            motivos.append("Email inválido")

        if aluno['idade'] < 16:
            motivos.append('Idade menor que 16 anos')

        if aluno['curso'] not in cursos_disponiveis:
            motivos.append("Curso não disponível")

        if motivos:
            alunos_invalidos.append({"nome": aluno['nome'], "motivos": motivos})
        else:
            alunos_validos.append(aluno)

    return alunos_validos, alunos_invalidos
validos, invalidos = validar_alunos(alunos)

print("Alunos válidos:", validos)
print("Alunos inválidos:", invalidos)