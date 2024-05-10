from ligonine_class import Ligonine

def main():
    ligonine = Ligonine()

    while True:
        print('\n Pasirinkite veiksma: ')
        print('1 - baigti darba')
        print('2-prideti gydytoja')
        print('3-prideti pacienta')
        print('4-prideti susitikima')
        print('5-perziureti lentele')

        pasirinkimas = input('Iveskite pasirinkimo numeri: ')

        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite gydytojo informacija')
            vardas = input('vardas ')
            pavarde = input('pavarde ')
            specializacija = input('specializacija ')
            el_pastas = input('el_pastas ')
            gydytojas = ligonine.prideti_gydytoja(vardas, pavarde, specializacija, el_pastas)
            print(f'gydytojas {gydytojas.vardas} buvo pridetas')
        elif pasirinkimas == '3':
            print('Iveskite paciento informacija')
            vardas = input('vardas ')
            pavarde = input('pavarde ')
            gimimoData = input('Iveskite gimimo data ')
            lytis = input('Iveskite lytį ')
            el_pastas = input('el_pastas ')
            gydytojo_id = int(input('Iveskite gydytojo id'))
            pacientas = ligonine.prideti_pacienta(vardas, pavarde, gimimoData, lytis, el_pastas, gydytojo_id)
            print(f'pacientas {pacientas.vardas} buvo pridetas')
        elif pasirinkimas == '4':
             print('Iveskite susitikimo informacija')
             paciento_id = input('Paciento_id: ')
             gydytojo_id = input('Gydytojo_id: ')
             susitikimo_data = input('Vizito data: ')
             paskirtis = input('Paskirtis: ')
             komentarai = input('Komentarai: ')
             susitikimo_id = ligonine.prideti_susitikima(paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai)
             susitikimas = ligonine.gauti_susitikimo_info_pagal_id(susitikimo_id)
             pac_vardas, gyd_vardas, data = susitikimas # unpackinam.
             print(f'Susitikimas {gyd_vardas} {pac_vardas} {data} buvo pridetas.')
        elif pasirinkimas == '5':
             lentele = input('Iveskite lenteles pavadinimas: ')
             ligonine.perziureti_irasus(lentele)
             
        else:
            print('Pasirinkimas neteisingas bandykite dar karta! ')

if __name__ == '__main__':
    main()