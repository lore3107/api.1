# faturamento bruto da empresa = 50.000
fat = 50000

# percentual de bonus = 10%
perc_de_bonus = 0.10

# calculo do valor total do bonus 
bon_total = fat * perc_de_bonus

#calculo do valor final do faturamento
fat_final = fat - bon_total

# exiba o valor do bonus 
print("Bonus total", bon_total)

# exiba o valor do faturamento final
print("Faturamento final", fat_final)