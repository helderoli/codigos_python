#exibição do nome da fazenda e quantidade de cavalos na fazenda, e quantidade de ferraduras necessarias para equipar todos cavalos!

nome = input("Insira o nome da sua fazenda aqui: ")
quantidade = int(input("Insira a quantidade de cavalos que sua fazenda tem: "))

print("Pronto!, sua fazenda", nome, "está pronta pra fazer sua solicitação de ferraduras")

print("A fazenda", nome, "possui", quantidade, "cavalos, a quantidade total de ferraduras para equipar todos os cavalos é:", quantidade*4, "ferraduras!")