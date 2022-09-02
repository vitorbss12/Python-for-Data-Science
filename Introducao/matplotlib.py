import matplotlib.pyplot as plt
from random import randrange

notas = []

for i in range(8):
    notas.append(randrange(0, 10))

x = list(range(1, 9))
y = notas

plt.plot(x, y, marker='o')
plt.title("Notas")
plt.xlabel("Provas")
plt.ylabel("Notas")
plt.show()
