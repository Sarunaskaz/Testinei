import sqlite3
import datetime
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder



phone = pd.read_csv('data/smartphone_cleaned_v5.csv')

from sklearn.preprocessing import LabelEncoder

phone = pd.read_csv('data/smartphone_v2.csv', sep=',')

label_encoder = LabelEncoder()

unique_brand_names = phone['brand_name'].unique()
brand_name_mapping = {name: idx for idx, name in enumerate(unique_brand_names)}
phone['brand_name_encoded'] = phone['brand_name'].map(brand_name_mapping)

unique_model_names = phone['model'].unique()
model_mapping = {name: idx for idx, name in enumerate(unique_model_names)}
phone['model_encoded'] = phone['model'].map(model_mapping)

unique_proccesor_names = phone['processor_brand'].unique()
proccesor_mapping = {name: idx for idx, name in enumerate(unique_proccesor_names)}
phone['proccesor_encoded'] = phone['processor_brand'].map(proccesor_mapping)

unique_has_5g_names = phone['has_5g'].unique()
has_5g_mapping = {name: idx for idx, name in enumerate(unique_has_5g_names)}
phone['has_5g_encoded'] = phone['has_5g'].map(has_5g_mapping)




phone = phone.drop(['model'], axis=1)
phone = phone.drop(['brand_name'], axis=1)
phone = phone.drop(['resolution'], axis=1)
phone = phone.drop(['processor_brand'], axis=1)
phone = phone.drop(['has_nfc'], axis=1)
phone = phone.drop(['has_ir_blaster'], axis=1)
phone = phone.drop(['num_cores'], axis=1)
phone = phone.drop(['processor_speed'], axis=1)
phone = phone.drop(['refresh_rate'], axis=1)
phone = phone.drop(['num_rear_cameras'], axis=1)
phone = phone.drop(['num_front_cameras'], axis=1)
phone = phone.drop(['extended_upto'], axis=1)
phone = phone.drop(['fast_charging'], axis=1)
phone = phone.drop(['os'], axis=1)
phone = phone.drop(['has_5g'], axis=1)

phone = phone.dropna()

phone['price']= phone['price'].fillna(phone['price'].mean())


class Phone:
    def __init__(self,operacion_system, screen_size, pixels_back_camera, pixels_front_camera,batery_size, fast_charger, five_G):
        self.operacion_system = operacion_system
        self.screen_size = screen_size
        self.pixels_back_camera = pixels_back_camera
        self.pixels_front_camera = pixels_front_camera
        self.batery_size = batery_size
        self.fast_charger = fast_charger
        self.five_G = five_G

class Phone_prediction:
    def __init__(self):
        self.conn = sqlite3.connect('duombaze/phone_database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS phones(
            phone_id INTEGER PRIMARY KEY,
            operacion_system VARCHAR(50) NOT NULL,
            screen_size INTEGER NOT NULL,
            pixels_back_camera INTEGER NOT NULL,
            pixels_front_camera INTEGER NOT NULL,
            batery_size INTEGER,
            fast_charger INTEGER NOT NULL,
            five_G INTEGER NOT NULL)""")
        
    def add_phone(self,operacion_system, screen_size, pixels_back_camera, pixels_front_camera,batery_size, fast_charger, five_G):
        phone = Phone(operacion_system, screen_size, pixels_back_camera, pixels_front_camera,batery_size, fast_charger, five_G)
        self.cursor.execute("INSERT INTO phones (operacion_system, screen_size, pixels_back_camera, pixels_front_camera,batery_size, fast_charger, five_G) VALUES (?, ?, ?, ?, ?,?,?)", (operacion_system, screen_size, pixels_back_camera, pixels_front_camera,batery_size, fast_charger, five_G))
        self.conn.commit()
        return phone

    def delete_phone(self, phone_id):
        self.cursor.execute("DELETE FROM phones WHERE phone_id=?", (phone_id,))
        self.conn.commit()

    def update_phone(self, phone_id, operacion_system, screen_size, pixels_back_camera, pixels_front_camera, batery_size, fast_charger, five_G):
        self.cursor.execute("""UPDATE phones SET operacion_system=?, screen_size=?, pixels_back_camera=?, pixels_front_camera=?, batery_size=?, fast_charger=?, five_G=?
                               WHERE phone_id=?""",
                            (operacion_system, screen_size, pixels_back_camera, pixels_front_camera, batery_size, fast_charger, five_G, phone_id))
        self.conn.commit()


    def get_all_phones(self):
        self.cursor.execute("SELECT * FROM phones")
        return self.cursor.fetchall()
    
    def model_train(self,X, Y):
        polynomia = PolynomialFeatures(degree=2)
        X_poly = polynomia.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_poly, Y, test_size=0.2, random_state=42)

        model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=10000))
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        return r2

    def close(self):
        self.conn.close()
    


telefonas = Phone_prediction()

# telefonas.model_train(phone['price'], phone['price'])

# telefonas.add_phone('android', 6, 64, 32, 1, 1, 1)
# telefonas.delete_phone(1)
# telefonas.update_phone(1, 'IOS', 6, 16, 8, 4500, 1, 1)

# telefonas.add_phone('android', 6, 64, 32, 4000, 1, 1)


r2_score = telefonas.model_train(phone[['price']], phone['price'])
print(r2_score)

