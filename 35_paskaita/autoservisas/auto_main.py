from auto_class import Autoservisas

def main():

    autoservisas = Autoservisas()

    while True:
        print('\nPasirinkite veiksmą:')
        print('1 - baigti darbą')
        print('2 - prideti mechanika')
        print('3 - prideti klienta')
        print('4 - prideti automobili')
        print('5 - prideti remonta')
        print('6 - perziureti lenteles')
        print('7 - perziureti kliento bendra mokejimo suma: ')
        print('8 - perziureti kliento bendra mokejimo suma uz konkretu automobili: ')

        pasirinkimas = input('Iveskite pasirinkimo numeri: ')

        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite mechaniko informacija')
            vardas = input('vardas ')
            pavarde = input('pavarde ')
            el_pastas = input('el_pastas ')
            valadinis_atlyginimas = input('Iveskite vid_atlyginima ')
            specializacija = input('specializacija ')
            mechanikas = autoservisas.prideti_mechanika(vardas, pavarde, el_pastas, valadinis_atlyginimas,specializacija)
            print(f'mechanikas {mechanikas.vardas} buvo pridetas')
        elif pasirinkimas == '3':
            print('Iveskite kliento informacija')
            vardas = input('vardas ')
            pavarde = input('pavarde ')
            el_pastas = input('el_pastas ')
            klientas = autoservisas.prideti_klienta(vardas, pavarde, el_pastas)
            print(f'klientas {klientas.vardas} buvo pridetas')
        elif pasirinkimas == '4':
            print('Iveskite kliento informacija')
            valstybinis_nr = input('valstybinis_nr ')
            marke = input('marke ')
            modelis = input('modelis ')
            kliento_id = input('kliento_id ')
            klientas = autoservisas.prideti_automobili(valstybinis_nr, marke, modelis, kliento_id)
        elif pasirinkimas == '5':
            print('Iveskite remontui reikalinga informacija')
            kliento_id = input('Iveskite kliento_id ')
            mechaniko_id = input('Iveskite mechaniko_id ')
            darbo_pradzia = input('Iveskite darbo_pradzia ')
            darbo_pabaiga = input('Iveskite darbo_pabaiga ')
            remonto_kategorija = input('Iveskite remonto_kategorija: ')
            remontas = autoservisas.prideti_remonta(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija)
            print(f'remontas {remontas.remonto_kategorija} buvo pridetas')
        elif pasirinkimas == '7':
            print('Iveskite kliento id')
            kliento_id = input('kliento_id ')
            klientas = autoservisas.kiek_klientas_sumokejas_is_viso(kliento_id)
        elif pasirinkimas == '8':
            print('Iveskite kliento id')
            kliento_id = input('kliento_id ')
            auto_id = input('auto_id ')
            klientas = autoservisas.kiek_klientas_sumokejas_is_viso_uz_viena_auto(kliento_id, auto_id)
        elif pasirinkimas == '6':
             lentele = input('Iveskite lenteles pavadinima mechanikai/klientai/kliento_automobilis/remontas: ')
             while lentele not in ['mechanikai', 'klientai', 'kliento_automobilis', 'remontas']:
                 lentele = input('Iveskite lenteles pavadinima gydytojai/pacientai/susitikimai: ')
             autoservisas.perziureti_irasus(lentele)









if __name__ == '__main__':
    main()