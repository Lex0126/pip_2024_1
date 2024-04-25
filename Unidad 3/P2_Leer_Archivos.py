def cargarArchivo():
    archivo =open("../Unidad 3/Archivos/ejemplo.csv")

    contenidoArchivo = archivo.readlines()
    lineas = [i[0:-2].split(",") for i in contenidoArchivo]
    listanueva = []
    for i in lineas:
        listanueva.append([i[0], int(i[1])])

    return listanueva

if __name__ == "__main__":
    a = cargarArchivo()
    print(a)
