import urllib2
import time
import datetime

accionAExtraer = 'KO', 'CAT'

def extraerDatos(accion):

	try:

		print 'Extrayendo', accion
		print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


		archivo = accion + '.txt'
		urlAVisitar = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+accion+'/chartdata;type=quote;range=5d/csv'
		
		try:

			leerDatosExistentes = open(archivo, 'r').read()
			separarExistente = leerDatosExistentes.split('\n')
			lineaMasReciente = separarExistente[-2]
			ultimoUnix = int(lineaMasReciente.split(',')[0])

		except Exception, e:
			print str(e)
			ultimoUnix = 0

		guardarArchivo = open(archivo, 'a')
		codigoFuente = urllib2.urlopen(urlAVisitar).read()
		separarFuente = codigoFuente.split('\n')

		for cadaLinea in separarFuente:
			separarLineas = cadaLinea.split(',')
			if len(separarLineas) == 6:
				if 'values' not in cadaLinea:
					guardarArchivo = open(archivo, 'a')
					lineaAEscribir = cadaLinea + '\n'
					guardarArchivo.write(lineaAEscribir)
		guardarArchivo.close()
		
		print 'Extraido', accion
		print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		time.sleep(1)


	except Exception, e:

		print 'No ha funcionado, hay un problema en:', str(e)

'''EJECUTAMOS LA FUNCION UNA VEZ'''
#extraerDatos(accionAExtraer)
'''EJECUTAMOS LA FUNCION EN BUCLE PARA CADA VALOR'''
# for cadaAccion in accionAExtraer:
# 	extraerDatos(cadaAccion)
'''EJECUTAMOS LA FUNCION AUTOMATICAMENTE CADA X TIEMPO'''
while True:
	for cadaAccion in accionAExtraer:
		extraerDatos(cadaAccion)
	time.sleep(1)
