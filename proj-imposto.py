def somarImposto(valor, taxaImposto):
    return valor + (valor * taxaImposto/ 100)

print("=== Cálculo de Preço de Imposto ===")
valor = float(input("Digite a taxa de imposto(%): "))
taxaImposto = float(input("Digite o custo do item (antes do imposto): "))

valorImposto = somarImposto(valor, taxaImposto)
print(f"Preço final com imposto: R$ {valorImposto}")