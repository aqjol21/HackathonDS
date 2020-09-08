from django.core.management.base import BaseCommand
from django.db import models
from ...models import Route

import requests
import json
import pandas as pd
import datetime

origin = "NQZ"
destination = "ALA"
month = "2020-09-10"
url_initial = "http://api.travelpayouts.com/v2/prices/month-matrix?currency=kzt&origin={}&destination={}&show_to_affiliates=false&month={}&token=200a89e6d3c3eea2c02ea3b8e200e629"

url_needed = url_initial.format(origin, destination, month)

response = requests.request("GET", url_needed)
data = json.loads(response.text)

codes = {
    "ALA": "Алматы",
    "NQZ": "Нур-Султан",
    "KGF": "Караганда",
    "SCO": "Актау",
    "AKX": "Актобе",
    "GUW": "Атырау",
    "BXH": "Балхаш",
    "KSN": "Костанай",
    "KOV": "Кокшетау",
    "PWQ": "Павлодар",
    "PPK": "Петропавловск",
    "PLX": "Семей",
    "CIT": "Шымкент",
    "TDK": "Талдыкорган",
    "DMB": "Тараз",
    "URA": "Уральск",
    "UKK": "Усть-Каменогорск",
    "DZN": "Жезказган",
}


# class Command(BaseCommand):
#     # def add_arguments(self, parser):
#     #     parser.add_argument(
#     #         "file_name", type=str, help="The txt file that contains the journal titles."
#     #     )

#     def handle(self, *args, **kwargs):
#         # route = Route(
#         #     source="Орал",
#         #     departure="2020-09-08 12:00:00+00:00",
#         #     arrival="2020-09-08 12:00:00+00:00",
#         #     destination="Караганда",
#         #     company="Scat",
#         #     price=13000,
#         #     isPlane=True,
#         #     isTrain=False,
#         #     isBus=False,
#         # )
#         route.save()
#         # file_name = kwargs['file_name']
#         # with open(f'{file_name}.txt') as file:
#         # for row in file:


# class Command(BaseCommand):
#     # def add_arguments(self, parser):
#     #     parser.add_argument(
#     #         "file_name", type=str, help="The txt file that contains the journal titles."
#     #     )

#     def handle(self, *args, **kwargs):
#         for ticket in data["data"]:
#             route = Route(
#                 source=codes[ticket["origin"]],
#                 price=int(ticket["value"]),
#                 destination=codes[ticket["destination"]],
#                 departure=ticket["depart_date"],
#                 company="Unknown",
#                 isPlane=True,
#                 isTrain=False,
#                 isBus=False,
#                 isBusiness=ticket["trip_class"],
#                 duration=ticket["duration"],
#                 distance=ticket["distance"],
#             )
#             route.save()
# file_name = kwargs['file_name']
# with open(f'{file_name}.txt') as file:
# for row in file:
