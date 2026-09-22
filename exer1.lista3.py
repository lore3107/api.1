# caixas disponíveis 
caix_disponiveis = 1250

# quanto caminhão suporta 
cami_suporta = 12

# quantos caminhões cheios 
cami_cheio = caix_disponiveis / cami_suporta

# exibição de caminhões cheios 
print("Caminhões cheios", cami_cheio) 

# quantas caixas sobrarão: operador % retorna o restante da divisão
caix_sobradas = caix_disponiveis % cami_suporta

# exibição das caixas sobradas 
print("Caixas restantes", caix_sobradas)