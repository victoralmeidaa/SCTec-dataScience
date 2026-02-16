class Pessoa: # classe é um molde para criar objetos, define atributos e métodos
    def __init__(self, nome, idade): # método construtor, é chamado automaticamente quando um objeto é criado
        self.__nome = nome # atributo privado, não pode ser acessado diretamente fora da classe
        self.__idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome} e tenho {self.__idade} anos.")

    def get_nome(self): # método getter para acessar o nome privado
        return self.__nome

    def get_idade(self): # método getter para acessar a idade privada
        return self.__idade
    
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

print(p1.get_nome())
print(p1.get_idade())


# Aula 13 - Orientação a Objetos com Python - Parte 2

