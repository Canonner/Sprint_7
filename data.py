import datetime as dt
from datetime import date as d

url = 'https://qa-scooter.praktikum-services.ru'


class OrderData:
    def __init__(self, color):
        tomorrow_date = (d.today() + dt.timedelta(days=1)).strftime("%Y-%m-%d")
        self.payload_order = {
            "firstName": "Chester",
            "lastName": "Nimitz",
            "address": "CINCPAC, COM TF34",
            "metroStation": 34,
            "phone": "+7194410251030",
            "rentTime": 1,
            "deliveryDate": tomorrow_date,
            "comment": "The world wonders",
            "color": color
        }

    colors = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]


class CourierData:
    creation_missing_fields = [
        {"login": "Halsey", "firstName": "Bill"},
        {"password": "1944", "firstName": "Bill"},
    ]

