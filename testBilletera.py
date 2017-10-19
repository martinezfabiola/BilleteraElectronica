# -*- coding: utf-8 -*-
# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#	- Fabiola Martinez 1310838
#	- Yarima Luciani  1310770
# Descripcion: suite de pruebas unitarias.

from codeBilletera import *                                   
import unittest 

class TestSuite(unittest.TestCase):

	# Caso Frontera: se consume lo que posee como saldo
	def testFrontera(self):
		print("Frontera")
		credito = Creditos(3580, 14/01/2017, 1234) 
		debito = Debitos(0, 15/01/2017, 1234)
		billeteraFabi = BilleteraElectronica(01, "Fabi", "Mercedes", "Martinez", "Perez", 26027714, 0001, credito, debito)
		recargaFabi = billeteraFabi.recargar(3580, 14/01/2017, 1234)
		consumoFabi = billeteraFabi.consumir(3580, 15/01/2017, 1234, 0001)

	# Caso Interior: se mconsume 999 de los 1000
	def testInterior(self):
		print("Interior")
		credito2 = Creditos(1000, 26/11/2011, 0000) 
		debito2 = Debitos(0, 27/11/2011, 1234)
		billeteraYari = BilleteraElectronica(01, "Yari", "Gabriela", "Luciani", "Faccini", 26127714, 0002, credito2, debito2)
		recargaYari = billeteraYari.recargar(1000, 14/01/2017, 1234)
		consumoYari = billeteraYari.consumir(999, 15/01/2017, 1234, 0002)

	# Caso Malicioso: no se tiene suficiente saldo para consumir
	def testMalicia1(self):
		print("Malicia 1")
		credito3 = Creditos(0, 26/11/2011, 0000) 
		debito3 = Debitos(0, 27/11/2011, 1234)
		billeteraDavid = BilleteraElectronica(01, "David", "Ernesto", "Cabeza", "Luque", 24135051, 0003, credito3, debito3)
		recargaDavid = billeteraDavid.recargar(1000, 14/01/2017, 1234)
		consumoDavid = billeteraDavid.consumir(3000, 15/01/2017, 1234, 0003)

	# Caso Malicioso: el pin que se usa para hacer un consumo es distinto al que esta registrado en la billetara electronica.
	def testMalicia2(self):
		print("Malicia 2")
		credito4 = Creditos(0, 26/11/2011, 0000) 
		debito4 = Debitos(0, 27/11/2011, 1234)
		billeteraMari = BilleteraElectronica(01, "Mariano", "Jose", "Rodriguez", "Perez", 27888909, 0004, credito4, debito4)
		recargaMari = billeteraMari.recargar(5000, 14/01/2017, 1234)
		consumoMari = billeteraMari.consumir(3000, 15/01/2017, 1234, 0005)