textInput = open("day1_input.txt", "r")
numeric = "1234567890"
sum = i = maximum = imaximum = 0
for lign in textInput:
    if lign[0] not in numeric: #si la ligne est un espace
        i += 1
        if sum>maximum:
            maximum,imaximum = sum,i
        sum = 0 # on arrête la somme
        continue
    sum += int(lign) 

print(imaximum,maximum)
