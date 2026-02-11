# SCTEC

## Carreira tech

### Trilha Data Science

Sobre o programa
O SCTEC é um programa do Governo de Santa Catarina, em parceria com o SENAI/SC, que visa impulsionar a inovação e o desenvolvimento tecnológico no estado. O programa capacita o participante para o uso da Inteligência Artificial e o prepara para construir ou aprimorar sua carreira em tecnologia.

---

### Modulo 01

---

**# Configurando Ambiente com Virtualenv**<br>

---

Intalando virtualenv:

```bash
pip3 install virtualenv
```

Criando ambiente:

```bash
virtualenv venv
```

Ativando o ambiente:

```bash
venv\Scripts\activate
```

Desativando o ambiente:

```bash
deactivate
```

---

**# Estrutura de Dados**<br>
Estrutura de dados: Listas, Dicionários, Tuplas, Módulos e Pacotes.

---

- Lista:

```bash
numeros = [10,20,30,40]
nomes = ["Ana","João","Maria"]
```

Adicionar Elemendo na Lista:

Append( ): A funcão adicionar novos elementos no final da lista.

```bash
numeros.append(50)
nomes.append("Pedro")
```

Insert( ): A função adicionar um novo elemento na lista sendo o primeiro parametro indicando a posição do novo elemento dentro da lista, e o segundo parametro indicando o valor do novo elemento adicionado na lista.

```bash
numeros.insert(0,50)
nomes.insert(0,"Pedro")
```

---

Remover Elemento da Lista:

remove( ): a função remove um elemento da lista.

```bash
numeros.remove(50)
nomes.remove("Pedro")
```

pop( ): a função remove um elemento da lista a partir do indice.

```bash
numeros.pop(4)
nomes.pop(3)
```
