# 6. Reajuste Salarial: Leia o salário de um funcionário e calcule o novo valor com 15% de aumento.

print("Reajuste Salarial")

s = float(input("Digite o salário do funcionário: R$ "))
a = s * 0.15
ns = s + a

print(f"\nSalário atual: R$ {s:.2f}")
print(f"Aumento: R$ {a:.2f}")
print(f"Novo salário: R$ {ns:.2f}")
