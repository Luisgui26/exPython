import matplotlib.pyplot as plt

t = 0
pop_a = 80000
pop_b = 200000
a = [pop_a]
b = [pop_b]
while pop_a < pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    t += 1
    a.append(pop_a)
    b.append(pop_b)
    tempo.append(t)
print(f"Você vai precisar de {t} anos")

plt.plot(tempo, a, "b", label = "Pop A")
plt.plot(tempo, b, "r", label = "Pop B")
plt.legend()
plt.ylabel("População")
plt.xlabel("tempo")
plt.title("População em função do tempo")
plt.grid()
plt.show()
