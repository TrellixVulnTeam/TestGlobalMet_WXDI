# -*- coding: utf-8 -*-
import requests
import datetime
import pytz
import csv


def get_observation_data():
    auth_token = "ea86a649b495c8cb159b32a89099359503f8ff28"

    response = requests.get("https://globalmet.mx/estaciones/conditions/78/", headers={"authorization":("Token %s" % auth_token)})

    return response.json()

def create_csv(data):
    with open('observacion.csv','w') as output:
        csvwriter = csv.writer(output)
        for row in data.items():
            csvwriter.writerow(row) 
    
    print "Archivo observacion.csv creado"