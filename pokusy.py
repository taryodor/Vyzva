#tady si chci zkusit nacteni ze zdrojaku a rozsekani na kousky, ulozeni do sloviku a jdu spat
import collections
#Toto importuji proto, abych mohl pouzit serazeny slovnik
#Ten pouzivam jen pro muj komfort :-)
seznam_vstupu = []
#Sem ukladam radky vstupu do serazenych slovniku
seznam_pomocny = []
slovnik_pomocny = collections.OrderedDict()
#Pomocnici k peknemu rozsekani a rozcleneni jednotlivych radku

seznam_indexu = ["source", "destination", "departure", "arrival", "flight_number", "price", "bags_allowed", "bag_price"]
#Je toto nutno komentovat? Nu uvidime zitra rano :-)


with open("vstup.txt") as soubor:
    #Otevru soubor, po radkach(zbavenych koncovych \n) jej ukladam do seznam_pomocny a rovnou jej delim na jednotlive zaznamy
    i = 0
    for radek in soubor.readlines():
        radek = radek.rstrip()
        seznam_pomocny.append(radek.split(","))
    i += 1

for q in range(len(seznam_pomocny)):
    #Tady delim jednotlive seznamy do oklicovanych pozic v orddictu
    for w in range(len(seznam_pomocny[q])):
        slovnik_pomocny[seznam_indexu[w]] = seznam_pomocny[q][w]
    seznam_vstupu.append(slovnik_pomocny.copy())
    slovnik_pomocny.clear()

slovnik_pomocny.clear()
seznam_pomocny.clear()
#Pokud se nic nezmeni, Vasich sluzeb jiz nebude zapotrebi

#Testovaci tisknuti neuskodi, ne?
for j in range(len(seznam_vstupu)):
    print(seznam_vstupu[j])
    #print(seznam_vstupu[j][seznam_indexu[-1]])
