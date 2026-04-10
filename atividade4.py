from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Jorge", "email": "jorgeben@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Rogerio", "email": "rogerioceni@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "cleiton", "email": "cleitonrasta@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

def validar_alunos(aluno, cursos):
    motivos = []

    if len(aluno.get("nome", "")) < 3:
        motivos.append("Nome com menos de 3 caracteres")
    
    email = aluno.get("email", "")
    if "@" not in email or "." not in email.split("@")[-1]:
        motivos.append("Email invalido")
    
    if aluno.get("idade", 0) < 16:
        motivos.append("Idade menor que 16 anos")
    
    if aluno.get("curso") not in cursos:
        motivos.append("Curso não disponível")
    
    return motivos

@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def post_aluno():
    novo_aluno = request.get_json()
    motivos = validar_alunos(novo_aluno, cursos_disponiveis)

    if motivos:
        return jsonify({
            "status": "invalido", 
            "aluno": novo_aluno["nome"], 
            "motivos": motivos
        }), 400
    else:
        alunos.append(novo_aluno)
        return jsonify({
            "status": "valido", 
            "aluno": novo_aluno
        }), 201

if __name__ == "__main__":
    app.run(debug=True)