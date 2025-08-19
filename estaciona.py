import numpy as np
import matplotlib.pyplot as plt

# Matriz de transição P
P = np.array([
    [0,     0.5,   0.5,   0   ],
    [1/3,   0,     1/3,   1/3 ],
    [0.5,   0,     0,     0.5 ],
    [0.5,   0.5,   0,     0   ]
])

# Número de passos
n_steps = 20
state_labels = ['A', 'B', 'C', 'D']

# Estado inicial: robô começa na página A
pi_0 = np.array([1, 0, 0, 0])
history = [pi_0]

# Iterativamente calcula π⁽ⁿ⁺¹⁾ = π⁽ⁿ⁾P
for _ in range(n_steps):
    pi_next = history[-1] @ P
    history.append(pi_next)

# Converte para array e plota
history = np.array(history)

plt.figure(figsize=(8, 5))
for i in range(4):
    plt.plot(range(n_steps + 1), history[:, i], label=f'Estado {state_labels[i]}')

plt.xlabel("n (número de passos)")
plt.ylabel("Probabilidade de estar no estado")
plt.title("Evolução da distribuição de estados: $\\pi^{(n)} = \\pi^{(0)} P^n$")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("evolucao_potencias_P.png")
plt.show()
