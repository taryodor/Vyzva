#tady si chci zkusit nacteni ze zdrojaku a rozsekani na kousky, ulozeni do sloviku a jdu spat
import collections, datetime, time
#Toto importuji proto, abych mohl pouzit serazeny slovnik
#Ten pouzivam jen pro muj komfort :-)
seznam_vstupu = []
#Sem ukladam radky vstupu do serazenych slovniku
seznam_pomocny = []
slovnik_pomocny = collections.OrderedDict()
#Pomocnici k peknemu rozsekani a rozcleneni jednotlivych radku

seznam_kombinaci = []
#sem chci ukladat vafiltrovane kombinace
#Ukladat chci jen cisla radku, ktere se nasledne znovuoveri a promazou

seznam_indexu = ["source", "destination", "departure", "arrival", "flight_number", "price", "bags_allowed", "bag_price"]
#Je toto nutno komentovat? Nu uvidime zitra rano :-)

def sedi_cas(t1, t2):
    dovolena_odchylka = datetime.timedelta(0,14400)
    nulovy_cas = datetime.timedelta(0,0)
    cas1 = datetime.datetime(int(t1[0:4]), int(t1[5:7]), int(t1[8:10]), int(t1[11:13]), int(t1[14:16]))
    cas2 = datetime.datetime(int(t2[0:4]), int(t2[5:7]), int(t2[8:10]), int(t2[11:13]), int(t2[14:16]))
    rozdil_casu = cas2-cas1
    if nulovy_cas < rozdil_casu <= dovolena_odchylka:
        return True
    else:
        return False

def sedi_destinace(d1,d2):
    return d1 == d2

def nacteni_vstupu(zdroj_vstupu):
    with open(zdroj_vstupu) as soubor:
        #Otevru soubor po radkach
        i = 0
        for radek in soubor.readlines():
            radek = radek.rstrip()#zbavim radky otravnych \n
            seznam_pomocny.append(radek.split(","))#rozsekam stringy dle logickych celku
            for w in range(len(seznam_pomocny[i])):
                slovnik_pomocny[seznam_indexu[w]] = seznam_pomocny[i][w]#nacpu logicke celky do orddictu dle klice
            seznam_vstupu.append(slovnik_pomocny.copy())#ulozim do seznamu ve formatu pripravenem k vyhodnoceni
            slovnik_pomocny.clear()#smazu slovnik, jen pro jistotu :-)
            i += 1

    slovnik_pomocny.clear()
    seznam_pomocny.clear()
#Pokud se nic nezmeni, Vasich sluzeb jiz nebude zapotrebi

def parovani_letu(seznam_letu, radek_porovnavaneho_letu):
    seznam_lokalni = []
    for j in range(len(seznam_letu)):
        if radek_porovnavaneho_letu == j:
            continue#Nechci porovnavat stejne radky
        elif sedi_destinace(seznam_letu[radek_porovnavaneho_letu]["destination"], seznam_letu[j]["source"]) == False:
            continue
        elif sedi_cas(seznam_letu[radek_porovnavaneho_letu]["arrival"], seznam_letu[j]["departure"]) == False:
            continue
        seznam_kombinaci.append([])
        seznam_kombinaci[len(seznam_kombinaci)-1].append(radek_porovnavaneho_letu)
        seznam_kombinaci[len(seznam_kombinaci)-1].append(j)

"""
Cela tat ofunkce je spatne...
def retezeni_letu(seznam_dvojic, index_testovane_dvojice):
    for bb in range(len(seznam_dvojic)):
        if index_testovane_dvojice == bb:
            continue
        #print("testuji ", seznam_dvojic[index_testovane_dvojice][-1], seznam_dvojic[bb][0])
        #print("index testovanych", index_testovane_dvojice, bb)
        if seznam_dvojic[index_testovane_dvojice][-1] == seznam_dvojic[bb][0]:
            seznam_dvojic.append(list.copy(seznam_dvojic[index_testovane_dvojice]))
            seznam_dvojic[index_testovane_dvojice].append(seznam_dvojic[bb][-1])
    return seznam_dvojic
"""


nacteni_vstupu("vstup.txt")#Nacteni vstupu z daneho zdrojaku, pozdeji to udelam na vstup ze soubor udle zadani uzivatele
for i in range(len(seznam_vstupu)):
    parovani_letu(seznam_vstupu, i)

for k in range(len(seznam_kombinaci)):
    print(k, seznam_kombinaci[k])
print()

pojistka = []

for l in range(len(seznam_kombinaci)):
    for m in range(len(seznam_kombinaci)):
        if l == m:
            continue
        if seznam_kombinaci[l][-1] == seznam_kombinaci[m][0]:
            pojistka.append(list.copy(seznam_kombinaci[l]))
            pojistka[-1].append(seznam_kombinaci[m][-1])#Sem a na odpovidajici misto dole staci pridat cyklus, ktery pridava vsechny nasledujici cleny, ale uz jdu spat. Doubrou    
            if pojistka[-1] in seznam_kombinaci:
                continue
            seznam_kombinaci.append(list.copy(seznam_kombinaci[l]))
            seznam_kombinaci[-1].append(seznam_kombinaci[m][-1])
l = 0
m = 0
"""
for l in range(len(seznam_kombinaci)):
    for m in range(len(seznam_kombinaci)):
        #print(len(seznam_kombinaci))
        if l == m:
            continue
        if seznam_kombinaci[l][-1] == seznam_kombinaci[m][0]:
            pojistka.append(list.copy(seznam_kombinaci[l]))
            pojistka[-1].append(seznam_kombinaci[m][-1])
            if pojistka[-1] in seznam_kombinaci:
                continue
            seznam_kombinaci.append(list.copy(seznam_kombinaci[l]))
            seznam_kombinaci[-1].append(seznam_kombinaci[m][-1])
            print("porovnavam ", seznam_kombinaci[l], " s ", seznam_kombinaci[m], end=" ")
            print("spojil jsem..." , l, m, end=" ")
            print("vytvoril jsem...", seznam_kombinaci[-1], end=" ")

for l in range(len(seznam_kombinaci)):
    for m in range(len(seznam_kombinaci)):
        #print(len(seznam_kombinaci))
        if l == m:
            continue
        for q in range(1,len(seznam_kombinaci[m])):
            if seznam_kombinaci[l][-1] == seznam_kombinaci[m][q] and (len(seznam_kombinaci[m])-1)>q:
                pojistka.append(list.copy(seznam_kombinaci[l]))
                pojistka[-1].append(seznam_kombinaci[m][q+1])
                if pojistka[-1] in seznam_kombinaci:
                    continue
                seznam_kombinaci.append(list.copy(seznam_kombinaci[l]))
                seznam_kombinaci[-1].append(seznam_kombinaci[m][q+1])
                print("porovnavam ", seznam_kombinaci[l], " s ", seznam_kombinaci[m], end=" ")
                print("spojil jsem..." , l, m, end=" ")
                print("vytvoril jsem...", seznam_kombinaci[-1])
"""

for k in range(len(seznam_kombinaci)):
    print(k, seznam_kombinaci[k])
print()
