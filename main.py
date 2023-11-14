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
"""Comentario
de multiplas linhas"""

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



















