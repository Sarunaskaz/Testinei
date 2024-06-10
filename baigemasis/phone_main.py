from phone_class import PhonePrediction

def main():
    telefonu_spejimas = PhonePrediction()

    while True:
        print('\nPasirinkite veiksmą:')
        print('1 - baigti darbą')
        print('2 - nuspeti telefono kaina')
        print('3 - Rodyti visas vartotojo įvestis')
        print('4 - Ištrinti iš duomenų bazės telefona')

        pasirinkimas = input('Iveskite pasirinkimo numeri: ')

        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite telefono parametrus, kad būtų galima nuspėti jo kaina')
            os = input('Iveskite operacine sistema: android ar ios: ')
            battery_capacity = int(input('Iveskite baterijos dydį: '))
            fast_charging_available = int(input('Iveskite skaičių atitinkančia jūsų norima pasirenkima: 0 - neturi greito ikrovimo, 1 - turi greita ikrovima: '))
            internal_memory = int(input('Iveskite vidinės atminties dydį: '))
            screen_size = float(input('Iveskite ekrano dydį: '))
            primary_camera_rear = int(input('Iveskite galinės kameros pixeliu kiekį: '))
            primary_camera_front = int(input('Iveskite priekinės kameros pixeliu kiekį: '))
            proccesor_encoded = int(input('Iveskite skaičių atitinkantį jūsų norima procesorių: snapdragon: 0, exynos: 1, dimensity: 2, bionic: 3, helio: 4, unisoc: 5, tiger: 6, nan: 7, google: 8, sc9863a: 9, spreadtrum: 10, fusion: 11, kirin: 12, mediatek: 13: '))
            has_5g_encoded = int(input('Ar turi 5g : 0 - neturi, 1 - turi: '))
            
            telefonas = telefonu_spejimas.add_phone(
                os, battery_capacity, fast_charging_available, internal_memory,
                screen_size, primary_camera_rear, primary_camera_front,
                proccesor_encoded, has_5g_encoded
            )
            print(f'Telefonas su OS {os} buvo pridėtas su prognozuojama kainą: {telefonas.price}')

        elif pasirinkimas == '3':
            lentele = input('Įveskite lenteles pavadinimą "phones": ')
            telefonu_spejimas.get_all_phones(lentele)

        elif pasirinkimas == '4':
            phone_id = int(input('Įveskite phone_id, kad ištrintumėte įrašą: '))
            telefonu_spejimas.delete_phone(phone_id)
            print(f'Telefonas su id {phone_id} buvo ištrintas')


if __name__ == '__main__':
    main()