"""
Zbyva dodelat:
-vymazani nevalidnich kombinaci (dle webu)
-spocteni ceny baglovneho pro jednotlive lety
-ulozeni vystupu v rozumnem formatu do souboru
-mrkni na funkci retezeni letu, jestli nebude lepsi uzit "in" a "index"
    - teda lepsi to bude, ale hlavne to bude lepe vypadat
bonus - jde predelat funkci parovani letu tak, aby mi nehrabala do globalnich seznamu?
"""

import collections, datetime, time
#Toto importuji proto, abych mohl pouzit serazeny slovnik
#Ten pouzivam jen pro muj komfort :-)
seznam_vstupu = []#Sem ukladam radky vstupu do serazenych slovniku
slovnik_pomocny = collections.OrderedDict()#Pomocnici k peknemu rozsekani a rozcleneni jednotlivych radku

seznam_kombinaci = []
#sem chci ukladat vafiltrovane kombinace
#Ukladat chci jen cisla radku, ktere se nasledne znovuoveri a promazou

seznam_indexu = ["source", "destination", "departure", "arrival", "flight_number", "price", "bags_allowed", "bag_price"]
#Je toto nutno komentovat? Nu uvidime zitra rano :-)

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

def sedi_destinace(d1,d2):
    return d1 == d2

def nacteni_vstupu(zdroj_vstupu):
    seznam_pomocny = []
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
#Funkce na parovani letu dle casu priletu/odletu a destinaci
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

def retezeni_letu_v2(seznam_dvojic):
    pojistka = []
    pomocny_seznam = []
    for pivotni_radek in range(len(seznam_dvojic)):
    #otestuji kazdy radek
        for testovany_radek in range(len(seznam_dvojic)):
        #otestuji kazdy clen v pivotnim radku
            if pivotni_radek == testovany_radek:
            #netestuji stejny radek proti sobe
                continue
            for testovany_index in range(len(seznam_dvojic[testovany_radek])):
            #testuji na kazdem jinem radku kazdy clen an to, jestli je stejny s poslednim clenem pivotniho radku
                if seznam_dvojic[pivotni_radek][-1] == seznam_dvojic[testovany_radek][testovany_index] and testovany_index < len(seznam_dvojic[testovany_radek])-1:
                #Musim overit, ze kyzeny clen v testovanem radku neni na konci...
                    pojistka.append(list.copy(seznam_dvojic[pivotni_radek]))
                    pojistka[-1].append(seznam_dvojic[testovany_radek][testovany_index+1])
                    #Sem a na odpovidajici misto dole staci pridat cyklus, ktery pridava vsechny nasledujici cleny, ale uz jdu spat. Doubrou
                    #Toto jiz neni potreba, dokonce to s touto verzi kodu neni mozne, nebo to spis ja neumim
                    #Vyreseno vhodne cyklenym volanim funkce
                    #Vtip je ten, ze ja vzdy pridam jen jedno cislo od hledaneho cisla vpravo
                    #Coz neni na skodu, ale to jsem si predtim nemyslel
                    if pojistka[-1] in seznam_dvojic:
                        continue
                    #Pojistka proti duplovani zapisu
                    pomocny_seznam.append(list.copy(seznam_dvojic[pivotni_radek]))
                    pomocny_seznam[-1].append(seznam_dvojic[testovany_radek][testovany_index+1])
                    #samotne zapsani a vraceni nove nalezene kombinace
                    return pomocny_seznam[-1]


def rozkodovani_retezce(seznam_letu, kombinace_k_rozkodovani,):
    for i in range(len(kombinace_k_rozkodovani)):
        print(seznam_vstupu[i], i, "/n")
#Tyto dve funkce je treba prehodnotit... jejich styl, return a prinos...
def rozkodovani_pozice_retezce(seznam_letu, kombinace_k_rozkodovani, pozice):
    print(len(kombinace_k_rozkodovani))
    i = 0
    for i in range(len(kombinace_k_rozkodovani)):
        print(seznam_vstupu[i][pozice])
        print(i)

nacteni_vstupu("vstup.txt")#Nacteni vstupu z daneho zdrojaku, pozdeji to udelam na vstup ze soubor udle zadani uzivatele
for i in range(len(seznam_vstupu)):
    parovani_letu(seznam_vstupu, i)
#sparovani letu, neni co dodat

while retezeni_letu_v2(seznam_kombinaci) != None:
    seznam_kombinaci.append(retezeni_letu_v2(seznam_kombinaci))
#V seznamu kombinaci se budou hledat a pridavat vhodne kombinace az do chvile, kdy uz algoritmus
#zadnou novou kombinaci nenajde, v tu chvili se apend neprovadi

for k in range(len(seznam_kombinaci)):
    print(k, seznam_kombinaci[k])
#jen rutinni vypis, at vim, co se deje :-)

#print(rozkodovani_retezce(seznam_vstupu, seznam_kombinaci[-1]))
#print(rozkodovani_pozice_retezce(seznam_vstupu, seznam_kombinaci[-1], "destination"))
