# faturamento inicial do projeto
fat_inicial = 15000

# custos fixos de faturamento 
cust_fixo = 5000

# impostos sobre faturamento 
impo_fat = 15/100 * fat_inicial
# exibição do faturamento 
print("Imposto sobre o faturamento",impo_fat)

# lucro liquido do projeto
luc_liquido = fat_inicial - impo_fat
# exibição do lucro liquido do projeto
print("Lucro liquido do projeto", luc_liquido)

# margem de lucro do projeto 
marg_lucro = luc_liquido / fat_inicial
# exibição da margem de lucro 
print("Margem de lucro", marg_lucro)

# verifica se a meta atingida é superior a 30%: true se for maior e false se menor
meta_ating = marg_lucro > 0.3 
# exibição da meta 
print("Meta atingida", meta_ating)