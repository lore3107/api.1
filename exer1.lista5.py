# contrato em meses 
duracao = 40

# em quantos anos 
anos_contrato = duracao // 12

# quantos meses sobram
meses_sobrados = anos_contrato % 12

# exiba o valor x anos e y meses
print("Duração final é de", anos_contrato, "anos e", meses_sobrados, "meses" )