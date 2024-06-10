import sqlite3
import numpy as np
import pandas as pd
import joblib




class Phone:
    def __init__(self, os_encoded, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded, price):
        self.os_encoded = os_encoded
        self.battery_capacity = battery_capacity
        self.fast_charging_available = fast_charging_available
        self.internal_memory = internal_memory
        self.screen_size = screen_size
        self.primary_camera_rear = primary_camera_rear
        self.primary_camera_front = primary_camera_front
        self.proccesor_encoded = proccesor_encoded
        self.has_5g_encoded = has_5g_encoded
        self.price = price


class PhonePrediction:
    def __init__(self):
        self.conn = sqlite3.connect('duombaze/phone_database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS phones(
            phone_id INTEGER PRIMARY KEY,
            os_encoded INTEGER NOT NULL,
            battery_capacity INTEGER NOT NULL,
            fast_charging_available INTEGER NOT NULL,
            internal_memory INTEGER NOT NULL,
            screen_size DOUBLE NOT NULL,
            primary_camera_rear INTEGER NOT NULL,
            primary_camera_front INTEGER NOT NULL,
            proccesor_encoded INTEGER NOT NULL,
            has_5g_encoded INTEGER NOT NULL,
            price DOUBLE)""")
        self.conn.commit()
        
        #regression model
        self.model = joblib.load('regression_model.joblib')
        
        #OS mapping
        self.os_mapping = {
            'android': 0,
            'ios': 1

        }

        self.expected_columns = [
            'battery_capacity', 'fast_charging_available', 'internal_memory', 'screen_size',
            'primary_camera_rear', 'primary_camera_front', 'proccesor_encoded', 'has_5g_encoded', 'os_encoded'
        ]
        
    def predict_price(self, os, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded):
        os_encoded = self.os_mapping.get(os, -1)  # Encode OS
        
        input_data = pd.DataFrame([{
            'battery_capacity': battery_capacity,
            'fast_charging_available': fast_charging_available,
            'internal_memory': internal_memory,
            'screen_size': screen_size,
            'primary_camera_rear': primary_camera_rear,
            'primary_camera_front': primary_camera_front,
            'proccesor_encoded': proccesor_encoded,
            'has_5g_encoded': has_5g_encoded,
            'os_encoded': os_encoded
        }])

        # pertvarkau kolumus pagal traininimo data
        input_data = input_data[self.expected_columns]

        predicted_price = self.model.predict(input_data)[0]
        round_predicted_price = round(predicted_price, 2)
        
        return round_predicted_price * 0.011 # Predictinu ir (nes data sete rupijos) paverciu i EUR
    
    def add_phone(self, os, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded):
        price = self.predict_price(os, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded)
        os_encoded = self.os_mapping.get(os, -1)
        phone = Phone(os_encoded, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded, price)
        self.cursor.execute("INSERT INTO phones (os_encoded, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (os_encoded, battery_capacity, fast_charging_available, internal_memory, screen_size, primary_camera_rear, primary_camera_front, proccesor_encoded, has_5g_encoded, price))
        self.conn.commit()
        return phone
    
    def delete_phone(self, phone_id):
        self.cursor.execute("DELETE FROM phones WHERE phone_id=?", (phone_id,))
        self.conn.commit()


    def get_all_phones(self, table):
        self.cursor.execute(f'SELECT * FROM {table}')
        rezultattu_sarasas = self.cursor.fetchall()
        print('Irasai pagal jusu uzklausa: ')
        for rezultatas in rezultattu_sarasas:
            print(rezultatas)
#pvz pridejimui
# phone_prediction = PhonePrediction()
# phone = phone_prediction.add_phone('android', 4000, 1, 64, 6, 32, 16, 3, 1)
# phone2 = phone_prediction.add_phone('ios', 6400, 2, 64, 6, 64, 16, 3, 1)
# print(f"Added Phone with Predicted Price: {phone.price}\n {phone2.price}")