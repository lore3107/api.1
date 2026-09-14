#revisando variáveis
print("Olá, mundo!")

nome = "Lorena"
idade = "18"

print(nome)
print(idade)

numero1 = 5
numero2 = 10

resultado = numero1 + numero2

print(resultado)

#maior ou menor de idade: if=se, else=senão
idade = 16
if idade>=18:
  print("Maior de idade")
else
print("Menor de idade")

nota = 5
if nota>=9:
  print("Excelente")
elif nota>=6:
  print("Aprovado")
else
print("Reprovado")

#criar uma função
def saudação():
  print("Olá")

#devolver um resultado
def somar():
  resultado = 5 + 5
  return resultado

#converter para decimal: float
def altura():
  altura = float("1.70")
  print(altura)

#recebe o texto: input
def nome():
  input("Digite o seu nome")
  return nome

#diferença entre int e float: int serve para números inteiros e float serve para decimais.
idade = int(input("Digite sua idade:"))
nota = float(input("Digite sua nota:"))

preço = float(input("Digite o preço:"))
quantidade = int(input("Digite a quantidade:"))

total = preço * quantidade
print(total)
