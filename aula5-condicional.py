nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

media = (nota1 + nota2)/2

if media >= 7:
    print("Sua media foi", media, "Você passou :)")
elif media == 6:
    print("Sua media foi 6, você está de recuperação")
else:
    print("Sua media foi", media, "Você reprovou :( )")