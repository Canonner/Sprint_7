import datetime as dt
from datetime import date as d

url = 'https://qa-scooter.praktikum-services.ru'


class OrderData:

    colors = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]

    tomorrow_date = (d.today() + dt.timedelta(days=1)).strftime("%Y-%m-%d")
    payload_order = {
        "firstName": "Наполеон",
        "lastName": "Бонапарт",
        "address": "ул. 29 флореаля 12 года",
        "metroStation": 34,
        "phone": "+180518041104",
        "rentTime": 1,
        "deliveryDate": tomorrow_date,
        "comment": "привезти на остров Святой Елены"
    }


class CourierData:
    creation_missing_fields = [
        {"login": "Halsey", "firstName": "Bill"},
        {"password": "1944", "firstName": "Bill"},
    ]
