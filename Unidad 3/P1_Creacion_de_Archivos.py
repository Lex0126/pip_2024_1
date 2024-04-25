archivo =open("../Unidad 3/Archivos/ejemplo.csv","w")

listaNombres = [
    ["clemente",34],
    ["cristobal",23],
    ["ana",12],
    ["poncho",21],
    ["orozco",19],
    ["jorge",11],
    ["aquino",12],
    ["badillo",37],
    ["segoviano",13],
    ["salazar",14],
    ["Eduardo",15],
    ["natalia",67],
    ["rodrigo",20],
    ["miguel",21],
    ["amando",28],
    ["raul",34],
    ["lexiss",3],
    ["mariana",56],
    ["angel",78],
    ["emmanuel",98],
    ["isaac",99],
    ["checo",90],
    ["paniagua",46]

]
print(listaNombres)

for datosNombre in listaNombres:
    for dato in datosNombre:
        archivo.write(str(dato)+",")
    archivo.write("\n")

archivo.flush()
archivo.close()