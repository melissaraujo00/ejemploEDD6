Datos_Basicos = {"Nombres": "Juan Carlos",
                "Apellidos": "Perez Garcia",
                "DUI": "0102453-5",
                "Fecha_Nacimiento": "23/07/1980",
                "Lugar_Nacimiento": "Soya City",
                "Nacionalidad": "Salvadoreña",
                "Estado_civil": "Complicado"
                }

print("\nDetalle del Dicionario")
print("=========================")

print("\nClaves del dicionario: ", Datos_Basicos.keys())
print("\nValores del diccionario: ", Datos_Basicos.values())
print("\nElementos del diccionario: ", Datos_Basicos.items())

print("\nIncripcion del curso")
print("=========================")

print("\nDatos del participante")
print("=========================")

print("DUI: ", Datos_Basicos["DUI"])
print("Nombre completo: ",Datos_Basicos["Nombres"] + " " + Datos_Basicos["Apellidos"])
