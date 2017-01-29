#SO it begins... again :-)
#lety chci ukladat do objektu tridy let, s atributy nasledovnici
#nasledne ve funkci retezeni_letu chci retezit lety a nekam to ulozit :-)

import datetime, pprint
zdroj_vstupu = 'vstup.txt'
#seznam_indexu = ["source", "destination", "departure", "arrival", "flight_number", "price", "bags_allowed", "bag_price"]
seznam_letu = list()
#Je toto nutno komentovat? Nu uvidime zitra rano :/

class Let():
    def __init__(self, source, destination, departure, arrival, flight_number, price, bags_allowed, bag_price):
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.flight_number = flight_number
        self.price = price
        self.bags_allowed = bags_allowed
        self.bag_price = bag_price
        self.navazujici = list()

    def __repr__(self):
        return self.flight_number


def sedi_cas(t1, t2):
#Funkce na porovnani casu priletu a odletu danych letu
    dovolena_odchylka = datetime.timedelta(0,14400)
    nulovy_cas = datetime.timedelta(0,0)
    cas1 = datetime.datetime(int(t1[0:4]), int(t1[5:7]), int(t1[8:10]), int(t1[11:13]), int(t1[14:16]))
    cas2 = datetime.datetime(int(t2[0:4]), int(t2[5:7]), int(t2[8:10]), int(t2[11:13]), int(t2[14:16]))
    rozdil_casu = cas2-cas1
    if nulovy_cas < rozdil_casu <= dovolena_odchylka:
        return True
    else:
        return False

def nacteni_vstupu(zdroj_vstupu):
    seznam_pomocny = list()
    with open(zdroj_vstupu) as soubor:
        #Otevru soubor po radkach
        for radek in soubor.readlines():
            radek = radek.rstrip()#zbavim radky otravnych \n
            seznam_pomocny.append(radek.split(","))#rozsekam stringy dle logickych celku
            seznam_letu.append(Let(seznam_pomocny[0][0], seznam_pomocny[0][1], seznam_pomocny[0][2], seznam_pomocny[0][3], seznam_pomocny[0][4], seznam_pomocny[0][5], seznam_pomocny[0][6], seznam_pomocny[0][7]))
            seznam_pomocny.clear()#smazu seznam, jen pro jistotu :-)

def overeni_navaznosti_letu(let1, let2):
    if (let1.destination == let2.source) and sedi_cas(let1.arrival, let2.departure):
        return True
    else:
        return False

def prevest_jmeno_letu_na_pozici_v_poli(seznam_letu, identifikator_letu):
    for pozice, flight in enumerate(seznam_letu):
        if flight.flight_number == identifikator_letu:
            return pozice

def retezeni_letu(seznam_letu):
    #Jako prvni si zjistim, kdo na koho navazuje
    for number1, flight in enumerate(seznam_letu):
        for number2, flight2 in enumerate(seznam_letu):
            if overeni_navaznosti_letu(flight, flight2):
                flight.navazujici.append(flight2.flight_number)
    # Nejdrive si udelam dvojice
    seznam_retezcu = list()
    pomocny_list = list()
    for object in seznam_letu:
        for atribut in object.navazujici:
            if atribut != []:
                pomocny_list.append(object.flight_number)
                pomocny_list.append(atribut)
                seznam_retezcu.append(list(pomocny_list))
                pomocny_list = list()
    #A ted rozjedeme retezeni ve velkem cyklu...ehm...stylu
    jedeme = True
    while jedeme:
        jedeme = False
        for pivotni_retez in seznam_retezcu:
            for testovany_retez in seznam_retezcu:
                if pivotni_retez[-1] == testovany_retez[0]:
                    pomocny_list = pivotni_retez + testovany_retez[1:]
                    if pomocny_list in seznam_retezcu:
                        continue
                    else:
                        seznam_retezcu.append(pomocny_list)
                        jedeme = True
    return list(seznam_retezcu)

nacteni_vstupu(zdroj_vstupu)
seznam_retezcu = retezeni_letu(seznam_letu)

for flight in seznam_letu:
    print('Na let cislo {} navazuji lety {}'.format(flight.flight_number, flight.navazujici))
    del flight.navazujici
for radek in seznam_retezcu:
    for clen in radek:
        pozice = prevest_jmeno_letu_na_pozici_v_poli(seznam_letu, clen)
        print(vars(seznam_letu[pozice]))
    print()
