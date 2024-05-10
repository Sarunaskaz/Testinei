from ligonine_class import Ligonine

def main():
    ligonine = Ligonine()

    while True:
        print('\n Pasirinkite veiksma: ')
        print('1 - baigti darba')
        print('2-prideti gydytoja')
        print('3-prideti pacienta')
        print('4-prideti pacienta')

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
            paciento_id = int(input('Iveskite paciento id '))
            gydytojo_id = int(input('Iveskite gydytojo id '))
            susitikimo_data = input('Iveskite susitikimo data ')
            paskirtis = input('Iveskite susitikimo paskirti ')
            komentarai = input('palikite komentara ')
            susitikimas = ligonine.prideti_susitikima(paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai)
            print(f'susitikimas {susitikimas.susitikimo_data} buvo pridetas')
        else:
            print('Pasirinkimas neteisingas bandykite dar karta! ')

if __name__ == '__main__':
    main()