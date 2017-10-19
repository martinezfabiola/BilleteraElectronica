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

	
	# Caso Esquina: consume mas de lo que tiene en el saldo y el pin de consumo es distinto al que tiene registrado
	def testEsquina(self):
		print("Esquina")
		credito5 = Creditos(1000, 26/11/2011, 0000) 
		debito5 = Debitos(0, 27/11/2011, 1234)
		billeteraPablo = BilleteraElectronica(01, "Pablo", "Eduardo", "Gonzalez", "Castro", 26455689, 0006, credito5, debito5)
		recargaPablo = billeteraPablo.recargar(1000, 14/01/2017, 1234)
		consumoPablo = billeteraPablo.consumir(1001, 15/01/2017, 1234, 0007)

	# Caso Malicia: consumo sea un valor negativo 
	def testMalicia3(self):
		print("Malicia 3")
		credito6 = Creditos(1000, 26/11/2011, 0000) 
		debito6 = Debitos(0, 27/11/2011, 1234)
		billeteraPedro = BilleteraElectronica(01, "Pedro", "Enrique", "Guitierrez", "Cedeño", 26455689, 0010, credito6, debito6)
		recargaPedro = billeteraPedro.recargar(1000, 14/01/2017, 1234)
		consumoPedro = billeteraPedro.consumir(-1001, 15/01/2017, 1234, 0010)

	# Caso Malicia: recarga sea un valor negativo 
	def testMalicia4(self):
		print("Malicia 4")
		credito7 = Creditos(1000, 26/11/2011, 0000) 
		debito7 = Debitos(0, 27/11/2011, 1234)
		billeteraCarlos = BilleteraElectronica(01, "Carlos", "Miguel", "Hernandez", "Suarez", 26450089, 0011, credito7, debito7)
		recargaCarlos = billeteraCarlos.recargar(-1000, 14/01/2017, 1234)

if __name__ == '__main__':
	unittest.main()
