class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_pordia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_pordia = pontos_pordia
        self.linguagem = linguagem
        
    def __repr__(self):
        return f"{self.nome} ({self.senioridade}, {self.linguagem})"
    
class Projeto: 
    def __init__(self, descricao, prazo_dias, pontos_funcao):
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, dev: Desenvolvedor):
        self.desenvolvedores.append(dev)

    def calcular_capacidade_total(self):
        return sum(dev.pontos_pordia for dev in self.desenvolvedores) * self.prazo_dias

    def verificar_viabilidade(self):
        capacidade = self.calcular_capacidade_total()
        if capacidade >= self.pontos_funcao:
            return "projeto viavel vambora kk"
        else:
            return "projeto inviavel ta ruim ó"
        
projeto = Projeto(descricao="Sistema de controle academico", prazo_dias=30, pontos_funcao=500)

dev1 = Desenvolvedor("Rogerio Ceni", "Sênior idolo do sao paulo", 20, "Python")
dev2 = Desenvolvedor("Jorge Ben", "Junior idolo do mpb", 10, "Java")
dev3 = Desenvolvedor("Darth Vader", "Pleno e lider do lado mal da força", 15, "C#")

projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)
projeto.adicionar_desenvolvedor(dev3)

print("Capacidade total:", projeto.calcular_capacidade_total())
print("Resultado:", projeto.verificar_viabilidade())