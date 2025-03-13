import time
'''Libreria time proporciona opciones para lograr una manipulacion del tiempo'''
#hare una prueba con workflows
for hora in range (24):
    for min in range (60):
        for seg in range (60):
            print ("Hora", hora, "minutos", min, "segundos", seg)
            print (hora, ":", min, ":", seg)
            time.sleep(1)
            #la funcion time.sleep() hace pausas segun el tiempo especificado
            #para poder hacer una visualizacion mejor del tiempo
