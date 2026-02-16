class Pessoa: # classe é um molde para criar objetos, define atributos e métodos
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def apresentar(self):
        print(f"nome: {self.__nome} - idade: {self.__idade} anos.")

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def set_nome(self, nome):
        self.__nome = nome
        print(f"Nome atualizado para {self.__nome}")
    
    def set_idade(self, idade):
        self.__idade = idade
        print(f"Idade atualizada para {self.__idade} anos.")    

class Aluno(Pessoa): # classe Aluno "herda" da classe Pessoa, ou seja, Aluno é uma subclasse de Pessoa, isto se chama "herança"
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade) # chama o construtor da classe pai
        self.__matricula = matricula

    def apresentar(self): # sobrescreve o método apresentar da classe pai, isto se chama "polimorfismo"
        super().apresentar() # chama o método apresentar da classe pai
        print(f"Sou um aluno meu nome é {self.get_nome()}, minha matrícula {self.__matricula}.")

    def estudante(self): # método específico da classe Aluno
        print(f"Matrícula: {self.__matricula}")
    
a1 = Aluno("Carlos", 20, "2024001")
a1.apresentar()
a1.estudante()

 
    

