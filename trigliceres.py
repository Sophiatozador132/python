j = input("Você está em jejum s/n? ")
t = input("trigliceres? ")
t = int(t) # converter pra int
if j == ("s"):
    if t >150:
        print("Seu trigliceres está alto")
    else:
        print("Seu trigliceres está normal")
else:
    if t >175:
        print("Seu trigliceres está alto!")
    else:
        print("Seu trigliceres está normal")