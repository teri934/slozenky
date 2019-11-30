

def sablona1():
    zoznam = [[] for _ in range(20)]
    cisla = 'nula jeden dva tri štyri päť šesť sedem osem deväť desať jedenásť dvanásť trinásť štrnásť pätnásť šestnásť sedemnásť osemnásť devätnásť'.split(' ')
    i = 0
    for cislo in cisla:
        while i < len(zoznam):
            zoznam[i].append(cislo)
            if i > 0 and i < 5:
                zoznam[i].append('dsať')
            if i > 4 and i < 10:
                zoznam[i].append('desiat')
            if i > 0 and i < 10:
                zoznam[i].append('sto')
            i += 1
            break
    return zoznam

def prevod1(pocet, hodnota, x):
    rad = len(pocet) - 1
    for i in range (len(pocet)):
        hodnota = int(pocet[i])
        if hodnota == 0:    #podmienka pre 0, ktora nema pri viaccifernych cislach slovne vyjadrenie
            rad -= 1
            continue
        if rad > 0:
            if hodnota == 1 and rad == 1:
                x += zoznam[int(str(hodnota)+str(pocet[i+1]))][0]  #podmienka pre viacciferne cisla s konecnymi 10 az 19
                rad -= 1
                break
            elif hodnota == 1 and rad == len(pocet) - 1:     #podmienka, ze nebude na zaciatku vypisovat cislovku jedna 
                x += zoznam[hodnota][rad]
                rad -= 1
            elif hodnota == 2 and rad == len(pocet) - 1 and rad > 1:      #podmienka pre cislovku 200, aby vypisalo dvesto a nie dvasto + osetrenie pre 20, lebo to ma zostat povodne
                x += 'dve' + zoznam[hodnota][rad]
                rad -= 1
            else:
                x += zoznam[hodnota][0] + zoznam[hodnota][rad]
                rad -= 1
        else:
            if hodnota != 0:
                x += zoznam[hodnota][0]
    return x

def prevod2(pocet, x):
    sablona2 = ['tisíc', 'milión', 'miliarda']
    podiel = int(len(pocet)) // 3   #zisti pocet trojic
    zvysok = int(len(pocet)) % 3     #zisti pocet prvych cifier, ktore netvoria trojicu
    hodnota = ''
    if zvysok > 0:                 #ak nebol zvysok nula, tak vypise zvlast hodnotu prvych cifier
        trojice = pocet[:zvysok]
        for p in trojice:
            hodnota += str(p)
        hodnota = int(hodnota)
        if hodnota <= 19:          #zoberie danu hodnotu v zozname a zo sablona2 jej priradi rad
            x += zoznam[hodnota][0] + sablona2[podiel - 1]
        else:
            x += prevod1(trojice, hodnota, x) + sablona2[podiel - 1]   #ak je to > 19, pouzije prevod1 a da hodnote rad
        hodnota = ''
    for i in range(podiel):      #pre jednotlive trojice vola prevod1 a priradi im prislusny rad
        trojice = pocet[zvysok + 3*i:zvysok + 3*i + 3]
        for q in trojice:
            hodnota += str(q)
        hodnota = int(hodnota)
        subvysledok = prevod1(trojice, hodnota, x)
        x = ''                                          #x sa muselo 'vynulovat', lebo kvoli rekurzii dochadzalo k opakovaniu udajov
        if i == podiel - 1:
            return subvysledok
        elif hodnota == 0:                           #pripad, ked je hodnota 0, aby nevypisovalo rady
            x += subvysledok
            hodnota = ''
            continue
        else:
            x += subvysledok + sablona2[podiel - 2 - i]
        hodnota = ''


def prevod(zoznam):
    x = ''
    hodnota = input()
    try: 
        hodnota = int(hodnota)
    except: 
        if hodnota == 'Koniec':
            return('Koniec')
        else:
            return('Nesprávny údaj.')
    hodnota = int(hodnota)
    if hodnota <= 19:         #ak je cislo mensie ako 20, tak rovno vypisem kompletne cislo zo zoznamu
        vysledok = zoznam[hodnota][0]
    else:
        pocet = list(str(hodnota))
        if len(pocet) <= 3:    #ak je cislo trociferne a mensie, urobi prevod1
            vysledok = prevod1(pocet, hodnota, x)
        if len(pocet) > 3:      #ak je vacsie ako trojciferne, urobi prevod2
            vysledok = prevod2(pocet, x)
    return vysledok




zoznam = sablona1()
print('Zadaj postupne čísla, ktoré chceš vypísať. Pokiaľ zadáš niečo, čo nie je číslo, tak to program oznámi. Ak chceš skončiť, napíš "Koniec".')
while True:
    vypis = prevod(zoznam)
    if vypis == 'Koniec':
        print('************************************************************************************************************************')
        break
    else:
        print(vypis)