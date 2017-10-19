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
