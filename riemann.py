import numpy as np
import matplotlib.pyplot as plt

# Nome: Gabriel Santos Costa
# Matrícula: 2311100036
# Data 24/03/2024

def f(x):
    return 1 / (1 + x**2)

intervalo_a = int(input("Digite o intervalo mínimo: "))
intervalo_b = int(input("Digite o intervalo máximo: "))
num_particoes = int(input("Digite o número de partições: "))

x_valores = np.linspace(intervalo_a, intervalo_b, num_particoes + 1)

largura_particao = (intervalo_b - intervalo_a) / num_particoes

altura_particao = f(x_valores[:-1])

area_particao = largura_particao * altura_particao

soma_areas = np.sum(area_particao)

plt.bar(x_valores[:-1], altura_particao, width=largura_particao, alpha=0.4, align='edge', color='purple', label='Retângulos')

valores_x = np.linspace(intervalo_a, intervalo_b, 400)
plt.plot(valores_x, f(valores_x), color='purple', label='f(x)')

plt.text(2.5, 0.5, "Área da função: {:.6f}".format(soma_areas), fontsize=10, ha='center')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Soma de Riemann para f(x)')
plt.legend()
plt.grid(True)
plt.show()
