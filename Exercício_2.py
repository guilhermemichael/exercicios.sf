# 2. Conversor de Medidas: Crie um programa que receba um valor em metros e o exiba convertido em centímetros e milímetros.

print("Conversor de Medidas")

metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"\n{metros} metros:")
print(f"→ {centimetros:.2f} cm")
print(f"→ {milimetros:.2f} mm")
