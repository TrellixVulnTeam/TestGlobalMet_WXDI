# -*- coding: utf-8 -*-

import requests
import datetime
import pytz
import csv

from functions.utils import get_observation_data, create_csv

def main():

    data = get_observation_data()

    data = data.pop('current_observation')

    #Conversion y formateo zona horaria

    format = "%Y-%m-%dT%H:%M:%S"

    date = datetime.datetime.strptime(data['fecha_medicion'][:-1], format)

    utc_tz = pytz.timezone('UTC')
    local_tz = pytz.timezone('America/Hermosillo')

    #Conversiones

    temp_f = float(data["temp_c"]*9/5) + 32
    wind_mph = float(data["wind_kph"]*0.62)
    precip_today_inches = float(data["precip_today_metric"]*25.4) 

    #Print datos solicitados

    print "-------------------"
    print "Observación actual:"
    print "-------------------\n"
    print "Fecha de medición: \t\t\t%s" % utc_tz.localize(date).astimezone(local_tz)
    print "Temperatura grados celsius: \t\t\t%s °C" % data["temp_c"]
    print "Temperatura grados fahrenheit: \t\t\t%s °F" % temp_f
    print "Viento kph: \t\t\t\t\t%s Kph" % data["wind_kph"]
    print "Viento mph: \t\t\t\t\t%s Mph" % wind_mph
    print "Direccion del viento: \t\t\t\t%s" % data["wind_dir"]
    print "Precipitacion acumulada en mm: \t\t\t%s mm" % data["precip_today_metric"]
    print "Precipitacion acumulada en pulg: \t\t%s Pulg" % precip_today_inches
    print "Humedad relativa: \t\t\t\t%s" % data["relative_humidity"]
    print "Evapotranspiracion: \t\t\t\t%s" % data["eto"]
    print "-------------------\n"
    
    #Archivo .csv 
    create_csv(data)
    



if __name__ == "__main__":
    main()