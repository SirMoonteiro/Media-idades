#coidgo para coletar o sexo e idade,depois mostrar as medias por sexo e total.

sex_m = []
sex_f = []
idade_m = []
idade_f = []

for i in range(1, 5):
    sexo = str(input("Informe o sexo>>> "))
    if sexo == "m":
        sex_m.append(sexo)
        idade = int(input("Informe sua idade >>>"))
        idade_m.append(idade)
    elif sexo == "f":
        sex_f.append(sexo)
        idade = int(input("Informe sua idade >>>"))
        idade_f.append(idade)

media_h = sum(idade_m) / len(sex_m)
media_f = sum(idade_f) / len(sex_f)
media_t = (sum(idade_m) + sum(idade_f)) / (len(sex_m) + len(sex_f))

print("Média de idade dos homens:", media_h)
print("Média de idade das mulheres:", media_f)
print("Média de idade total:", media_t)