# -*- coding: utf-8 -*-
# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 3
# Autores:
#   - Fabiola Martinez 1310838
#   - Yarima Luciani 1310770
# Descripcion: programa que maneja una billetra electronica. 
import sys

# Clase Credito
# Descripcion: objeto tipo credito que tienen como atributos monto, fecha de transaccion y id del establecimiento
class Creditos:
	def __init__(self, monto, fechaTrans, idEstablecimiento):
		self.monto = monto
		self.fechaTrans = fechaTrans
		self.idEstablecimiento = idEstablecimiento

# Clase Debito
# Descripcion: objeto tipo debito que tiene como atributos monto, fecha de transaccion y id del establecimiento
class Debitos:
	def __init__(self, monto, fechaTrans, idEstablecimiento):
		self.monto = monto
		self.fechaTrans = fechaTrans
		self.idEstablecimiento = idEstablecimiento

# Clase Billetera Electronica
# Descripcion: obtejo tipo billetera electronica que tiene como atributos datos personales, codigo secreto del 
# usuario (pin) para realizar transacciones y, objetos tipo credito y debito.
class BilleteraElectronica:
	
	def __init__(self, identificador, primerNombre, segundoNombre, primerApellido, segundoApellido, ci, pin, creditos, debitos):
		self.identificador = identificador
		self.primerNombre= primerNombre
		self.segundoNombre = segundoNombre
		self.primerApellido = primerApellido
		self.segundoApellido = segundoApellido
		self.ci = ci
		self.pin = pin
		# Lista que almacena objetos tipo credito
		self.creditos = []
		# Lista que almacena objetos tipo debito
		self.debitos = []

	# Metodo Monto Total de Creditos
	# Descripcion: se encarga de calcular el monto total de todos los objetos tipo credito.
	def montoTotalCreditos(self):

		totalCredito = 0

		# Iteramos en la lista que almacena objetos tipo credito para sumarlos 
		for credito in self.creditos:
			totalCredito += credito.monto

		return totalCredito

	# Metodo Monto Total de Debitos
	# Descripcion: se encarga de calcular el monto total de todos los objetos tipo debito.
	def montoTotalDebitos(self):

		totalDebito = 0

		# Iteramos en la lista que almacena objetos tipo debito para sumarlos 
		for debito in self.debitos:
			totalDebito += debito.monto

		return totalDebito