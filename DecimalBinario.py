# converter de decimal para binário

x = int(input("Digite um valor para conversão: "))

aux = x

cont = 0

bin = [];

while x > 0:

    bin.insert(cont,str(x%2))

    x = x // 2

    cont += 1

    continue

bin.reverse()

y = "".join(bin)

print("O número {} em binário é {} ".format(aux,y))

