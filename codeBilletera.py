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

	# Metodo Saldo
	# Descripcion: retorna el monto disponible que se tiene para consumir, es decir el saldo
	def saldo(self):

		saldoTotal = 0 

		# Verificamos que haya credito en la lista de credito
		try:
			assert(len(self.creditos) != 0)
		# De lo contario, se cierra el programa
		except:
			print("Error: No hay credito")
			return 0
		
		saldoTotal = self.montoTotalCreditos() - self.montoTotalDebitos()

		return saldoTotal

	# Metodo Recarga
	# Descripcion: anade un objeto tipo credito a la lista de creditos.
	def recargar(self, monto, fechaTrans, idEstablecimiento):
		
		# Verificamos que el monto a recargar sea mayor a cero
		try: 
			assert(monto > 0)
		# De lo contrario, se cierra el programa
		except:
			print("Error: no introdujo saldo suficiente")
			return False
		
		# Instanciamos el objeto credito
		cre = Creditos(monto, fechaTrans,idEstablecimiento)
		# Anadimos objeto credito a la lista de creditos
		self.creditos.append(cre)

		print("Se recargo: " + str(monto))

		return True

	# Metodo Consumir
	# Descripcion: anade un objeto tipo debito a la lista de debitos.
	def consumir(self, monto, fechaTrans, idEstablecimiento, pin):

		# Verificamos que codigo secreto introducido se igual al de la persona que consume,
		# que el saldo disponible alcance para consumir el monto introducido y que el monto 
		# introducido sea mayor a cero
		try:
			assert(self.pin == pin and self.saldo() >= monto and monto > 0)
		# De lo contraio, se cierra el programa
		except:
			print("Error: no posee saldo suficiente o ingreso pin invalido")
			return False 

		# Instaciamos objeto debito
		de = Debitos(monto, fechaTrans, idEstablecimiento)
		# Anadimos objeto debito a la lista de debitos
		self.debitos.append(de)

		print("Se consumio: " + str(monto))

		return True








