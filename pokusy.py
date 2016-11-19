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

pole = []
pole.append([])
pole[0].append([1])
pole[0].append([2])
print(pole[0])






#Testovaci tisknuti neuskodi, ne?
#for index in range(len(seznam_vstupu)):
#    print(seznam_vstupu[index]["bags_allowed"])
#print(seznam_vstupu[j][seznam_indexu[-1]])
