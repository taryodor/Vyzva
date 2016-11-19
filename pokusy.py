#Tak a jdu si hrat s casem
"""import datetime, time

casik1 = "2017-02-11T06:25:00"
casik2 = "2017-02-11T07:25:00"

def sedi_cas(t1, t2):
    dovolena_odchylka = datetime.timedelta(0,14400)
    cas2 = datetime.datetime(int(t1[0:4]), int(t1[5:7]), int(t1[8:10]), int(t1[11:13]), int(t1[14:16]))
    cas1 = datetime.datetime(int(t2[0:4]), int(t2[5:7]), int(t2[8:10]), int(t2[11:13]), int(t2[14:16]))
    rozdil_casu = cas2-cas1
    if cas1 >= cas2 and rozdil_casu <= dovolena_odchylka:
        return True

for l in range(len(seznam_kombinaci)):
    for m in range(len(seznam_kombinaci)):
        if l == m:
            continue
        for u in range(len(seznam_kombinaci[m])):
            if seznam_kombinaci[l][-1] == seznam_kombinaci[m][u] and u < len(seznam_kombinaci[m])-1:
                pojistka.append(list.copy(seznam_kombinaci[l]))
                pojistka[-1].append(seznam_kombinaci[m][u+1])#Sem a na odpovidajici misto dole staci pridat cyklus, ktery pridava vsechny nasledujici cleny, ale uz jdu spat. Doubrou
                if pojistka[-1] in seznam_kombinaci:
                    continue
                seznam_kombinaci.append(list.copy(seznam_kombinaci[l]))
                seznam_kombinaci[-1].append(seznam_kombinaci[m][u+1])


print(sedi_cas(casik1, casik2))
"""

"""
for i in range(11):
    if i == 7:
        continue
    print(i)

def sedi_destinace(d1,d2):
    return d1 == d2

def sedi_pocet_baglu(pocet_bagu1, pocet_bagu2):
    return pocet_bagu1 <= pocet_bagu2
"""

for i in range(10):
    print(i)

print()
print(i)

for i in range(10):
    print(i)






#Testovaci tisknuti neuskodi, ne?
#for index in range(len(seznam_vstupu)):
#    print(seznam_vstupu[index]["bags_allowed"])
#print(seznam_vstupu[j][seznam_indexu[-1]])
