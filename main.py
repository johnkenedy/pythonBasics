"""
a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print(a)

# Comentário de 1 linha
""""""Comentario
de multiplas linhas""""""

# Tema 2: Variables

# Atribuição Múltipla
a, b = 1, 2
print("Antes da troca")
print(f"O valor das variáveis: a = {a}, b = {b}")

# Primeira Troca
temp = a
a = b
b = temp
print("Primeira troca")
print(f"O valor das variáveis: a = {a}, b = {b}")

# Segunda troca
a, b = b, a
print("Segunda troca")
print(f"O valor das variáveis: a = {a}, b = {b}")

print(1_000_000)
print(type(1_000_000))

# Complex type
complexType = complex(2, 5)
print(complexType)
# A chamada r.conjugate() retorna o conjugado do número complexo r,
# em que a parte real é mantida e a parte imaginária tem o seu sinal trocado.
complexConjugate = complexType.conjugate()
print(complexConjugate)

print(not (2 < 3))

# Por exemplo, tuple('abc') retorna ('a', 'b', 'c') e tuple( [1, 2, 3] ) retorna (1, 2, 3).
# range(3) cria a sequência (0, 1, 2), range(2, 7) cria a sequência (2, 3, 4, 5, 6).
# O passo é o valor que será incrementado de um termo para o próximo. Por exemplo, range(2, 9, 3) cria a sequência (2, 5, 8).


# Tema 3: Extruturas condicionais

a = 9
b = 22
maior = a
if b > a:
    maior = b
print(f'O maior é: {maior}')

if a % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')

lista = [10, 2, 5, 7, 6, 3, 10]
soma = 0

for i in lista:
    if i % 2 == 0:
        soma = soma + i
print(f'O valor é: {soma}')

s = 0
a = 1
while s < 5:
    s = 3 * a
    a += 1
    print(s)



def find_minimum(lista):
    minimo = lista[0]
    for elem in lista:
        if elem < minimo:
            minimo = elem
    return minimo


test_list = [2, 10, 3, 9, 6, 5, 4, 2, 1, 9]
least = find_minimum(test_list)
print(least)


# Tema 4: Excecoes


def check_if_it_is_number(numero):
    try:
        x = int(numero)
        print(f'Your number is { x }')
    except ValueError:
        print("Entre com um número válido")
        check_if_it_is_number(input("Digite um numero válido: "))


check_if_it_is_number(input("Digite um numero: "))


while True:
    try:
        x = int(input("Digite um numero: "))
        print(f'Your number is {x}')
        break
    except ValueError:
        print("Entre com um numero valido")

# Modulo 2 Orientado a objetos - Agregação, classes e metodos estáticos
    #Agregação


class Salary:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def annual_salary(self):
        return (self.base * 12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.aggregate_salary = salary

    def total_salary(self):
        return self.aggregate_salary.annual_salary()


salary = Salary(10000, 700)
employee = Employee('John', 26, salary)
print(employee.total_salary())

# Classes e metodos estáticos


from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_age(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def legal_age(age):
        return age >= 18


person1 = Person("John", 26)
person2 = Person.from_birth_age("Patty", 2000)

print(person1.age)
print(person2.age)
print(Person.legal_age(17))
"""
