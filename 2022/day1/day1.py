#Partie 1

textInput = open("day1_input.txt", "r")
numeric = "1234567890"
sum = maximum = 0
for lign in textInput:
    if lign[0] not in numeric: #si la ligne est un espace
        if sum>maximum:
            maximum = sum
        sum = 0 # on arrête la somme
        continue
    sum += int(lign) 

print(maximum)
