records = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
names_incorrect = []
names_correct = []
names_edited = []

for i in records:
    testing_capital = []
    pairs = []
    name_splited = i.split()

    for n in name_splited:
        control_lower = n.islower()
        if control_lower == True:
            testing_capital.append(n)
        n = n.capitalize()
        pairs.append(n)

    names_edited.append(" ".join(pairs))

    if testing_capital:
        names_incorrect.append(i)
    else:
        names_correct.append(i)

print("Nesprávně napsaná jména:", names_incorrect)
print("Správně napsaná jména:", names_correct)
print("Opravena jmena:", names_edited)


