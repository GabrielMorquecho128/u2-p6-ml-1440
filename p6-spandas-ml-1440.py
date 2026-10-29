import pandas as pd
import numpy as np

serie_amigos=["pedro","morgan","Farfan","El Adrian","Jessie","Eliseo","Mario"]
print("---- serie listado de amigos   NC 1440")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("---- serie listado valor de billetes MX  NC 1440")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("---- serie listado nombre y valor de billetes MX  NC 1440")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)
# diccionario dataFrame
# diccionario de  valor monedas y nombre 
print("datos de diccionario a DataFrame en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras" :["veinte","cincuenta","cien","docientos","quinientos","mil"]
}
tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio de Marco morquecho NC 1440")
