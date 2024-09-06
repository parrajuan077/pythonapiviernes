from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import Relationship
from sqlalchemy.ext.declarative import declarative_base
#Cerar una instancia de la base para crear tablas
Base = declarative_base()
 #Listados de modelo de APLICACION
 #Usuario
 class Usuario(Base):
__tablename__= 'usuarios'
id=Column(Integer,primary_key=True, autoincrement=True)
nombres=Column(String(50))
edad=Column(Integer)
telefono=Column(String (12))
Correo = Column(String(20))
contreseña=Column(String (10))
fechaRegistro=Column(Date)
ciudad = Column(String(50))
 #Gasto
 class Gasto(Base):
__tablename__= 'gasto'
monto=Column(String(20))
fecha=Column(Date)
descripcion=Column(String(50))
nombres=Column(String (50))
 
 class Categorio(Base):
 __tablename__=categoria
nombres=Column(Stringtring(20))
descripcion=Column(String(50))
 #nombreCategoria
 #descripcion
 #fotoicono

 # METODOS DE PAGO
 class METODODEPAGAGO(Base):
 pass
#id
#nombreMetodo
#descripcion

 #Factura
 class FACTURA (Base):
 pass