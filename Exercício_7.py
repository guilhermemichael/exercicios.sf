# 7. Conversor de Moeda: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar (Considere US$ 1,00 = R$ 5,00).

print("Conversor de Moeda")

r = float(input("Digite quanto dinheiro você possui na carteira (em R$): "))
d = r / 5.0

print(f"\nVocê possui R$ {r:.2f}")
print(f"\nPode comprar US$ {d:.2f}")

print(f"\nCom R$ {r:.2f} você pode comprar até US$ {d:.2f}, considerando a cotação de US$ 1,00 = R$ 5,00.")
