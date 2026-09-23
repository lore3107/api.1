# faturamento do produto
fat_prod = 45000

# custo do produto
custo = 23500

# calculo do lucro
lucro = fat_prod - custo

# calculo da margem de lucro
margem = lucro / fat_prod

# exibição do lucro e da margem
# :,.2f : separador de milhar e duas casas decimais
# :.0% : converte para porcentagem sem casas decimais 

print(f"Lucro: R${lucro:,.2f}, Margem: {margem:.0%}")