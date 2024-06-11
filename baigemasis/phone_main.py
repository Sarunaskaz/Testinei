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
            print('Įveskite telefono parametrus, kad būtų galima nuspėti jo kaina')
            os = input('Įveskite operacine sistema: android ar ios: ')
            battery_capacity = int(input('Įveskite baterijos dydį: '))
            fast_charging_available = int(input('Įveskite skaičių atitinkantį jūsų norima pasirenkimą: 0 - neturi greito ikrovimo, 1 - turi greita ikrovima: '))
            internal_memory = int(input('Įveskite vidinės atminties dydį: '))
            screen_size = float(input('Įveskite ekrano dydį: '))
            primary_camera_rear = int(input('Įveskite galinės kameros pixelių kiekį: '))
            primary_camera_front = int(input('Įveskite priekinės kameros pixelių kiekį: '))
            proccesor_encoded = int(input('Įveskite skaičių atitinkantį jūsų norimą procesorių: snapdragon: 0, exynos: 1, dimensity: 2, bionic: 3, helio: 4, unisoc: 5, tiger: 6, nan: 7, google: 8, sc9863a: 9, spreadtrum: 10, fusion: 11, kirin: 12, mediatek: 13: '))
            has_5g_encoded = int(input('Ar turi 5g : 0 - neturi, 1 - turi: '))
            
            telefonas = telefonu_spejimas.add_phone(
                os, battery_capacity, fast_charging_available, internal_memory,
                screen_size, primary_camera_rear, primary_camera_front,
                proccesor_encoded, has_5g_encoded
            )
            print(f'Telefonas su OS {os} buvo pridėtas su prognozuojama kainą: {telefonas.price}')

        elif pasirinkimas == '3':
            lentele = input('Įveskite lentelės pavadinimą "phones": ')
            telefonu_spejimas.get_all_phones(lentele)

        elif pasirinkimas == '4':
            phone_id = int(input('Įveskite telefono id esantį phones lentelėje, kad ištrintumėte įrašą: '))
            telefonu_spejimas.delete_phone(phone_id)
            print(f'Phones lentelėje esantis įrašas id:{phone_id}, buvo ištrintas')


if __name__ == '__main__':
    main()